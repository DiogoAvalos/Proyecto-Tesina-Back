from typing import List
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from ..db import get_db
from .models import *
from .schema import *

unidad_venta = APIRouter(prefix="/unidad_venta", tags=["Ficheros"])

@unidad_venta.get("/", response_model=List[UnidadVentaSchema])
def get_unidad_venta(db: Session = Depends(get_db)):
    try:
        unidad_ventas = db.query(UnidadVenta).all()
        return unidad_ventas
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
