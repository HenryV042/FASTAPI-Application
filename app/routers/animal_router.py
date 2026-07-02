from fastapi import APIRouter, HTTPException
from app.model.animal_model import Animal
from app.repositories import animal_crud as aCrud

router = APIRouter(prefix="/animais", tags=["Animais"])

# Rota para Criar um Animal
@router.post("")
async def criar_animal(animal: Animal):
    try:
        return aCrud.criar_animal(animal)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Erro ao criar um Animal: {e}")
