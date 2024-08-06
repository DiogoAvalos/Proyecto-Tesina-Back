from pydantic import BaseModel
from datetime import date 

class UsuarioBase(BaseModel):
    username: str
    nombres: str
    apellidos: str
    email: str
    birthdate: date
    clave: str
    tipodoc: int
    numdoc: str
    pais: str | None
    ciudad: str | None
    genero: str
    telefono: str | None
    fecha_creacion: date | None
    rol: str
    activo: bool | None
    imagen_base64: str | None