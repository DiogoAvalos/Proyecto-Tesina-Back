from typing import List
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from ..db import get_db
from .models import SubFamilia
from .schema import SubFamiliaSchema

router = APIRouter(prefix="/subfamilia", tags=["Ficheros"])

@router.get("/", response_model=List[SubFamiliaSchema])
def read_paises(db: Session = Depends(get_db)):
    try:
        paises = db.query(SubFamilia).all()
        return paises
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
