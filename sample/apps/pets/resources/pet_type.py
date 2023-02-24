from flask import Blueprint, Flask
from flask_sqlalchemy.query import Query

from flask_api_factory import factory_api
from flask_api_factory.filter import FilterBase, add_filter
from sample.ext.db import db
from sample.ext.openapi import api_doc

from ..models import PetType
from ..serializers import PetTypeSerializer

blueprint = Blueprint("pet_types", __name__, url_prefix="/pet-types")


def init_app(app: Flask, router: Blueprint) -> None:
    router.register_blueprint(blueprint)


class PetTypeFilter(FilterBase):
    @add_filter("name")
    def ilike_name(self, query: Query, value: str) -> Query:
        return query.filter(PetType.name.ilike(f"%{value.lower()}%"))


factory_api(
    blueprint,
    db,
    PetType,
    PetTypeSerializer,
    api_doc=api_doc,
    ordering=("name",),
    filter_class=PetTypeFilter,
)
