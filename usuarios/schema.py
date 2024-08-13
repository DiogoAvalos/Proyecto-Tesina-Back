from pydantic import BaseModel
from datetime import date 

class UsuarioSchema(BaseModel):
    id: int | None
    username: str
    nombres: str
    apellidos: str
    email: str
    birthdate: date
    clave: str
    tipodoc: str
    numdoc: str
    pais_id: str | None
    departamento: str | None
    distrito: str | None
    genero: str
    telefono: str | None
    #*fecha_creacion: date | None
    rol: str | None
    activo: bool | None
    imagen_base64: str | None
    
    class Config:
            orm_mode = True

class LoginForm(BaseModel):
    username: str
    password: str