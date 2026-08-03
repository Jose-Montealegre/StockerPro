from pydantic import BaseModel


class Product(BaseModel):
    nombre: str
    descripcion: str
    precio: float
    stock: int
    