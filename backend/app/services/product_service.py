from fastapi import HTTPException
from app.schemas.product import ProductCreate, ProductResponse


products =[]
next_id = 1

def create_product(product: ProductCreate):
    global next_id
    
    if product.precio < 1000:
        raise HTTPException(
            status_code=400,
            detail="El precio debe ser mayor o igual a 1000"
        )
    
    new_product = ProductResponse(
        id=next_id,
        nombre=product.nombre,
        descripcion=product.descripcion,
        precio=product.precio,
        stock=product.stock
    )
    
    
    next_id += 1
        
    products.append(new_product)
        
    return new_product

def get_products():
    return products
    

def get_product_by_id(id: int):
    for product in products:
        if product.id == id:
            return product

    raise HTTPException(
        status_code=404,
        detail="Producto no encontrado"
    )
