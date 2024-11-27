import asyncio
import aiohttp
from aiohttp import web

app = web.Application()

def handler_function(request):
    data = {'ime': 'Ivo', 'prezime': 'Ivić', 'godine': 25}
    return web.json_response(data)
    # print("Hello world")

proizvodi = [
{"id": 1, "naziv": "Laptop", "cijena": 5000},
{"id": 2, "naziv": "Miš", "cijena": 100},
{"id": 3, "naziv": "Tipkovnica", "cijena": 200},
{"id": 4, "naziv": "Monitor", "cijena": 1000},
{"id": 5, "naziv": "Slušalice", "cijena": 50}
]

def handler_function_2(request):
    return web.json_response(proizvodi)

async def post_handler(request):
    data = await request.json()
    print(data)
    return web.json_response(data)

app.router.add_get("/", handler_function)
app.router.add_post("/", post_handler)
app.router.add_get("/proizvodi", handler_function_2)
#app.router.add_get("/proizvodi/", {id})
web.run_app(app, host="localhost", port=8081)