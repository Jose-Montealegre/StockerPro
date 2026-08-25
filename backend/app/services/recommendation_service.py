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
    

def calculate_restock_quantity(
    stock_actual: int,
    total_outputs: int
):
    stock_objetivo = total_outputs * 2
    
    cantidad_reponer = stock_objetivo - stock_actual
    
    if cantidad_reponer < 0:
        return 0 
    
    return cantidad_reponer

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
        
        cantidad_sugerida = calculate_restock_quantity(
        product.stock,
        total_salidas
    )

        if product.stock == 0:
            estado = "AGOTADO"
            recomendacion = (
                f"Producto agotado. Se recomienda reponer"
                f"{cantidad_sugerida} unidades"
            )

        elif product.stock <= 5:
            estado = "STOCK_BAJO"
            recomendacion = (
                f"Stock bajo. Se recomienda reponer "
                f"{cantidad_sugerida} unidades"
            )

        elif rotacion == "ROTACION_ALTA":
            estado = "ROTACION_ALTA"
            recomendacion = (
                f"Producto con alta rotación. Se recomienda reponer "
                f"aproximadamente {cantidad_sugerida} unidades"
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
                "cantidad_sugerida_reposicion": cantidad_sugerida,
                "recomendacion": recomendacion
            }
        )

    return recommendations