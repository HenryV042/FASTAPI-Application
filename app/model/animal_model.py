from pydantic import BaseModel
from typing import Optional
from datetime import date

class Animal (BaseModel):
    id_animal: int
    id_fazenda: int
    id_raca: int
    nome: str
    sexo: str
    data_nasc: Optional[str] = None
    peso: Optional[float] = None
    status_saude: Optional[str] = None
    fase_vida: Optional[str] = None

class AnimalUpdate (BaseModel):
    nome: Optional[str] = None
    sexo: Optional[str] = None
    data_nasc: Optional[str] = None
    peso: Optional[float] = None
    status_saude: Optional[str] = None
    fase_vida: Optional[str] = None