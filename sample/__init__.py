from flask import Flask

from . import apps, ext


def create_app() -> Flask:
    app = Flask(__name__)

    ext.init_app(app)
    apps.init_app(app)

    return app
