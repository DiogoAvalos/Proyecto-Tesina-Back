from typing import List
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from ..db import get_db
from .models import RoleMenu, Rol, MenuItems
from .schema import RoleMenuSchema, RolSchema, MenuItemSchema

seguridad = APIRouter(prefix="/seguridad", tags=["Ficheros"])

@seguridad.get('')
def _(db: get_db):
    return