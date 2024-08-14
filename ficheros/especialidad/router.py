from typing import List
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from ..db import get_db
from .models import Especialidad
from .schema import EspecialidadSchema

especialidad = APIRouter(prefix="/especialidad", tags=["Ficheros"])

@especialidad.get("/", response_model=List[EspecialidadSchema])
def _(db: Session = Depends(get_db)):
    try:
        especialidad = db.query(Especialidad).all()
        return especialidad
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
