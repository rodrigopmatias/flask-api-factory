from flask import Flask

from . import db, json, migrate, openapi


def init_app(app: Flask) -> None:
    db.init_app(app)
    migrate.init_app(app)
    json.init_app(app)
    openapi.init_app(app)
