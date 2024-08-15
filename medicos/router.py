from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .db import get_db
from .models import Medico
from .schema import MedicoSchema

router = APIRouter(tags=['Medico'])

@router.get("/medico/", response_model=List[MedicoSchema])
def get_usuarios(db: Session = Depends(get_db)):
    listas = db.query(Medico).all()
    return [MedicoSchema.from_orm(lista) for lista in listas]
