from pydantic import BaseModel

class TipoDocSchema(BaseModel):
    id: str
    cod_sunat: str | None
    cod_corto: str | None
    descripcion: str

    class Config:
        orm_mode = True