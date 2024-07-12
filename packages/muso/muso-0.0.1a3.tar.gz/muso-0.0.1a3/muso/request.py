# -*- coding: UTF-8 -*-
from typing import Optional

import orjson
from marshmallow import Schema

from starlette.requests import Request as StarletteRequest


class MusoRequest:

    def __init__(self, starlette_request: StarletteRequest,
                 query_args_schema: Optional[Schema] = None,
                 form_data_schema: Optional[Schema] = None,
                 json_body_schema: Optional[Schema] = None):
        self._starlette_request: StarletteRequest = starlette_request
        self._query_args_schema: Optional[Schema] = query_args_schema
        self._form_data_schema: Optional[Schema] = form_data_schema
        self._json_body_schema: Optional[Schema] = json_body_schema

        self._cached_query_args: Optional[dict] = None
        self._cached_form_data: Optional[dict] = None
        self._cached_json_body: Optional[dict] = None

    def headers(self):
        return self._starlette_request.headers

    async def query_args(self) -> dict:
        if self._cached_query_args is None:
            self._cached_query_args = self._query_args_schema.load(
                self._starlette_request.query_params) or dict()
        return self._cached_query_args

    async def form_data(self) -> dict:
        if self._cached_form_data is None:
            form_data = await self._starlette_request.form()
            self._cached_form_data = self._form_data_schema.load(
                form_data) or dict()
        return self._cached_form_data

    async def json_body(self) -> dict:
        if not hasattr(self._starlette_request, "_json"):
            body = await self._starlette_request.body()
            json_result = orjson.loads(body)
            self._starlette_request._json = json_result
            self._cached_json_body = self._json_body_schema.load(json_result)
        return self._cached_json_body
