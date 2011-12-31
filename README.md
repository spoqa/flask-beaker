# Flask Beaker

[Flask Beaker] is [Flask] extension for [Beaker] Session.

## How to use

    ```python

    from flask import app, session
    from flaskext.beaker import Beaker

    # setup
    app = Flask(__name__)
    Beaker(app)

    # in handler
    
    @app.route("/set_value")
    def set_value():
        session["key"] = "value"
        return "ok"

    @app.route("/get_value")
    def get_value():
        return session["key"]

[Flask Beaker]: http://github.com/spoqa/flask-beaker
[Flask]: http://flask.pocoo.org/docs/
[Beaker]: http://pypi.python.org/pypi/Beaker
