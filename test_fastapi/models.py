
from pydantic import BaseModel

class CreateProizvod(BaseModel):
    naziv: str
    cijena: float

class ResponseProizvod(CreateProizvod):
    id: int
    
#pydantic klase su read only

# class BaseProizvod(BaseModel):
#     naziv: str
#     cijena: float

# class CreateProizvod(BaseProizvod):
#     naziv: str
#     cijena: float
#     # moze i samo:
#     # pass

# class ResponseProizvod(BaseModel):
#     id: int
