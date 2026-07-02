from fastapi import APIRouter, HTTPException
from app.model.v_producao_model import vProducaoLeiteAnimal
from app.repositories import v_producao_crud as pCrud

router = APIRouter(prefix="/producao", tags=["Producao Geral dos Animais"])

# Rota para listar todas os 
@router.get("")
async def listar_producao ():
    try:
         return pCrud.listar_produção()
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Erro ao listar a produção - {e}")

# Rota para buscar um animal pelo id
@router.get("/animal/{id}")
async def resumo_producao (id: int):
    animal = pCrud.resumo_producao(id)
    
    if not animal:
        raise HTTPException(status_code=404, detail="Animal não encontrado")
        
    return animal
