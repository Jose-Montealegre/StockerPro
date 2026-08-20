from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session

from app.schemas.movement import MovementCreate, MovementResponse
from app.services.movement_service import (
    create_movement,
    get_movements,
    get_movement_by_id
)
from app.database import get_db


router = APIRouter()


@router.post(
    "/movements",
    response_model=MovementResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Registrar un movimiento de inventario",
    description="Permite registrar una entrada o salida de productos."
)
def create_movement_route(
    movement: MovementCreate,
    db: Session = Depends(get_db)
):
    return create_movement(db, movement)


@router.get(
    "/movements",
    response_model=list[MovementResponse],
    summary="Listar movimientos de inventario",
    description="Obtiene el historial de movimientos registrados."
)
def get_movements_route(
    db: Session = Depends(get_db)
):
    return get_movements(db)


@router.get(
    "/movements/{id}",
    response_model=MovementResponse,
    summary="Obtener un movimiento por ID",
    description="Permite consultar un movimiento específico mediante su identificador."
)
def get_movement_route(
    id: int,
    db: Session = Depends(get_db)
):
    return get_movement_by_id(db, id)