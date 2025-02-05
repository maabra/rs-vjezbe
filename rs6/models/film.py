from pydantic import BaseModel, Field #, validator
from typing import List, Optional

class Film(BaseModel):
    imdbID: str
    Title: str
    Year: str
    Rated: str
    Runtime: str
    Genre: str
    Language: str
    Country: str
    Actors: str
    Plot: str
    Writer: str
    Images: List[str] = Field(..., example=["https://example.com/image1.jpg"])
    type: str = Field("movie", pattern="^(movie|series)$")

    # @validator('Year')
    # def year_must_be_valid(cls, v):
    #     if v <= 1900:
    #         raise ValueError('Godina veca od 1900')
    #     return v

    # @validator('Runtime')
    # def runtime_must_be_valid(cls, v):
    #     if v <= 0:
    #         raise ValueError('Runtime veci od 0')
    #     return v


    # @validator('imdbRating')
    # def validate_imdb_rating(cls, v):
    #     if v is not None and (v < 0 or v > 10):
    #         raise ValueError('izmedu 0 i 10')
    #     return v

    # @validator('imdbVotes')
    # def validate_imdb_votes(cls, v):
    #     if v is not None and v <= 0:
    #         raise ValueError('veci od 0')
    #     return v
