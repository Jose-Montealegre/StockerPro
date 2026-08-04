from fastapi import HTTPException
from app.schemas.product import Product



def create_product(product: Product):
    if product.precio < 1000:
        raise HTTPException(
            status_code=400,
            detail="El precio debe ser mayor o igual a 1000"
        )
        
    return product