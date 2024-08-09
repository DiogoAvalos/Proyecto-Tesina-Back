from pydantic import BaseModel

class TipoDocSchema(BaseModel):
    id: str
    descripcion: str

    class Config:
        orm_mode = True