from fastapi import APIRouter
from app.schemas.product import Product

router = APIRouter()
@router.post("/products")
def create_product(product: Product):
    return {
        "mensaje": "Producto recibido correctamente",
        "producto": product
    }