from fastapi import APIRouter, HTTPException
from app.model.animal_model import Animal, AnimalUpdate
from app.repositories import animal_crud as aCrud

router = APIRouter(prefix="/animais", tags=["Animais"])

# Rota para listar todos os animais
@router.get("")
async def listar_animais ():
    try:
         return aCrud.listar_animais()
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Erro ao listar animais - {e}")

# Rota para buscar um animal pelo id
@router.get("/animal/{id}")
async def buscar_animal (id: int):
    animal = aCrud.buscar_animal(id)
    
    if not animal:
        raise HTTPException(status_code=404, detail="Animal não encontrado")
        
    return animal

# Rota para Criar um Animal
@router.post("")
async def criar_animal(animal: Animal):
    try:
        return aCrud.criar_animal(animal)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Erro ao criar um Animal - {e}")

# Rota para atualizar um animal do id
@router.patch("/animal/{id}")
async def atualizar_animal(id: int, animal: AnimalUpdate):
    try:
        return aCrud.atualizar_animal(id, animal)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Erro ao atualizar o Animal - {e}")

# Rota para deletar um animal a partir do id
@router.delete("/animal/{id}")
async def deletar_animal(id: int):
    try:
        return aCrud.deletar_animal(id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Erro ao deletar o Animal - {e}")