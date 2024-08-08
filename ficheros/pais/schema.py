from pydantic import BaseModel

class PaisSchema(BaseModel):
    id: int
    iso: str
    nombre: str