from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.movement import Movement
from app.models.product import Product
from app.schemas.movement import MovementCreate


def create_movement(db: Session, movement: MovementCreate):
    product = db.query(Product).filter(
        Product.id == movement.product_id
    ).first()

    if not product:
        raise HTTPException(
            status_code=404,
            detail="Producto no encontrado"
        )

    if movement.tipo == "ENTRADA":
        product.stock += movement.cantidad

    elif movement.tipo == "SALIDA":
        if movement.cantidad > product.stock:
            raise HTTPException(
                status_code=400,
                detail="Stock insuficiente"
            )

        product.stock -= movement.cantidad

    new_movement = Movement(
        product_id=movement.product_id,
        tipo=movement.tipo,
        cantidad=movement.cantidad
    )

    try:
        db.add(new_movement)
        db.commit()
        db.refresh(new_movement)

        return new_movement

    except Exception:
        db.rollback()
        raise

def get_movements(db: Session):
    return db.query(Movement).all()

def get_movement_by_id(db: Session, id: int):
    movement = db.query(Movement).filter(
        Movement.id == id
    ).first()

    if not movement:
        raise HTTPException(
            status_code=404,
            detail="Movimiento no encontrado"
        )

    return movement