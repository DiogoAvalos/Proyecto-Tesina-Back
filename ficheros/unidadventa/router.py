from typing import List
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from ..db import get_db
from .models import UnidadVenta
from .schema import UnidadVentaSchema

unidad_venta = APIRouter(prefix="/unidad_venta", tags=["Ficheros"])

@unidad_venta.get("/", response_model=List[UnidadVentaSchema])
def read_paises(db: Session = Depends(get_db)):
    try:
        paises = db.query(UnidadVenta).all()
        return paises
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
