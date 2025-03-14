from typing import List
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from ..db import get_db
from .models import *
from .schema import *

marca = APIRouter(prefix="/marca", tags=["Ficheros"])

#* Marca GET
@marca.get("/marca", response_model=List[MarcaSchema])
def get_marca(db: Session = Depends(get_db)):
    try:
        marca = db.query(MarcaSchema).all()
        return marca
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))