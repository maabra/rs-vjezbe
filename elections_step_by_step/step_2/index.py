# elections/index.py

from aiohttp import web

# Rječnik za pohranjivanje glasova
votes = {
    "plavi": 0,
    "crveni": 0
}

# Funkcija za bilježenje glasova
async def glasaj(request):
    try:
        data = await request.json()
    except Exception:
        return web.json_response({"status": "nevažeći podaci"}, status=400)

    opcija = data.get("opcija")
    if opcija not in votes:
        return web.json_response({"status": "nepoznata opcija"}, status=400)

    votes[opcija] += 1
    return web.json_response({"status": "uspješno glasanje"}, status=200)

# Funkcija za prikaz trenutnih rezultata
async def trenutni_rezultati(request):
    return web.json_response(votes)

# Definiranje ruta
app = web.Application()
app.add_routes([web.post('/glasaj', glasaj)])
app.add_routes([web.get('/rezultati', trenutni_rezultati)])

if __name__ == '__main__':
    web.run_app(app, port=8080)
