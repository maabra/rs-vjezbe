from pydantic import BaseModel, Field, validator
from typing import List, Optional

class Actor(BaseModel):
    name: str
    surname: str

class Writer(BaseModel):
    name: str
    surname: str

class Movie(BaseModel):
    imdbID: str
    Title: str
    Year: int = Field(..., gt=1899)
    Rated: str
    Runtime: int = Field(..., gt=0)
    Genre: str
    Language: str
    Country: str
    Actors: List[Actor]
    Plot: str
    Writer: List[Writer]
    Images: Optional[List[str]] = []
    type: str
    imdbRating: float = Field(..., ge=0, le=10)
    imdbVotes: int = Field(..., gt=0)

    @validator("type")
    def validate_type(cls, value):
        if value not in ["movie", "series"]:
            raise ValueError("Type must be 'movie' or 'series'")
        return value
