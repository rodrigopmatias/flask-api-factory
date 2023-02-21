from flask import Blueprint, Flask

from .models import APIContact, APIDescription, APIDoc, APILicense, APIServer

blueprint = Blueprint("flask-api-factory-openapi", __name__, url_prefix="")
api_doc = APIDoc(
    desciption=APIDescription(
        title="My API",
        summary="Simple summary of API",
        term_of_service="term_of_service",
        contact=APIContact(name="My API", url="address of contact", email="email@sample.com"),
        license=APILicense(name="License Name", url="license url"),
        version="1.0.0",
        servers=[APIServer(url="http://localhost:5000/v1", description="description")],
    )
)


def init_app(app: Flask) -> None:
    app.register_blueprint(blueprint)


@blueprint.get("/openapi.json")
def get():
    return api_doc.dict(), 200
