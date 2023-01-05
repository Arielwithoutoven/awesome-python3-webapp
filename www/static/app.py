# Web App骨架

import asyncio
import json
import logging
import os
import time
from datetime import datetime

import aiomysql
from aiohttp import web

logging.basicConfig(level=logging.INFO)


def index(request):
    return web.Response(body=b"<h1>Awesome<h1>", content_type="text/html")


async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route("GET", "/", index)
    # srv = yield from loop.creat_server(app.make_handler(), "127.0.0.1", 9000)
    srv = await loop.create_server(app.make_handler(), "127.0.0.1", 9000)
    logging.info("server started at http://127.0.0.1:9000...")
    return srv


loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
