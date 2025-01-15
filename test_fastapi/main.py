from fastapi import FastAPI
from models import CreateProizvod, ResponseProizvod

app = FastAPI()

proizvodi = [
    {"id": 1, "naziv": "Miš", "cijena": 50},
    {"id": 2, "naziv": "Tipkovnica", "cijena": 100},
    {"id": 3, "naziv": "Laptop", "cijena": 1000}
]

#route parametar definiramo i u dekoratoru i u funkciji
#query parametar (?) - ne definiramo u dekoratur ali da u funkciji i koristimo primitiv
#body parametar - ne pisemo tj definiramo u dekoratoru ali definiramo u funkciji kao dict ili pydantic 
@app.get("/proizvodi/{proizvod_id}") #route
def get_proizvodi(proizvod_id):
    print("tip podataka:", type(proizvod_id))
    trazeni_proizvod = next((proizvod for proizvod in proizvodi if proizvod["id"] == proizvod_id ), None)
    return {"trazeni_proizvod": trazeni_proizvod}

@app.get("/proizvodi_cijena/{proizvod_id}") #route
def get_proizvodi(proizvod_id: int, min_cijena: float):
    print("tip podataka:", type(proizvod_id))
    trazeni_proizvod = next((proizvod for proizvod in proizvodi if proizvod["id"] == proizvod_id and proizvod["cijena"] >= min_cijena), None)
    return {"trazeni_proizvod": trazeni_proizvod}

@app.post("/proizvodi") 
def dodaj_proizvod(proizvod: CreateProizvod): # http body jer nema u nazivu rute "{nesto}" 
    print("proizvod", proizvod) 
    new_id = len(proizvodi) + 1 
    proizvod_sa_id = ResponseProizvod(id=new_id, **proizvod.model_dump()) 
    proizvodi.append(proizvod_sa_id.model_dump()) 
    return {"status": "OK", "proizvod": proizvod_sa_id}

# def novu fastapi rutu get /filmovi klijentu vraca listu filmova definiranu u slje ruti 
#     new_id = len(proizvodi) + 1
#     proizvod[id] = new_id
#     proizvodi.append(proizvod)
    
#     print("proizvod_sa_id:", proizvod)
#     return {"status": "OK"}