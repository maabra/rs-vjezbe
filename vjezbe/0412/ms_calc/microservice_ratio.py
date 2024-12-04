import aiohttp
import asyncio
from aiohttp import web
# koji endpoint moramo definirati?
app = web.Application()

async def ratio_handler(request):
  podaci = await request.json()
  brojevi = podaci.get("brojevi")
  zbroj = podaci.get("zbroj")
  ratio_list = [round(broj/zbroj, 2) for broj in brojevi]

  return web.json_response({"ratio": ratio_list})

app.router.add_post("/ratio", ratio_handler)

web.run_app(app, host='localhost', port=8082)
