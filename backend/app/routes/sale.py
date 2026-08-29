from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.sale import SaleCreate, SaleResponse
from app.services.sale_service import create_sale, get_sales, get_sale_by_id                                


router = APIRouter(
    prefix="/sales",
    tags=["Ventas"]
)


@router.post(
    "",
    response_model=SaleResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Registrar venta"
)
def create_sale_route(
    sale: SaleCreate,
    db: Session = Depends(get_db)
):
    return create_sale(
        db,
        sale
    )


@router.get(
    "",
    response_model=list[SaleResponse],
    summary="Listar ventas"
)
def get_sales_route(
    db: Session = Depends(get_db)
):
    return get_sales(db)


@router.get(
    "/{sale_id}",
    response_model=SaleResponse,
    summary="Obtener venta por ID"
)
def get_sale_by_id_route(
    sale_id: int,
    db: Session = Depends(get_db)
):
    return get_sale_by_id(
        db,
        sale_id
    )