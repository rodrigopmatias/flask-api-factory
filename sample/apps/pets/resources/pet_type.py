from flask import Blueprint, Flask

from flask_api_factory import factory_api
from sample.ext.db import db
from sample.ext.openapi import api_doc

from ..models import PetType
from ..serializers import PetTypeSerializer

blueprint = Blueprint("pet_types", __name__, url_prefix="/pet-types")


def init_app(app: Flask, router: Blueprint) -> None:
    router.register_blueprint(blueprint)


factory_api(blueprint, db, PetType, PetTypeSerializer, api_doc=api_doc, ordering=("name",))
