from flask import Blueprint, Flask

from flask_api_factory import factory_api
from sample.ext.db import db
from sample.ext.openapi import api_doc

from ..models import Pet
from ..serializers import PetSerializer

blueprint = Blueprint("pets", __name__, url_prefix="/pets")


def init_app(app: Flask, router: Blueprint) -> None:
    router.register_blueprint(blueprint)


factory_api(
    blueprint,
    db,
    Pet,
    PetSerializer,
    api_doc=api_doc,
    ordering=(
        "name",
        "-born_date",
    ),
)
