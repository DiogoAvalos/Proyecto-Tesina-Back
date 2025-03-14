from pydantic import BaseModel
from datetime import date, datetime

class ORMBaseModel(BaseModel):
    class Config:
        orm_mode = True

class ProductoSchema(ORMBaseModel):
    nombre: str | None
    descripcion: str | None
    precio: float | None
    fecha_salida: date | None