from sqlalchemy.orm import Session

from app.models.product import Product
from app.models.category import Category


def get_dashboard_summary(db: Session):
    
    products = db.query(Product).all()
    categories = db.query(Category).all()
    
    total_productos = len(products)
    
    total_unidades = sum(
        product.stock
        for product in products
    )
    
    productos_stock_bajo = sum(
        1
        for product in products
        if 0 < product.stock <= 5
    )
    
    productos_agotados = sum(
        1
        for product in products 
        if product.stock == 0
    )
    
    total_categorias =  len(categories)
    
    return{
        "total_productos": total_productos,
        "total_unidades": total_unidades,
        "productos_stock_bajo": productos_stock_bajo,
        "productos_agotados": productos_agotados,
        "total_categorias": total_categorias
    }