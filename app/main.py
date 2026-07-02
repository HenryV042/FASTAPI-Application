from fastapi import FastAPI
from app.routers.animal_router import router as animal_router
from app.routers.v_resumo_router import router as resumo_router

app = FastAPI(
    title="API - Gestão Agropecuária",
    description="Aplicação Final da Entrega 4: CRUD + consulta às views do banco.",
    version="1.0.0",
)

# Adiciona as rotas de animal
app.include_router(animal_router)
# Adiciona as rotas de v_resumo_fazendas
app.include_router(resumo_router)

@app.get("/", tags=["Status"])
def raiz():
    return {"msg": "API da Entrega 4 - Gestão Agropecuária no ar."}
