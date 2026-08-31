from fastapi import HTTPException
from sqlalchemy.orm import Session
from datetime import datetime, timezone

from app.models.customer import Customer
from app.models.product import Product
from app.models.sale import Sale
from app.models.sale_detail import SaleDetail
from app.models.movement import Movement
from app.schemas.sale import SaleCreate


def create_sale(
    db: Session,
    sale_data: SaleCreate
):
    
    customer = db.query(Customer).filter(
        Customer.id == sale_data.customer_id
    ).first()

    if not customer:
        raise HTTPException(
            status_code=404,
            detail="Cliente no encontrado"
        )

    if not sale_data.items:
        raise HTTPException(
            status_code=400,
            detail="La venta debe incluir al menos un producto"
        )

    new_sale = Sale(
        customer_id=sale_data.customer_id,
        total=0
    )

    try:
        db.add(new_sale)
        db.flush()

        total_sale = 0

        for item in sale_data.items:

            product = db.query(Product).filter(
                Product.id == item.product_id
            ).first()

            if not product:
                raise HTTPException(
                    status_code=404,
                    detail=f"Producto con ID {item.product_id} no encontrado"
                )

            if product.stock < item.cantidad:
                raise HTTPException(
                    status_code=400,
                    detail=(
                        f"Stock insuficiente para {product.nombre}. "
                        f"Disponible: {product.stock}"
                    )
                )

            precio_unitario = product.precio

            subtotal = (
                precio_unitario
                * item.cantidad
            )

            detail = SaleDetail(
                sale_id=new_sale.id,
                product_id=product.id,
                cantidad=item.cantidad,
                precio_unitario=precio_unitario,
                subtotal=subtotal
            )

            db.add(detail)
            
            stock_anterior = product.stock
            
            product.stock -= item.cantidad
            
            stock_resultante = product.stock
            
            movement =  Movement(
                product_id=product.id,
                tipo="SALIDA",
                cantidad=item.cantidad,
                stock_anterior=stock_anterior,
                stock_resultante=stock_resultante,
                fecha=datetime.now(timezone.utc)
            )

            db.add(movement)

            total_sale += subtotal

        new_sale.total = total_sale

        db.commit()
        db.refresh(new_sale)

        return new_sale

    except Exception:
        db.rollback()
        raise
    
    
def get_sales(db: Session):
    return db.query(Sale).all()


def get_sale_by_id(
    db: Session,
    sale_id: int
):
    sale = db.query(Sale).filter(
        Sale.id == sale_id
    ).first()

    if not sale:
        raise HTTPException(
            status_code=404,
            detail="Venta no encontrada"
        )

    return sale