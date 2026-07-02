from fastapi import FastAPI
from app.routers.animal_router import router as animal_router

app = FastAPI(
    title="API - Gestão Agropecuária",
    description="Aplicação Final da Entrega 4: CRUD + consulta às views do banco.",
    version="1.0.0",
)

app.include_router(animal_router)

@app.get("/", tags=["Status"])
def raiz():
    return {"mensagem": "API da Entrega 4 - Gestão Agropecuária no ar."}
