from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.category import Category
from app.schemas.category import CategoryCreate


def create_category(
    db: Session,
    category: CategoryCreate
):
    existing_category = db.query(Category).filter(
        Category.nombre == category.nombre
    ).first()

    if existing_category:
        raise HTTPException(
            status_code=400,
            detail="La categoría ya existe"
        )

    new_category = Category(
        nombre=category.nombre
    )

    try:
        db.add(new_category)
        db.commit()
        db.refresh(new_category)

        return new_category

    except Exception:
        db.rollback()
        raise


def get_categories(db: Session):
    return db.query(Category).all()