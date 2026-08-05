from fastapi import APIRouter, status
from app.schemas.product import ProductCreate, ProductResponse
from app.services.product_service import (create_product, get_products, get_product_by_id)

router = APIRouter()

@router.post(
    "/products",
    status_code=status.HTTP_201_CREATED,
    summary="Crear un nuevo producto", 
    description="Permite registrar un nuevo producto en el sistema."
)
def create_product_route(product: ProductCreate):
    return create_product(product)


@router.get(
    "/products",
    summary="Listar todos los productos",
    description="Obtiene la lista de todos los productos registrados"
)
def get_products_route():
    return get_products()

@router.get(
    "/products/{id}",
    response_model=ProductResponse,
    summary="Obtener un producto por ID",
    description="Permite consultar un producto específico mediante su identificador."
)
def get_product_route(id: int):
    return get_product_by_id(id)