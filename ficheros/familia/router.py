from typing import List
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from ..db import get_db
from .models import Familia, SubFamilia
from .schema import FamiliaSchema, SubFamiliaSchema

familia = APIRouter(prefix="/familia", tags=["Ficheros"])

#* Familia GET
@familia.get("/familia", response_model=List[FamiliaSchema])
def get_familia(db: Session = Depends(get_db)):
    try:
        familia = db.query(Familia).all()
        return familia
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

#* SubFamilia GET
@familia.get("/subfamilia", response_model=List[SubFamiliaSchema])
def get_subfamilia(db: Session = Depends(get_db)):
    try:
        subfamilia = db.query(SubFamilia).all()
        return subfamilia
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
