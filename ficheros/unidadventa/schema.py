from pydantic import BaseModel
from datetime import date

class UnidadVentaSchema(BaseModel):
    id: int
    descripcion: str
    creador: str | None
    creacion: date | None

    class Config:
        orm_mode = True