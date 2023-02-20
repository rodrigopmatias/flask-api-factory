from flask import Flask

from . import db, jsonify, migrate


def init_app(app: Flask) -> None:
    db.init_app(app)
    migrate.init_app(app)
    jsonify.init_app(app)
