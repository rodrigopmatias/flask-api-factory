from uuid import uuid4

from flask import Flask
from sqlalchemy import Column, ForeignKey
from sqlalchemy import types as Types

from sample.ext.db import db


def init_app(app: Flask) -> None:
    ...


class BaseModel(db.Model):
    __abstract__ = True

    id = Column(Types.String(36), primary_key=True, nullable=False, default=lambda: str(uuid4()))


class PetType(BaseModel):
    name = Column(Types.String(30), nullable=False)

    @property
    def other(self) -> str:
        return "other-value"


class Owner(BaseModel):
    name = Column(Types.String(50), nullable=False)
    phone_number = Column(Types.String(12), nullable=False)


class Pet(BaseModel):
    owner_id = Column(Types.String(36), ForeignKey("owner.id"), nullable=False)
    pet_type_id = Column(Types.String(36), ForeignKey("pet_type.id"), nullable=False)

    name = Column(Types.String(50), nullable=False)
    sex = Column(Types.String(1), nullable=False, default="I")
    born_date = Column(Types.Date(), nullable=True)
