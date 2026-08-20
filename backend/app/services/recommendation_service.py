from sqlalchemy.orm import Session

from app.models.product import Product


def get_recommendations(db: Session):
    products = db.query(Product).all()

    recommendations = []

    for product in products:

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
                "recomendacion": recomendacion
            }
        )

    return recommendations