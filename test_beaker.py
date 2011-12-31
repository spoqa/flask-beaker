import unittest

from flask import Flask
from flaskext.beaker import Beaker
from flaskext.testing import TestCase

class BeakerTestCase(TestCase):
    def create_app(self):
        app = Flask(__name__)
        app.debug = True
        
        app.secret_key = 'for testing...'
        Beaker(app)
        
        self.app = app
        return app
    def test(self):
        from flask import session, request

        def _set():
            assert request.environ.has_key("beaker.session")
            session['key'] = "value"
            return "ok"
            
        self.app.add_url_rule('/set_value', 'set_value', _set)
        with self.app.test_client() as c:
            c.get("set_value")
            assert session['key'] == "value"


    
