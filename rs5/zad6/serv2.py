import time
from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/pozdrav")
async def pozdrav():
    time.sleep(4)  # Simulacija kašnjenja od 4 sekunde
    return JSONResponse(content={"message": "Pozdrav nakon 4 sekunde"})
