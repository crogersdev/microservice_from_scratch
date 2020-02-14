#!/usr/bin/env python3
"""
file  : app.py
author: Pat Foo
why   : starts the Foo webapp
"""

# python modules
import asyncio

# pip modules
from aiohttp import web

# twitmap modules
from api_v1 import create_foo_webapp


app = create_foo_webapp(loop=asyncio.get_event_loop())
web.run_app(app, port=5501)
