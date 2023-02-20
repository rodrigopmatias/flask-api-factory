from flask import Flask

from . import models, resources


def init_app(app: Flask) -> None:
    models.init_app(app)
    resources.init_app(app)
