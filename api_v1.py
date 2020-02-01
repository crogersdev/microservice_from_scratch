#!/usr/bin/env python3

"""
file  : api_v1.py
author: Pat Foo
why   : rest endpoints (v1) for the Foo microservice
"""

# python modules

# pip/conda modules
import aiohttp_cors
from aiohttp import web

# Foo Inc modules

routes = web.RouteTableDef()


@routes.get('/foo/{foo_id}')
async def get_foo_by_id(request):
    print('i got a foo id')
    return web.Response(
        body="Here's your foo!",
        status=200
    )


@routes.post('/foo')
async def add_foo(body):
    print('im supposed to add a new foo')
    pass


def create_foo_webapp(loop):
    foo_webapp = web.Application(loop=loop)

    # TRICKY: Please remove me when this is no longer in dev.
    cors = aiohttp_cors.setup(foo_webapp)
    for r in routes:
        resource = cors.add(foo_webapp.router.add_resource(r.path))
        cors.add(
            resource.add_route(r.method, r.handler),
            {'*': aiohttp_cors.ResourceOptions(
                allow_credentials=True,
                expose_headers=("X-Custom-Server-Header",),
                allow_headers=("X-Requested-With", "Content-Type"),
                max_age=3600)
             }
        )
    foo_webapp.router.add_routes(routes)
    return foo_webapp
