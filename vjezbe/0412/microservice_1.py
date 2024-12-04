import aiohttp
import asyncio
from aiohttp import web
async def handle_service1(request):
    return web.json_response({"message": "Hello from Microservice 1"})
app = web.Application()
app.router.add_get('/', handle_service1)
web.run_app(app, port=8081)