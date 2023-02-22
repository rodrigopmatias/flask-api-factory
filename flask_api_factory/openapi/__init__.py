from flask import Blueprint, Flask

from .models import APIDoc

blueprint = Blueprint("flask-api-factory-openapi", __name__, url_prefix="")


def init_app(app: Flask, api_doc: APIDoc) -> None:
    @blueprint.get("/openapi.json")
    def get():
        return api_doc.dict(), 200

    app.register_blueprint(blueprint)
