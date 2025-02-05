import json
from pathlib import Path
from fastapi import APIRouter, HTTPException
from models.film import Film
from typing import List, Optional
#import json

router = APIRouter()

DATA_PATH = Path("rs6") / "Film.JSON"

if DATA_PATH.exists():
    with open(DATA_PATH, "r", encoding="utf-8") as file:
        films_data = json.load(file)

films = [Film(**film) for film in films_data]

@router.get("/films", response_model=List[Film])
def get_films():
    return films

@router.get("/films/{imdbID}", response_model=Film)
def get_film_by_id(imdbID: str):
    for film in films:
        print("test")
        if film.imdbID == imdbID:
            return film
    raise HTTPException(status_code=404, detail="Filma nema")

@router.get("/films/title/{title}", response_model=List[Film])
def get_film_by_title(title: str):
    result = [film for film in films if film.Title.lower() == title.lower()]
    if not result:
        raise HTTPException(status_code=404, detail="Filma nema")
    return result
