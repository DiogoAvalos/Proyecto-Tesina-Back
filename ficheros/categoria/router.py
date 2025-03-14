from typing import List
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from ..db import get_db
from .models import *
from .schema import *

categoria = APIRouter(prefix="/categoria", tags=["Ficheros"])

#* Categoria GET
@categoria.get("/categoria", response_model=List[CategoriaSchema])
def get_categoria(db: Session = Depends(get_db)):
    try:
        categoria = db.query(Categoria).all()
        return categoria
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
