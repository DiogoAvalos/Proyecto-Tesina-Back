from pydantic import BaseModel
from datetime import date

class FamiliaSchema(BaseModel):
    id: int
    codigo_familia: str
    descripcion: str
    estado: bool | None
    creador: str | None
    creacion: date | None

    class Config:
        orm_mode = True