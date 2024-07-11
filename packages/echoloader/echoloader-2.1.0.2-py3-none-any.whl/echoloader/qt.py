import sys

import click
import requests
from PyQt6.QtCore import QUrl
from PyQt6.QtGui import QIcon
from PyQt6.QtWebEngineCore import QWebEngineProfile, QWebEnginePage, QWebEngineScript
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtWidgets import QApplication, QMainWindow


class WebBrowser(QMainWindow):
    def __init__(self, url: str, username: str, password: str):
        super(WebBrowser, self).__init__()

        self.browser = QWebEngineView()
        self.profile = QWebEngineProfile('Us2.ai', self.browser)
        self.page = QWebEnginePage(self.profile, self.browser)
        self.browser.setPage(self.page)
        self.browser.load(QUrl(url))
        self.setCentralWidget(self.browser)

        # Set window properties
        self.setWindowTitle("Copilot")
        self.setGeometry(100, 100, 1280, 720)

        self.setWindowIcon(QIcon("assets/logo.png"))
        # Inject JavaScript to save username and password to localStorage
        if username and password:
            self.inject_script(url, username, password)

    def inject_script(self, url, username, password):
        conf = requests.get(f'{url}/assets/config.json')
        conf.raise_for_status()
        conf = conf.json()
        backends = conf['backends']
        root = backends[0]
        apiurl = root['apiurl']
        if '://' not in apiurl:
            apiurl = f'{url}{apiurl}'
        req = requests.post(f'{apiurl}/users/login', json={'username': username, 'password': password})
        req.raise_for_status()
        authentication_result = req.json()['AuthenticationResult']
        id_token = authentication_result['IdToken']
        refresh_token = authentication_result['RefreshToken']
        access_token = authentication_result.get('AccessToken')
        res = ';'.join(f'sessionStorage.setItem("{k}", "{v}")' for k, v in {
            'idToken': id_token,
            'refreshToken': refresh_token,
            'accessToken': access_token,
        }.items() if v)
        js_code = f'(function() {{ {res} }})();'
        script = QWebEngineScript()
        script.setSourceCode(js_code)
        script.setInjectionPoint(QWebEngineScript.InjectionPoint.DocumentReady)
        script.setWorldId(QWebEngineScript.ScriptWorldId.MainWorld)
        script.setRunsOnSubFrames(False)
        self.page.scripts().insert(script)


@click.command
@click.argument('url', type=str)
@click.argument('qapplication', nargs=-1)
@click.option('--username', type=str)
@click.option('--password', type=str)
def main(qapplication, **kwargs):
    app = QApplication([sys.argv[0], *qapplication])
    window = WebBrowser(**kwargs)
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
