from pydantic import BaseModel
from datetime import date

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