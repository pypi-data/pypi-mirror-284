# -*- coding: UTF-8 -*-

import orjson
from marshmallow import Schema


class BaseSchema(Schema):
    class Meta:
        render_module = orjson
