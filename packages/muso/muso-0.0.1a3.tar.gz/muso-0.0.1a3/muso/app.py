# -*- coding: UTF-8 -*-

from typing import Any, List

from starlette.applications import Starlette
from starlette.types import Receive, Scope, Send

from muso.route import RouteGroup


class Muso:

    def __init__(self, config: Any):
        self._starlette = Starlette(debug=config.MUSO_DEBUG)
        self._route_group_list: List[RouteGroup] = []

    def add_route_group(self, *, route_group: RouteGroup):
        self._route_group_list.append(route_group)

    async def __call__(self, scope: Scope, receive: Receive, send: Send,
                       ) -> None:
        for api in self._route_group_list:
            for route in api.route_list:
                self._starlette.add_route(
                    path=route.path, route=route.endpoint,
                    methods=[route.method])
        scope['app'] = self._starlette
        if self._starlette.middleware_stack is None:
            self._starlette.middleware_stack = \
                self._starlette.build_middleware_stack()
        await self._starlette.middleware_stack(scope, receive, send)
