from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    descripcion = Column(String, nullable=False)
    precio = Column(Float, nullable=False)
    stock = Column(Integer, nullable=False)
    category_id = Column(
        Integer,
        ForeignKey("categories.id"),
        nullable=True
    )
    
    category = relationship(
        "Category",
        back_populates="products"
    )
    
    movements = relationship(
        "Movement",
        back_populates="product"
    )
    
   