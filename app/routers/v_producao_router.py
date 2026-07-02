from fastapi import APIRouter, HTTPException
from app.model.v_producao_model import vProducaoLeiteAnimal
from app.repositories import v_producao_crud as pCrud

router = APIRouter(prefix="/resumo", tags=["Resumo Geral da Fazenda"])

# Rota para listar todas os 
@router.get("")
async def listar_producao ():
    try:
         return pCrud.listar_producao()
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Erro ao listar animais - {e}")

# Rota para buscar um animal pelo id
@router.get("/fazenda/{id}")
async def buscar_animal (id: int):
    animal = aCrud.buscar_animal(id)
    
    if not animal:
        raise HTTPException(status_code=404, detail="Animal não encontrado")
        
    return animal
