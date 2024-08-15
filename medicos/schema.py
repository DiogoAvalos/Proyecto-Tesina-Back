from pydantic import BaseModel
from datetime import date 

class MedicoSchema(BaseModel):
    id: int | None
    nombre: str | None
    apellido_p: str | None
    apellido_m: str | None
    tipodoc: int | None
    numdoc: str | None
    especialidad_id: int | None
    activo: bool | None
    
    class Config:
            orm_mode = True
