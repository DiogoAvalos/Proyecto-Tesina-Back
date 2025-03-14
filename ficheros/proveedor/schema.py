from pydantic import BaseModel
from datetime import date

class MarcaSchema(BaseModel):
    id: str | None
    nombre_prov: str
    ruc: str
    direccion: str
    contacto: str | None
    telefono: str | None
    estado: str | None
    creador: str | None
    creacion: str | None

    class Config:
        orm_mode = True