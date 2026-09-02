from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.health import router as health_router
from app.routes.product import router as product_router
from app.routes.movement import router as movement_router
from app.config import settings
from app.database import Base, engine
from app.models.product import Product
from app.models.movement import Movement
from app.models.category import Category
from app.models.customer import Customer
from app.models.sale import Sale
from app.models.sale_detail import SaleDetail
from app.routes.recommendation import router as recommendation_router 
from app.routes.category import router as category_router
from app.routes.dashboard import router as dashboard_router
from app.routes.customer import router as customer_router
from app.routes.sale import router as sale_router
from app.routes.report import router as report_router

Base.metadata.create_all(bind=engine)




app = FastAPI(
    title=settings.APP_NAME,
    description=settings.APP_DESCRIPTION,
    version=settings.APP_VERSION
)


origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health_router)
app.include_router(product_router)
app.include_router(movement_router)
app.include_router(recommendation_router)
app.include_router(category_router)
app.include_router(dashboard_router)
app.include_router(customer_router)
app.include_router(sale_router)
app.include_router(report_router)

@app.get("/")
def root():
    return {
        "mensaje": "Bienvenido a Stocker Pro"
    }