from datetime import date, datetime
from decimal import Decimal

from flask import Flask
from flask.json.provider import DefaultJSONProvider


def init_app(app: Flask) -> None:
    app.json = __CustomJSONProvider(app)


class __CustomJSONProvider(DefaultJSONProvider):
    sort_keys = False

    def dumps(self, obj: any, **kwargs: any) -> str:
        return super().dumps(obj, default=self.default, **kwargs)

    def default(self, value: any) -> any:
        if isinstance(value, (date, datetime)):
            return value.isoformat()
        if isinstance(value, Decimal):
            return float(value)

        return super().default(value)
