from flask import Flask
from flask_migrate import Migrate

from .db import db

migrate = Migrate()


def init_app(app: Flask) -> None:
    migrate.init_app(app, db)
