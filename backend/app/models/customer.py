from sqlalchemy import Column, Integer, String

from app.database import Base

class Customer(Base):
    __tablename__ = "customers"
    
    id = Column(Integer, primary_key=True, index=True)
    
    nombre = Column(
        String,
        nullable=False
    )
    
    documento = Column(
        String,
        unique=True,
        nullable=False
    )
    
    correo = Column(
        String,
        unique=True,
        nullable=False
    )
    
    telefono = Column(
        String,
        nullable=False
    )