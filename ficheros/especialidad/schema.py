from pydantic import BaseModel

class EspecialidadSchema(BaseModel):
    id: str
    descripcion: str
    estado: bool

    class Config:
        orm_mode = True