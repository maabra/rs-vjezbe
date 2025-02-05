from fastapi import FastAPI
from routers.filmovi import router


app = FastAPI()


@app.get("/", tags=["Root"])
def read_root():
    return {"message": "test"}

# Uključivanje ruta
app.include_router(router)
