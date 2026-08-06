from fastapi import HTTPException
from app.schemas.product import (ProductCreate,ProductUpdate, ProductResponse)


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


def update_product(id: int, product: ProductUpdate):
    for existing_product in products:
        if existing_product.id == id:
            
            existing_product.nombre = product.nombre
            existing_product.descripcion = product.descripcion
            existing_product.precio = product.precio
            existing_product.stock = product.stock
            
            return existing_product
        
    raise HTTPException(
        status_code=404,
        detail="Producto no encontrado"
    )


def delete_product(id: int):
    for product in products:
        if product.id == id:
            products.remove(product)
            return

    raise HTTPException(
        status_code=404,
        detail="Producto no encontrado"
    )
