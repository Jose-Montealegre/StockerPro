from fastapi import HTTPException
from app.schemas.product import ProductCreate,ProductUpdate
from sqlalchemy.orm import Session
from app.models.product import Product


def create_product(db: Session, product: ProductCreate):
    if product.precio < 1000:
        raise HTTPException(
            status_code=400,
            detail="El precio debe ser mayor o igual a 1000"
        )
    
    new_product = Product(
        nombre=product.nombre,
        descripcion=product.descripcion,
        precio=product.precio,
        stock=product.stock
    )
    
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
        
    return new_product

def get_products(db: Session):
    return db.query(Product).all()
    

def get_product_by_id(db: Session, id: int):
    product = db.query(Product).filter(Product.id == id).first()

    if not product:
        raise HTTPException(
            status_code=404,
            detail="Producto no encontrado"
        )

    return product


def update_product(db: Session, id: int, product: ProductUpdate):
    existing_product = db.query(Product).filter(Product.id == id).first()

    if not existing_product:
        raise HTTPException(
            status_code=404,
            detail="Producto no encontrado"
        )

    existing_product.nombre = product.nombre
    existing_product.descripcion = product.descripcion
    existing_product.precio = product.precio
    existing_product.stock = product.stock

    db.commit()
    db.refresh(existing_product)

    return existing_product


def delete_product(db: Session, id: int):
    product = db.query(Product).filter(Product.id == id).first()

    if not product:
        raise HTTPException(
            status_code=404,
            detail="Producto no encontrado"
        )

    db.delete(product)
    db.commit()
