from typing import List
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from ..db import get_db
from .models import *
from .schema import *

proveedor = APIRouter(prefix="/proveedor", tags=["Ficheros"])

#* Proveedor GET
@proveedor.get("/proveedor", response_model=List[MarcaSchema])
def get_proveedor(db: Session = Depends(get_db)):
    try:
        proveedor = db.query(MarcaSchema).all()
        return proveedor
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))