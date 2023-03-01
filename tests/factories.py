import factory
from factory.alchemy import SQLAlchemyModelFactory
from faker import Faker

from sample.apps.pets.models import PetType
from sample.ext.db import db

faker = Faker()


class PetTypeFactory(SQLAlchemyModelFactory):
    name = factory.LazyFunction(faker.first_name)

    class Meta:
        model = PetType
        sqlalchemy_session = db.session
