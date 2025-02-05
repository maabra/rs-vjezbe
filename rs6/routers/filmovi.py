from fastapi import APIRouter, HTTPException, Query
import json
from pathlib import Path
from models.vrste import Movie
from typing import List, Optional

router = APIRouter()

MOVIES_FILE = Path("Film.JSON").resolve() 

try:
    with open(MOVIES_FILE, "r", encoding="utf-8") as f:
        movies_data = json.load(f)
except FileNotFoundError:
    print(f"[ERROR] JSON datoteka nije pronađena na lokaciji: {MOVIES_FILE}, ali nastavljamo bez nje.")
    movies_data = []

@router.get("/movies", response_model=List[Movie])
def get_movies(
    min_year: Optional[int] = Query(None, gt=1900),
    max_year: Optional[int] = Query(None, lt=2100),
    min_rating: Optional[float] = Query(None, ge=0, le=10),
    max_rating: Optional[float] = Query(None, ge=0, le=10),
    type: Optional[str] = Query(None)
):
    filtered_movies = [
        movie for movie in movies_data
        if (not min_year or movie["Year"] >= min_year)
        and (not max_year or movie["Year"] <= max_year)
        and (not min_rating or movie["imdbRating"] >= min_rating)
        and (not max_rating or movie["imdbRating"] <= max_rating)
        and (not type or movie["type"] == type)
    ]
    return filtered_movies

@router.get("/movies/{imdbID}", response_model=Movie)
def get_movie(imdbID: str):
    movie = next((m for m in movies_data if m["imdbID"] == imdbID), None)
    if movie is None:
        raise HTTPException(status_code=404, detail="Movie not found")
    return movie

@router.get("/movies/title/{title}", response_model=Movie)
def get_movie_by_title(title: str):
    movie = next((m for m in movies_data if m["Title"].lower() == title.lower()), None)
    if movie is None:
        raise HTTPException(status_code=404, detail="Movie not found")
    return movie
