from flask import Blueprint, Flask

from . import owner, pet, pet_type

blueprint = Blueprint("pets", __name__, url_prefix="/v1")


def init_app(app: Flask) -> None:
    pet_type.init_app(app, blueprint)
    owner.init_app(app, blueprint)
    pet.init_app(app, blueprint)

    app.register_blueprint(blueprint)
