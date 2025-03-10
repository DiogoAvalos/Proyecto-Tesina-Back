from pydantic import BaseModel

class TipoDocSchema(BaseModel):
    id: str
    cod_corto: str
    descripcion: str

    class Config:
        orm_mode = True