from fastapi import FastAPI
from routers.filmovi import router as filmovi_router

app = FastAPI()

try:
    app.include_router(filmovi_router)
except ImportError:
    print("[WARNING] Problem - učitavanje ruta, aplikacija dalje radi.")

