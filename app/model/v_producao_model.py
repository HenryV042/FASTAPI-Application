from pydantic import BaseModel, Field
from decimal import Decimal

class vProducaoLeiteAnimal(BaseModel):
    id_animal: int
    nome_animal: str
    especie: str
    raca: str
    total_ordenhas: int
    total_litros_produzidos: Decimal = Field(default=Decimal("0.00"))