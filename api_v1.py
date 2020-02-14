#!/usr/bin/env python3

"""
file  : api_v1.py
author: Pat Foo
why   : rest endpoints (v1) for the Foo microservice
"""

# python modules
import logging

# pip/conda modules
from aiohttp import web
import aiohttp_cors

# Foo Inc modules
from FooSvcImpl import FooSvcImpl


routes = web.RouteTableDef()


@routes.get('/foo/{foo_id}')
async def get_foo_by_id(request):

    foo_id = request.get('foo_id')

    foo_svc_impl = FooSvcImpl()
    _ = foo_svc_impl.get_foo(foo_id)

    print(f"Returning a foo, foo_id: {foo_id}")
    return web.Response(
        body="Here's your foo!",
        status=200
    )


@routes.post('/foo')
async def add_foo(body):
    foo_svc_impl = FooSvcImpl()
    status = foo_svc_impl.add_foo(body)

    print('im supposed to add a new foo')
    return web.Response(
        body=f"New foo created! {status}",
        status=200
    )


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
