from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.category import CategoryCreate, CategoryResponse
from app.services.category_service import (
    create_category,
    get_categories
)


router = APIRouter()


@router.post(
    "/categories",
    response_model=CategoryResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Crear una categoría",
    description="Permite registrar una nueva categoría de productos."
)
def create_category_route(
    category: CategoryCreate,
    db: Session = Depends(get_db)
):
    return create_category(db, category)


@router.get(
    "/categories",
    response_model=list[CategoryResponse],
    summary="Listar categorías",
    description="Obtiene todas las categorías registradas."
)
def get_categories_route(
    db: Session = Depends(get_db)
):
    return get_categories(db)