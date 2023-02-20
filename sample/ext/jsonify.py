from datetime import date, datetime
from decimal import Decimal

from flask import Flask
from flask.json import JSONEncoder


def init_app(app: Flask) -> None:
    app.json_encoder = __CustomJSONEncoder


class __CustomJSONEncoder(JSONEncoder):
    def default(self, value: any) -> any:
        if isinstance(value, (date, datetime)):
            return value.isoformat()
        if isinstance(value, Decimal):
            return float(value)

        return super().default(value)
