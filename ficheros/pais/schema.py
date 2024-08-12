from pydantic import BaseModel

class PaisSchema(BaseModel):
    id: int
    nombre: str

    class Config:
        orm_mode = True