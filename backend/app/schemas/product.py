from pydantic import BaseModel, ConfigDict


class ProductCreate(BaseModel):
    nombre: str
    descripcion: str
    precio: float
    stock: int
    
class ProductUpdate(BaseModel):
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
    
model_config = ConfigDict(from_attributes=True)