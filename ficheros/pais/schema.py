from pydantic import BaseModel

class PaisSchema(BaseModel):
    id: int
    iso: str
    nombre: str

    class Config:
        orm_mode = True