from typing import List
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from .db import get_db
from .models import Usuario
from .schema import UsuarioBase

router = APIRouter(tags=['Usuario'])

@router.get("/usuarios", response_model=List[UsuarioBase])
def get_usuarios(db: Session = Depends(get_db)):
    usuarios = db.query(Usuario).all()
    if not usuarios:
        raise HTTPException(status_code=404, detail="No users found")
    return usuarios