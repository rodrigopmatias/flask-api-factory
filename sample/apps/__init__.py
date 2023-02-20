from flask import Flask

from . import pets


def init_app(app: Flask) -> None:
    pets.init_app(app)
