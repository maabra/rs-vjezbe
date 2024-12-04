import aiohttp
import asyncio
from aiohttp import web
# koji endpoint moramo definirati?
app = web.Application()

async def sum_handler(request):
  podaci = await request.json()
  zbroj = sum(podaci)
  brojevi = podaci.get("brojevi")
  print("Brojevi:", brojevi)
  print(type(brojevi))
  return web.json_response({"zbroj": zbroj})

app.router.add_post("/zbroj", sum_handler)

web.run_app(app, host='localhost', port=8081)

# input json s listom brojeva npr. [1,2,3,4,5]
# output json s kljucem zbroj [x]
