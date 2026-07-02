from pydantic import BaseModel, Field
from decimal import Decimal

class vResumoFazenda(BaseModel):
    id_fazenda: int
    nome_fazenda: str
    nome_produtor: str
    area_hectares: float
    total_animais: int
    total_investido: Decimal = Field(default=Decimal("0.00"))