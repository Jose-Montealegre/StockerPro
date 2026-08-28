from pydantic import BaseModel, ConfigDict

class CustomerCreate(BaseModel):
    nombre: str 
    documento: str
    correo: str
    telefono: str
    

class CustomerUpdate(BaseModel):
    nombre: str 
    documento: str
    correo: str
    telefono: str


class CustomerResponse(BaseModel):
    id: int
    nombre: str 
    documento: str
    correo: str
    telefono: str
    
    model_config = ConfigDict(from_attributes=True)