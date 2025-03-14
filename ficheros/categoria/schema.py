from pydantic import BaseModel
from datetime import date

class CategoriaSchema(BaseModel):
    id: int
    descripcion: str
    estado: bool | None
    creador: str | None
    creacion: date | None

    class Config:
        orm_mode = True
