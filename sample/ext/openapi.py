from flask import Blueprint, Flask

from flask_api_factory import openapi

blueprint = Blueprint("openapi", __name__, url_prefix="/docs")


def init_app(app: Flask) -> None:
    openapi.init_app(blueprint)
    app.register_blueprint(blueprint)
