from fastapi import APIRouter
from app.schemas.product import Product
from app.services.product_service import create_product

router = APIRouter()
@router.post("/products")
def create_product_route(product: Product):
    result = create_product(product)
    
    return {
        "mensaje": "producto recibido correctamente",
        "producto": result
    }
    