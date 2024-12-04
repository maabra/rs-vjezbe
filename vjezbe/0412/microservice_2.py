import aiohttp
import asyncio
from aiohttp import web
async def handle_service2(request):
    return web.json_response({"message": "Hello from Microservice 2"})
app = web.Application()
app.router.add_get('/', handle_service2)
web.run_app(app, port=8082)
