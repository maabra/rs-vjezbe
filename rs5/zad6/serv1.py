import time
from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/pozdrav")
async def pozdrav():
    time.sleep(3)  # Simulacija kašnjenja od 3 sekunde
    return JSONResponse(content={"message": "Pozdrav nakon 3 sekunde"})
