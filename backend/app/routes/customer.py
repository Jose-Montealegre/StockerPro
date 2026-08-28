from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.customer import (
    CustomerCreate,
    CustomerUpdate,
    CustomerResponse
)
from app.services.customer_service import (
    create_customer,
    get_customers,
    get_customer_by_id,
    update_customer,
    delete_customer
)


router = APIRouter(
    prefix="/customers",
    tags=["Customers"]
)


@router.post(
    "",
    response_model=CustomerResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Crear cliente"
)
def create_customer_route(
    customer: CustomerCreate,
    db: Session = Depends(get_db)
):
    return create_customer(
        db,
        customer
    )


@router.get(
    "",
    response_model=list[CustomerResponse],
    summary="Listar clientes"
)
def get_customers_route(
    db: Session = Depends(get_db)
):
    return get_customers(db)


@router.get(
    "/{customer_id}",
    response_model=CustomerResponse,
    summary="Obtener cliente por ID"
)
def get_customer_by_id_route(
    customer_id: int,
    db: Session = Depends(get_db)
):
    return get_customer_by_id(
        db,
        customer_id
    )


@router.put(
    "/{customer_id}",
    response_model=CustomerResponse,
    summary="Actualizar Cliente"
)
def update_customer_route(
    customer_id: int,
    customer: CustomerUpdate,
    db: Session = Depends(get_db)
):
    return update_customer(
        db,
        customer_id,
        customer
    )


@router.delete(
    "/{customer_id}",
    summary="Eliminar cliente"
)
def delete_customer_route(
    customer_id: int,
    db: Session = Depends(get_db)
):
    return delete_customer(
        db,
        customer_id
    )