from pydantic import BaseModel, ConfigDict, Field


class CategoryProductResponse(BaseModel):
    id: int
    nombre: str

    model_config = ConfigDict(from_attributes=True)


class ProductCreate(BaseModel):
    nombre: str
    descripcion: str
    precio: float
    stock: int
    category_id: int | None = None


class ProductUpdate(BaseModel):
    nombre: str
    descripcion: str
    precio: float
    stock: int
    category_id: int | None = None


class ProductResponse(BaseModel):
    id: int
    nombre: str
    descripcion: str
    precio: float
    stock: int

    categoria: CategoryProductResponse | None = Field(
        default=None,
        validation_alias="category"
    )

    model_config = ConfigDict(from_attributes=True)