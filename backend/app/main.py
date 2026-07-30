from fastapi import FastAPI
from app.routes.health import router as health_router

app = FastAPI(
    title="Stocker Pro API",
    description="Sistema de gestion de inventarios",
    version="1.0.0"
)

app.include_router(health_router)

@app.get("/")
def root():
    return {
        "mensaje": "Bienvenido a Stocker Pro"
    }