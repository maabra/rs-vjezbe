from pydantic import BaseModel
from fastapi import FastAPI
import asyncio
from uuid import uuid4 as uuid
app = FastAPI()

sessions = ()

class LoginRequest(BaseModel):
    username: str
    password: str
    name: str

@app.get("/login")
async def root(login: LoginRequest):
    _id = str(uuid()) #generiranje jedinstvenog ID-a
    if login.username == "ntankovic": # ne radi se, ide u bazu podataka
        sessions(_id) = login # ne zbog spremanja passworda
    print (login) 
    return {"status":"ok"}

"""
JSON
{
    "username": "ntankovic"
    "password": "not"
    "name": "Nikola"
}
"""

@app.get("/api")
def api(session_id: str): 
    user = sessions.get(session_id, ())
    return user