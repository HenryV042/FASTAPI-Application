from fastapi import APIRouter, HTTPException
from app.repositories import v_resumo_fazenda_crud as rCrud

router = APIRouter(prefix="/resumo", tags=["Resumo Geral da Fazenda"])

# Rota para listar todos os resumos das fazendas
@router.get("")
async def listar_resumo ():
    try:
         return rCrud.listar_resumo()
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Erro ao listar os resumos - {e}")

# Rota para buscar um resumo pelo id da fazenda
@router.get("/fazenda/{id}")
async def resumo_fazenda (id: int):
    resumo = rCrud.resumo_fazenda(id)
    
    if not resumo:
        raise HTTPException(status_code=404, detail="Resumo não encontrado")
        
    return resumo
