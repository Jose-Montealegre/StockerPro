from sqlalchemy import func
from sqlalchemy.orm import Session

from app.models.sale import Sale
from app.models.sale_detail import SaleDetail
from app.models.product import Product


def get_sales_report(db: Session):

    total_vendido = db.query(
        func.coalesce(func.sum(Sale.total), 0)
    ).scalar()

    numero_ventas = db.query(
        func.count(Sale.id)
    ).scalar()

    unidades_vendidas = db.query(
        func.coalesce(func.sum(SaleDetail.cantidad), 0)
    ).scalar()

    producto_mas_vendido = (
        db.query(
            Product.id,
            Product.nombre,
            func.sum(SaleDetail.cantidad).label("unidades_vendidas")
        )
        .join(
            SaleDetail,
            SaleDetail.product_id == Product.id
        )
        .group_by(
            Product.id,
            Product.nombre
        )
        .order_by(
            func.sum(SaleDetail.cantidad).desc()
        )
        .first()
    )

    top_product = None

    if producto_mas_vendido:
        top_product = {
            "id": producto_mas_vendido.id,
            "nombre": producto_mas_vendido.nombre,
            "unidades_vendidas": producto_mas_vendido.unidades_vendidas
        }
        
    ventas_recientes = (
        db.query(Sale)
        .order_by(Sale.fecha.desc())
        .limit(5)
        .all()
    )

    return {
        "total_vendido": total_vendido,
        "numero_ventas": numero_ventas,
        "unidades_vendidas": unidades_vendidas,
        "producto_mas_vendido": top_product,
        "ventas_recientes": ventas_recientes
    }