from aiohttp import web

#text="HEllo world!"

votes= {
    "plavi": 0,
    "crveni": 0,
}

async def hello(request):
    return web.Response(text="HEllo world!")

async def glasaj(request):
    #procitati sto je korisnik htio
    body = await request.read()
    text = body.decode()
    #1/0 - 500 Internal Server Error, 
    # Server got itself in trouble
    # 17, in glasaj
    #     1/0
    #     ~^~
    # ZeroDivisionError: division by zero
    # cesta greska 
    # if body in votes:
    if text in votes: 
        votes[text] += 1
        return web.json_response({"status":"zabiljezeno"})
    else:
        return web.json_response({"status":"nepoznato"})
    # print(body)
    # return web.Response(text="OK")
async def rezultati(request): 
    return web.json_response(votes)

app = web.Application()
app.add_routes([web.get('/', hello)])
app.add_routes([web.post('/glasaj', glasaj)])
app.add_routes([web.get('/rezultati', rezultati)])

web.run_app(app)