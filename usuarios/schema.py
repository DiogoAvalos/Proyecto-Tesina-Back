from pydantic import BaseModel
from datetime import date 

class UsuarioSchema(BaseModel):
    id: int | None
    username: str
    nombres: str
    apellidos: str
    email: str
    fecha_nacimiento: date | None
    clave: str
    tipodoc: str
    numdoc: str
    pais_id: int | None
    departamento: str | None
    distrito: str | None
    genero: str
    telefono: str | None
    #*fecha_creacion: date | None
    rol: str | None
    activo: bool | None
    
    class Config:
            orm_mode = True

class LoginForm(BaseModel):
    username: str
    password: str


class Imagen64(BaseModel):
    user_id: int
    imagen_base64: str | None

#TODO: Esquemas para las tablas de los menús y roles
class RolSchema(BaseModel):
    id: int
    nombre_rol: str | None

    class Config:
        orm_mode = True

class MenuItemSchema(BaseModel):
    id: int
    label: str
    icon: str
    router_link: str

    class Config:
        orm_mode = True

class RoleMenuSchema(BaseModel):
    role_id: int
    menu_id: int

    class Config:
        orm_mode = True