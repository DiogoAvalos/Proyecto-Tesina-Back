from typing import List
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from ..db import get_db
from .models import TipoDoc
from .schema import TipoDocSchema

tipodoc = APIRouter(prefix="/tipodoc", tags=["Ficheros"])

@tipodoc.get("/", response_model=List[TipoDocSchema])
def get_tipodoc(db: Session = Depends(get_db)):
    try:
        tipodoc = db.query(TipoDoc).all()
        return tipodoc
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
