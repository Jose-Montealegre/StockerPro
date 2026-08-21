from datetime import datetime, timedelta, timezone
from sqlalchemy.orm import Session

from app.models.product import Product
from app.models.movement import Movement


def get_recent_outputs(
    db: Session,
    product_id: int,
    days: int = 7
):
    fecha_limite = datetime.now(timezone.utc) - timedelta(days=days)
    
    movements = db.query(Movement).filter(
        Movement.product_id == product_id,
        Movement.tipo == "SALIDA",
        Movement.fecha.isnot(None),
        Movement.fecha >= fecha_limite
    ).all()
    
    return movements

def get_total_recent_outputs(
    db: Session,
    product_id: int,
    days: int = 7
):
    movements = get_recent_outputs(
        db,
        product_id,
        days
    )

    total = sum(
        movement.cantidad
        for movement in movements
    )

    return total


def classify_rotation(total_outputs: int):
    if total_outputs == 0:
        return "SIN_MOVIMIENTO"

    elif total_outputs <= 5:
        return "ROTACION_BAJA"

    elif total_outputs <= 15:
        return "ROTACION_MEDIA"

    else:
        return "ROTACION_ALTA"


def get_recommendations(db: Session):
    products = db.query(Product).all()

    recommendations = []

    for product in products:

        total_salidas = get_total_recent_outputs(
            db,
            product.id,
            days=7
        )

        rotacion = classify_rotation(total_salidas)

        if product.stock == 0:
            estado = "AGOTADO"
            recomendacion = (
                "Producto agotado. Se requiere reposición inmediata"
            )

        elif product.stock <= 5:
            estado = "STOCK_BAJO"
            recomendacion = (
                "Se recomienda reponer inventario"
            )

        else:
            continue

        recommendations.append(
            {
                "producto_id": product.id,
                "producto": product.nombre,
                "stock_actual": product.stock,
                "estado": estado,
                "salidas_ultimos_7_dias": total_salidas,
                "rotacion": rotacion,
                "recomendacion": recomendacion
            }
        )

    return recommendations