from aiohttp import web
import math

async def calculate_euclidean_distance(request):
    try:
        data = await request.json()
        coordinates = data['coordinates']
        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]
        distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        response_data = {'distance': round(distance, 2)}
        return web.json_response(response_data)
    except Exception as e:
        return web.json_response({'error': str(e)}, status=400)

app = web.Application()
app.add_routes([web.post('/euclidean', calculate_euclidean_distance)])

if __name__ == '__main__':
    web.run_app(app, port=8091)
