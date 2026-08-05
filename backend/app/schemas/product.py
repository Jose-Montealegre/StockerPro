from pydantic import BaseModel


class ProductCreate(BaseModel):
    nombre: str
    descripcion: str
    precio: float
    stock: int
    

class ProductResponse(BaseModel):
    id: int
    nombre: str
    descripcion: str
    precio: float
    stock: int
    
    