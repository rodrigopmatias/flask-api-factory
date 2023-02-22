from flask import Blueprint, Flask

from flask_api_factory import factory_api
from sample.ext.db import db
from sample.ext.openapi import api_doc

from ..models import Owner
from ..serializers import OwnerSerializer

blueprint = Blueprint("owners", __name__, url_prefix="/owners")


def init_app(app: Flask, router: Blueprint) -> None:
    router.register_blueprint(blueprint)


factory_api(blueprint, db, Owner, OwnerSerializer, api_doc=api_doc, ordering=("name",))
