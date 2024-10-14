from typing import List
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from ..db import get_db
from .models import Familia, SubFamilia
from .schema import FamiliaSchema, SubFamiliaSchema

familia = APIRouter(prefix="/familia", tags=["Ficheros"])

#* Familia GET
@familia.get("/familia", response_model=List[FamiliaSchema])
def read_paises(db: Session = Depends(get_db)):
    try:
        paises = db.query(Familia).all()
        return paises
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

#* SubFamilia GET
@familia.get("/subfamilia", response_model=List[SubFamiliaSchema])
def read_paises(db: Session = Depends(get_db)):
    try:
        paises = db.query(SubFamilia).all()
        return paises
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
