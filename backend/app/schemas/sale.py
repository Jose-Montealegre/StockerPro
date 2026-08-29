from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class SaleItemCreate(BaseModel):
    product_id: int
    cantidad: int = Field(gt=0)


class SaleCreate(BaseModel):
    customer_id: int
    items: list[SaleItemCreate]


class SaleProductResponse(BaseModel):
    id: int
    nombre: str

    model_config = ConfigDict(from_attributes=True)


class SaleDetailResponse(BaseModel):
    id: int
    cantidad: int
    precio_unitario: float
    subtotal: float

    producto: SaleProductResponse = Field(
        validation_alias="product"
    )

    model_config = ConfigDict(from_attributes=True)


class SaleCustomerResponse(BaseModel):
    id: int
    nombre: str
    documento: str

    model_config = ConfigDict(from_attributes=True)


class SaleResponse(BaseModel):
    id: int
    total: float
    fecha: datetime

    cliente: SaleCustomerResponse = Field(
        validation_alias="customer"
    )

    detalles: list[SaleDetailResponse] = Field(
        validation_alias="details"
    )

    model_config = ConfigDict(from_attributes=True)