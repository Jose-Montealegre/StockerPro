from fastapi import FastAPI
from app.routes.health import router as health_router
from app.routes.product import router as product_router
from app.config import settings

app = FastAPI(
    title=settings.APP_NAME,
    description=settings.APP_DESCRIPTION,
    version=settings.APP_VERSION
)

app.include_router(health_router)
app.include_router(product_router)

@app.get("/")
def root():
    return {
        "mensaje": "Bienvenido a Stocker Pro"
    }