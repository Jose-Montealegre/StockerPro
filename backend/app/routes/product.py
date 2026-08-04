from fastapi import APIRouter, status
from app.schemas.product import Product
from app.services.product_service import create_product

router = APIRouter()

@router.post(
    "/products",
    status_code=status.HTTP_201_CREATED,
    summary="Crear un nuevo producto", 
    description="Permite registrar un nuevo producto en el sistema."
)
def create_product_route(product: Product):
    return create_product(product)