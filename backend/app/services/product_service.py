from fastapi import HTTPException
from app.schemas.product import ProductCreate,ProductUpdate
from sqlalchemy.orm import Session
from app.models.product import Product
from app.models.category import Category


def create_product(db: Session, product: ProductCreate):
    if product.stock < 0:
        raise HTTPException(
            status_code=400,
            detail="El stock no puede ser negativo"
        )

    if product.category_id is not None:
        category = db.query(Category).filter(
            Category.id == product.category_id
        ).first()

        if not category:
            raise HTTPException(
                status_code=404,
                detail="Categoría no encontrada"
            )

    new_product = Product(
        nombre=product.nombre,
        descripcion=product.descripcion,
        precio=product.precio,
        stock=product.stock,
        category_id=product.category_id
    )

    try:
        db.add(new_product)
        db.commit()
        db.refresh(new_product)

        return new_product

    except Exception:
        db.rollback()
        raise

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
    if product.stock < 0:
        raise HTTPException(
            status_code=400,
            detail="El stock no puede ser negativo"
        )

    existing_product = db.query(Product).filter(
        Product.id == id
    ).first()

    if not existing_product:
        raise HTTPException(
            status_code=404,
            detail="Producto no encontrado"
        )

    if product.category_id is not None:
        category = db.query(Category).filter(
            Category.id == product.category_id
        ).first()

        if not category:
            raise HTTPException(
                status_code=404,
                detail="Categoría no encontrada"
            )

    try:
        existing_product.nombre = product.nombre
        existing_product.descripcion = product.descripcion
        existing_product.precio = product.precio
        existing_product.stock = product.stock
        existing_product.category_id = product.category_id

        db.commit()
        db.refresh(existing_product)

        return existing_product

    except Exception:
        db.rollback()
        raise


def delete_product(db: Session, id: int):
    product = db.query(Product).filter(Product.id == id).first()

    if not product:
        raise HTTPException(
            status_code=404,
            detail="Producto no encontrado"
        )

    db.delete(product)
    db.commit()
