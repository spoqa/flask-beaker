from flask.sessions import SessionInterface
from beaker.middleware import SessionMiddleware

class BeakerSessionInterface(SessionInterface):
    def open_session(self, app, request):
        return request.environ['beaker.session']
    def save_session(self, app, session, response):
        session.save()

class Beaker(object):
    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)
        else:
            self.app = None

    def init_app(self, app):
        app.config.setdefault('BEAKER_SESSION_TYPE', 'file')
        app.config.setdefault('BEAKER_SESSION_URL', None)
        app.config.setdefault('BEAKER_SESSION_DATA_DIR', './.beaker-session')
        app.config.setdefault('BEAKER_SESSION_COOKIE_EXPIRES', True)

        self.app = app
        self._set_beaker_session()

    def _set_beaker_session(self):
        session_opts = {
            'session.type': self.app.config['BEAKER_SESSION_TYPE'],
            'session.data_dir': self.app.config['BEAKER_SESSION_DATA_DIR'],
            'session.url': self.app.config['BEAKER_SESSION_URL'],
            'session.cookie_expires': self.app.config['BEAKER_SESSION_COOKIE_EXPIRES']
            }
        
        self.app.wsgi_app = SessionMiddleware(self.app.wsgi_app, session_opts)
        self.session_interface = BeakerSessionInterface()
