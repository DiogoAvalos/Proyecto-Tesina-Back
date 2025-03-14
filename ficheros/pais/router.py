from typing import List
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from ..db import get_db
from .models import Paises
from .schema import PaisSchema

pais = APIRouter(prefix="/paises", tags=["Ficheros"])

@pais.get("/", response_model=List[PaisSchema])
def get_pais(db: Session = Depends(get_db)):
    try:
        paises = db.query(Paises).all()
        return paises
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
