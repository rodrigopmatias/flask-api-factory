from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from sample.config import settings

db = SQLAlchemy()


def init_app(app: Flask) -> None:
    app.config["SQLALCHEMY_DATABASE_URI"] = settings.DB_URI
    app.config["SQLALCHEMY_ECHO"] = settings.DB_ECHO

    db.init_app(app)
