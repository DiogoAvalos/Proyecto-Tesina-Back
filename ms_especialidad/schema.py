from pydantic import BaseModel, Field

class Especialidad(BaseModel):
    id: int = Field(primary_key=True)
    descripcion: str = Field(None)
    activo: bool = Field(True)

class EspecialidadOut(Especialidad):
    class Config:
        orm_mode = True
