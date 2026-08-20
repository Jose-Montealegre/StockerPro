from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
from app.database import Base


class Movement(Base):
    __tablename__ = "movements"

    id = Column(Integer, primary_key=True, index=True)

    product_id = Column(
        Integer,
        ForeignKey("products.id"),
        nullable=False
    )

    tipo = Column(
        String,
        nullable=False
    )

    cantidad = Column(
        Integer,
        nullable=False
    )
    
    stock_anterior = Column(
        Integer,
        nullable=False
    )

    stock_resultante = Column(
        Integer,
        nullable=False
    )
    
    fecha = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=True
    )
    
    product = relationship(
        "Product",
        back_populates="movements"
    )