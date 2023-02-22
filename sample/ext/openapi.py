from flask import Blueprint, Flask

from flask_api_factory import openapi
from flask_api_factory.openapi.models import APIContact, APIDoc, APIInfo, APILicense, APIServer

blueprint = Blueprint("openapi", __name__, url_prefix="/docs")

api_doc = APIDoc(
    info=APIInfo(
        title="My API",
        description="Somente one shot description of API service provide.",
        contact=APIContact(
            name="Rodrigo Pinheiro Matias", url="http://localhost:5000/contact", email="email@sample.com"
        ),
        license=APILicense(name="BSD 3.0", url="http://localhost:5000/license"),
        version="1.0.0",
    ),
    servers=[APIServer(url="http://localhost:5000/v1", description="description")],
)


def init_app(app: Flask) -> None:
    openapi.init_app(blueprint, api_doc)
    app.register_blueprint(blueprint)
