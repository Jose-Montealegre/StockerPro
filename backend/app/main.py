from fastapi import FastAPI
from app.routes.health import router as health_router
from app.routes.product import router as product_router
from app.routes.movement import router as movement_router
from app.config import settings
from app.database import Base, engine
from app.models.product import Product
from app.models.movement import Movement
from app.models.category import Category
from app.routes.recommendation import router as recommendation_router 
from app.routes.category import router as category_router
Base.metadata.create_all(bind=engine)




app = FastAPI(
    title=settings.APP_NAME,
    description=settings.APP_DESCRIPTION,
    version=settings.APP_VERSION
)

app.include_router(health_router)
app.include_router(product_router)
app.include_router(movement_router)
app.include_router(recommendation_router)
app.include_router(category_router)


@app.get("/")
def root():
    return {
        "mensaje": "Bienvenido a Stocker Pro"
    }