from pydantic import BaseModel, ConfigDict


class CategoryCreate(BaseModel):
    nombre: str


class CategoryResponse(BaseModel):
    id: int
    nombre: str

    model_config = ConfigDict(from_attributes=True)