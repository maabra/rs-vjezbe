
from fastapi import FastAPI
import hashlib

app = FastAPI()

@app.get("/")
def hello_world():
    for _ in range (500_000):
        hashlib.sha256("Poruka".encode("utf-8")).hexdigest()

    return {"message": "Hello, World!"}


