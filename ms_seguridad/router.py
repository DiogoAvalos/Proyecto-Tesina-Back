from typing import List
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from .db import get_db
from .models import Usuario
from .schema import UsuarioSchema

router = APIRouter(tags=['Usuario'])

#* Trae al usuario por id
@router.get("/usuarios/{id}", response_model=UsuarioSchema)
def get_usuario(id: int, db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.id == id).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="User not found")
    return UsuarioSchema.from_orm(usuario)

@router.post("/usuarios", response_model=UsuarioSchema)
def crear_usuario(usuario: UsuarioSchema, db: Session = Depends(get_db)):
    db_usuario = UsuarioSchema(**usuario.dict())
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario
