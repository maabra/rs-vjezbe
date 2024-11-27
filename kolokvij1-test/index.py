from aiohttp import web
import asyncio
import json
from pydantic import BaseModel, ValidationError, constr # pip install
from typing import Dict, Literal, Optional, Union, List
import datetime as dt

#text="HEllo world!"

votes: Dict[Union[str, bool], int] = {
    "plavi": 0,
    "crveni": 0,
    False: 0,
}

# class Student(BaseModel):
#     ime: constr(min_length=1)
#     prezime: Optional(str) = None
#     datum_rodjenja: Optional(dt) = None
#     kolegiji: Optional(List(str(Literal("WA","PI","PROG","ELE")))) = None
#     smjer:Literal("TFPU","FIPU")


st = """
    {
        "ime": "Nikola",
        "datum_rodjenja": "1986-01-31"
    }
 """

print(type(st))

s = Student.model_validate_json(st)

print(s, type(s))

# class VotingRequest(BaseModel):
#     opcija: Union/Literal("plavi,"crveni")

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