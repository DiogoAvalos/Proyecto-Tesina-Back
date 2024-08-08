from typing import List
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from ..db import get_db

pais = APIRouter(prefix="/paises", tags=["Ficheros"])