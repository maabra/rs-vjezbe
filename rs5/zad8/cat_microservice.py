import asyncio
import aiohttp
from aiohttp import web

async def fetch_cat_fact(session):
    async with session.get('https://catfact.ninja/fact') as response:
        data = await response.json()
        return data['fact']

async def get_cats(request):
    amount = int(request.rel_url.query.get('amount', 1))
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_cat_fact(session) for _ in range(amount)]
        facts = await asyncio.gather(*tasks)
    return web.json_response(facts)

app = web.Application()
app.router.add_get('/cats', get_cats)

if __name__ == '__main__':
    web.run_app(app, port=8086)
