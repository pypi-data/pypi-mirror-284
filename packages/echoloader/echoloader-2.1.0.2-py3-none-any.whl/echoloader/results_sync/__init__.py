import asyncio
import datetime
import io
import logging
from collections import defaultdict
from functools import cached_property

import numpy as np
import pymupdf
import requests
from dateutil import parser
from pydicom import dcmread
from pydicom.uid import generate_uid

from echoloader.dimse import destination_to_store
from echoloader.login import unpack
from echoloader.results_sync.hl7_sync import Hl7Sync
from echoloader.results_sync.pdf_sc import generate_pdf_sc

logger = logging.getLogger('echolog')

RESULT_FETCH_RETRIES = 3


def apply_overwrites(overwrites, ds, modality):
    for o in overwrites:
        m, rest = o.split(':', 1)
        if m == modality:
            k, v = rest.split('=', 1)
            if k.endswith('UID') and v.endswith('.'):
                v = generate_uid(prefix=v)
            setattr(ds, k, v)


class ResultsSync:
    def __init__(self, study, args, **kwargs):
        self.study = study
        self.args = args
        self.sid = str(study.get('id'))

        self.protocol = kwargs.get('protocol', {})
        self.last_sync = kwargs.get('last_sync')
        self.sync_source = kwargs.get('sync_source', 'ECHOLOADER')
        self.sync_event = kwargs.get('sync_event', 'ON_DEMAND')
        self.sync_mode = kwargs.get('sync_mode', 'ADVANCED')
        self.dicom_router_config = kwargs.get('dicom_router_config', {})
        self.api_url = kwargs.get('api_url', '')
        self.headers = kwargs.get('headers', {})
        self.db_mods = kwargs.get('mods', {})
        self.params = kwargs.get('params', {})
        self.ds_retrieve_func = kwargs.get('ds_retrieve_func')
        self.pdf_retrieve_func = kwargs.get('pdf_retrieve_func')
        self.audit_func = kwargs.get('audit_func')
        self.overwrite_tags = args.get('overwrite_tags', [])

        self.sr_params = {}
        self.doc_params = {}
        self.pdf_params = {}
        self.ps_params = {}
        self.sc_params = {}
        self.ds_params = {}
        self.sync_status_success = defaultdict(list)
        self.sync_status_failed = defaultdict(list)
        self.is_echoloader = self.sync_source == 'ECHOLOADER'
        self.is_advanced_sync = self.sync_mode == 'ADVANCED'
        self.disable_ts_check = not self.is_echoloader

        if args.get('sync_url'):
            self.sr_params['url'] = True
        if args.get('sync_main_findings'):
            self.sr_params['main_findings'] = True
            self.doc_params['main_findings'] = True
            self.pdf_params['main_findings'] = True
        if args.get('sync_pdf_images'):
            self.doc_params['image'] = True
            self.pdf_params['image'] = True
        if args.get('sync_designators'):
            self.sr_params['designators'] = args.get('sync_designators')
        if args.get('sync_mapping'):
            self.sr_params['mapping'] = args.get('sync_mapping')
        if args.get('sync_regulatory_status'):
            self.sr_params['regulatory_status'] = True
        if args.get('sync_edited_status'):
            self.sr_params['edited_status'] = True
        if args.get('sync_annotations'):
            self.sr_params['annotations'] = True
        if args.get('sync_ds_always_render'):
            self.ds_params['always_render'] = True
        if args.get('sync_ds_standardize'):
            self.ds_params['standardize'] = True

        self.doc_params['dicom_encapsulated_pdf'] = True
        self.by_measurement = args.get('sync_by_measurement', False)
        self.sync_pdf_as_sc = args.get('sync_pdf_as_sc', False)
        self.sync_generate_uid = args.get('sync_generate_uid', False)
        self.sync_same_series = args.get('sync_same_series', False)
        self.hl7_config = self.dicom_router_config.get('hl7_config', {})

        self.grouped_ms = None
        self.sync_destinations = kwargs.get('sync_destinations', {})

    def find_realtime_destinations(self, manual_triggers_present):
        self.grouped_ms = self.read_grouped_ms()

        if not self.is_echoloader:
            return self.sync_destinations

        # If the number of measurements to sync is greater than 0, sync to all destinations
        if len(self.grouped_ms) > 0:
            logger.debug(f'Found {len(self.grouped_ms)} new measurements for {self.study.get("visit", "")}')
            return list(filter(lambda x: x.get('sync_event', 'REAL_TIME') == 'REAL_TIME', self.sync_destinations))

        logger.info(f'No new measurements for {self.study.get("visit", "")}')

        if manual_triggers_present:
            return []

        ds_destinations = [
            destination for destination in self.sync_destinations if
            'DS' in destination.get('sync_modalities', []) and destination.get('sync_event', 'REAL_TIME') == 'REAL_TIME'
        ]

        logger.info(f'Found {len(ds_destinations)} DS destinations for {self.study.get("visit", "")}')
        return ds_destinations

    def find_trigger_destinations(self):
        try:
            triggered_destinations = self.read_manual_triggers()
        except Exception as exc:
            logger.error(f'Failed to fetch manual triggers due to {exc}')
            return []

        if len(triggered_destinations) > 0:
            logger.info(f'Found user triggers for {self.study.get("visit", "")}')
            return triggered_destinations
        else:
            logger.debug(f'No user triggers for {self.study.get("visit", "")}')
        return []

    @cached_property
    def mods(self):
        if not self.is_echoloader:
            return [vars(mod) for mod in self.db_mods]

        page_size = 10_000
        page = 0
        result = []
        count = 1
        while len(result) < count:
            params = {**self.params, 'page': page + 1, 'page_size': page_size}
            try:
                mods = unpack(requests.get(
                    f"{self.api_url}/sync/modification/{self.sid}", params=params, headers=self.headers))
            except Exception as exc:
                logger.warning(f'Failed to fetch modifications due to {exc}')
                if page_size / 2 != page_size // 2:
                    raise exc
                page_size //= 2
                page *= 2
                continue
            result.extend(mods['results'] if isinstance(mods, dict) else mods)
            count = mods['count'] if isinstance(mods, dict) else len(mods)
            page += 1
        return result

    def measurements_by_model(self, model):
        ms = defaultdict(dict)
        for mod in self.mods:
            if mod['model'] == model:
                pk = mod['obj_pk']
                ms[pk].update(mod['new_fields'])
                ms[pk]['id'] = pk
                ms[pk]['last_update'] = parser.parse(mod['creation']).replace(
                    tzinfo=datetime.timezone.utc) if self.is_echoloader else mod['creation']
                if mod['action'] == 'delete' and pk in ms:
                    del ms[pk]
        return ms

    def read_manual_triggers(self):
        triggered_destinations = []
        triggers = unpack(requests.get(
            f"{self.api_url}/sync/{self.sid}/sync_log", params={
                **self.params,
                'filter_by': 'MANUAL_TRIGGERS',
            }, headers=self.headers))

        for trigger in triggers:
            created_dt = parser.parse(trigger.get('created_at')).replace(tzinfo=datetime.timezone.utc)
            if created_dt > self.last_sync and trigger.get('sync_source') == 'ECHOLOADER':
                destination_id = trigger.get('destination_id')
                destination = [destination for destination in self.sync_destinations if destination.get(
                    'id') == destination_id and destination not in triggered_destinations]
                if len(destination) > 0:
                    destination = destination[0]
                    destination['sync_log_id'] = trigger.get('id')
                    triggered_destinations.append(destination)

        return triggered_destinations

    @cached_property
    def measurements(self):
        return self.measurements_by_model('measurement.measurements')

    @cached_property
    def dicoms(self):
        return {k: d for k, d in self.measurements_by_model('dicom.dicom').items()
                if not d.get('from_dicom_id') and d.get('file_type') != 'PLOT'}

    def read_grouped_ms(self):
        ms = self.measurements
        grouped_ms = defaultdict(list)
        for m in ms.values():
            proto = self.protocol.get('measurements', {}).get(str(m.get('code_id')), {})
            if (proto.get('shouldDisplay')
                    and (self.disable_ts_check or m['last_update'] > self.last_sync)
                    and m.get('used')
                    and m.get('dicom_id')
                    and m.get('plot_obj')):
                k = (m['dicom_id'], m['frame'], *([m['id']] if self.by_measurement else []))
                grouped_ms[k].append(m['id'])
        return grouped_ms

    def sync_sc(self, func):
        for ms in self.grouped_ms.values():
            yield func(ms)

    async def sync_sc_pdf(self, func):
        if self.sync_pdf_as_sc and len(self.grouped_ms) > 0:
            pdf_data = await self.pdf()

            if not pdf_data:
                logger.error(f'Failed to fetch PDF for {self.study.get("visit", "")}')
                return

            doc_pdf = pymupdf.open(stream=pdf_data, filetype="pdf")
            for i, page in enumerate(doc_pdf):
                pixmap = page.get_pixmap()
                pdf_page = pixmap.samples
                image_array = (np.frombuffer(pdf_page, dtype=np.uint8)
                               .reshape(pixmap.h, pixmap.w, len(pdf_page) // (pixmap.h * pixmap.w)))

                ds = generate_pdf_sc(image_array, self.study, i)
                yield func([], ds=ds)

            doc_pdf.close()

    def sync_ps(self, func):
        for ms in self.grouped_ms.values():
            yield func(ms)

    def ds(self):
        ds = self.dicoms
        for k, d in ds.items():
            if (self.disable_ts_check or d['last_update'] > self.last_sync) and not d.get(
                    'from_dicom_id') and d.get('output_path'):
                yield {
                    'url': f'{self.api_url}/dicom/ds/{k}',
                    'params': {**self.params, **self.ds_params},
                    'id': k,
                }

    def sr(self):
        return {
            'url': f'{self.api_url}/study/sr/{self.sid}',
            'params': {**self.params, **self.sr_params},
        }

    def ps(self, ms):
        return {
            'url': f'{self.api_url}/dicom/ps',
            'params': {**self.params, **self.ps_params, 'measurements': ms},
        }

    def sc(self, ms, ds=None):
        return {
            'ds': ds,
            'url': f'{self.api_url}/dicom/sc',
            'params': {**self.params, **self.sc_params, 'measurements': ms},
        }

    def doc(self):
        return {
            'url': f'{self.api_url}/study/pdf/{self.sid}',
            'params': {**self.params, **self.doc_params},
        }

    async def pdf(self):
        pdf_content = None

        try:
            if self.is_echoloader:
                res = requests.get(f"{self.api_url}/study/pdf/{self.study.get('id')}", headers=self.headers,
                                   params=self.pdf_params)
                pdf_content = res.content if res.status_code == 200 else None
                if res.status_code != 200:
                    logger.error(f'Failed to fetch from {res.url} - {res.status_code}')
            elif self.pdf_retrieve_func:
                pdf_content = await self.pdf_retrieve_func(self.pdf_params)

            return pdf_content
        except Exception as exc:
            logger.error(f'Failed to fetch PDF due to {exc}')
            return None

    async def retrieve_ds(self, req_obj, modality):
        if req_obj.get('ds'):
            return req_obj.get('ds')

        url = req_obj.get('url')
        params = req_obj.get('params')
        if self.is_echoloader:
            req = requests.get(url, headers=self.headers, params=params)
            try:
                bs = unpack(req)
            except Exception as exc:
                logger.error(f'Failed to fetch {url} due to {exc}')
                raise exc
            ds = dcmread(io.BytesIO(bs))
        elif self.ds_retrieve_func:
            ds = await self.ds_retrieve_func(modality, req_obj)
        else:
            return None
        prefix = '1.2.826.0.1.3680043.10.918.'
        if self.sync_generate_uid:
            ds.SOPInstanceUID = generate_uid(prefix=prefix, entropy_srcs=[f"{self.last_sync}{url}{params}"])
        if self.sync_same_series:
            ds.SeriesInstanceUID = generate_uid(prefix=prefix, entropy_srcs=[str(ds.StudyInstanceUID)])
        apply_overwrites(self.overwrite_tags, ds, modality)
        return ds

    def get_sync_summary(self, destination):
        return str(destination_to_store(destination))

    def update_sync_status(self, sync_destination, sync_status, error_summary):
        if self.is_echoloader:
            sync_log_id = sync_destination.get('sync_log_id')
            unpack(requests.put(f"{self.api_url}/sync/{self.sid}/sync_log/{sync_log_id}",
                                json={
                                    'sync_status': sync_status,
                                    'error_summary': error_summary,
                                    'sync_summary': self.get_sync_summary(sync_destination),
                                }, headers=self.headers))

    def update_sync_started(self, destinations):
        for sync_destination in destinations:
            sync_log_id = sync_destination.get('sync_log_id')
            if not sync_log_id:
                continue
            unpack(requests.put(f"{self.api_url}/sync/{self.sid}/sync_log/{sync_log_id}",
                                json={
                                    'sync_status': 'STARTED',
                                }, headers=self.headers))

    async def log_sync_status(self, destinations):
        for sync_destination in destinations:
            sync_status = ''
            error_summary = ''
            destination_id = sync_destination.get('id')
            if self.sync_status_success.get(destination_id) and not self.sync_status_failed.get(destination_id):
                sync_status = 'SUCCESS'
            elif self.sync_status_success.get(destination_id) and self.sync_status_failed.get(destination_id):
                sync_status = 'PARTIAL'
            elif self.sync_status_failed.get(destination_id):
                sync_status = 'FAILED'

            if self.sync_status_failed.get(destination_id):
                error_summary = '<br>'.join(self.sync_status_failed[destination_id])

            if self.is_echoloader and sync_destination.get('sync_log_id'):
                self.update_sync_status(sync_destination, sync_status, error_summary)
                continue

            sync_log = {
                'sync_source': self.sync_source,
                'sync_event': self.sync_event,
                'study_id': self.sid,
                'destination_id': destination_id if self.is_advanced_sync else None,
                'sync_summary': self.get_sync_summary(sync_destination),
                'error_summary': error_summary,
                'sync_status': sync_status,
                'sync_modalities': sync_destination.get('sync_modalities'),
            }

            if self.is_echoloader:
                unpack(requests.post(f"{self.api_url}/sync/{self.sid}/sync_log", json=sync_log, headers=self.headers))
            elif self.audit_func:
                await self.audit_func(sync_log)

    async def sync_ds(self, dimse_connections, modality, req_obj):
        error_summary = ''
        url = req_obj.get('url')

        for i in range(RESULT_FETCH_RETRIES):
            try:
                logger.info(f'Syncing {url}')
                ds = await self.retrieve_ds(req_obj, modality)
                if ds:
                    break
            except Exception as exc:
                error_summary = f'Failed to fetch {url}, Modality {modality}, #{i + 1} due to {exc}'
                logger.error(error_summary)
        else:
            logger.warning(f'Failed to sync {url}')
            for dimse_connection in dimse_connections:
                self.sync_status_failed[dimse_connection.id].append(
                    error_summary) if modality in dimse_connection.modalities else None
            return

        for dimse_connection in dimse_connections:
            if modality not in dimse_connection.modalities:
                continue
            try:
                called_ae = None
                if self.args.get('customer_aet'):
                    called_ae = self.study.get('customer')

                dimse_connection.store(ds, called_ae)
                logger.info(f'Synced {url} to {dimse_connection}')
                self.sync_status_success[dimse_connection.id].append(url)
            except Exception as exc:
                error_summary = f'Failed to sync {url} to {dimse_connection} due to {exc}'
                logger.error(error_summary)
                self.sync_status_failed[dimse_connection.id].append(error_summary)

    async def sync_study(self, destinations):
        modalities = [modality for destination in destinations for modality in destination.get('sync_modalities', [])]
        dimse_connections = [destination_to_store(sync_destination) for sync_destination in destinations]

        options = {
            'PS': lambda: self.sync_ps(self.ps),
            'SC': lambda: self.sync_sc(self.sc),
            'DS': lambda: self.ds(),
            'SR': lambda: [self.sr()],
            'DOC': lambda: [self.doc()],
        }

        for modality in list(dict.fromkeys(modalities)):
            for req_obj in options[modality]():
                await self.sync_ds(dimse_connections, modality, req_obj)

        if 'SC' in modalities:
            async for req_obj in self.sync_sc_pdf(self.sc):
                await self.sync_ds(dimse_connections, 'SC', req_obj)

        logger.info(f'Study {self.study.get("visit", "")} has been synced')
        await self.log_sync_status(destinations)

    def run_sync_results(self):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        result = loop.run_until_complete(self.sync_results())
        loop.close()
        return result

    async def sync_results(self):
        enable_hl7_sync = False
        logger.info(f"Starting sync for study {self.study.get('visit', '')}")

        trigger_destinations = []
        if self.is_echoloader and self.is_advanced_sync:
            trigger_destinations = self.find_trigger_destinations()

        manual_triggers_present = len(trigger_destinations) > 0
        destinations = self.find_realtime_destinations(manual_triggers_present)

        if len(destinations) > 0:
            await self.sync_study(destinations)
            enable_hl7_sync = self.is_echoloader
        else:
            logger.info(
                f'No measurements found for real time sync, skipping sync for study {self.study.get("visit", "")}')

        # If advanced sync is enabled, sync to manual triggers
        if manual_triggers_present:
            for sync_destination in trigger_destinations.copy():
                if sync_destination in destinations:
                    trigger_destinations.remove(sync_destination)
                    self.update_sync_status(sync_destination, 'SKIPPED', 'Real time sync already completed')

            if len(trigger_destinations) > 0:
                self.disable_ts_check = True
                self.grouped_ms = self.read_grouped_ms()
                self.update_sync_started(trigger_destinations)

                await self.sync_study(trigger_destinations)
                enable_hl7_sync = self.is_echoloader
            else:
                logger.info(f'No manual triggers for {self.study.get("visit", "")}')

        if enable_hl7_sync and self.hl7_config.get('enabled', False):
            kwargs = {
                'measurements': self.measurements,
                'hl7_config': self.hl7_config,
                'protocol': self.protocol,
                'api_url': self.api_url,
                'pdf_params': self.pdf_params,
                'headers': self.headers,
                'is_echoloader': self.is_echoloader,
                'pdf_retrieve_func': self.pdf_retrieve_func,
            }

            try:
                Hl7Sync(self.study, self.args, **kwargs).sync_hl7()
            except Exception as exc:
                logger.error(f'Failed to sync HL7 due to {exc}')
