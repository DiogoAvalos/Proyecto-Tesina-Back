from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .db import get_db
from .models import Usuario
from .schema import UsuarioSchema

router = APIRouter(tags=['Seguridad'])

