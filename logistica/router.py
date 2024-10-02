from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .db import get_db
from .models import Orden
from .schema import OrdenSchema

router = APIRouter(tags=['Orden'], prefix="/orden" )

@router.get("/", response_model=List[OrdenSchema])
def get_usuarios(db: Session = Depends(get_db)):
    listas = db.query(Orden).all()
    return [OrdenSchema.from_orm(lista) for lista in listas]
