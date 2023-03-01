import os

import pytest
from flask import Flask

from sample import create_app
from sample.ext.db import db


@pytest.fixture(scope="function")
def app() -> Flask:
    os.environ.update({"DB_URI": "sqlite:///", "DB_ECHO": "on"})

    app = create_app()

    with app.app_context():
        db.create_all()

    yield app

    with app.app_context():
        db.drop_all()
