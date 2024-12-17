from aiohttp import web
import json

async def check_facts(request):
    try:
        data = await request.json()
    except json.JSONDecodeError:
        return web.json_response({'error': 'Invalid JSON'}, status=400)

    if 'facts' not in data:
        return web.json_response({'error': 'No facts provided'}, status=400)

    filtered_facts = [fact for fact in data['facts'] if 'cat' in fact.lower() or 'cats' in fact.lower()]
    return web.json_response({'filtered_facts': filtered_facts})

app = web.Application()
app.router.add_post('/facts', check_facts)

if __name__ == '__main__':
    web.run_app(app, port=8087)
