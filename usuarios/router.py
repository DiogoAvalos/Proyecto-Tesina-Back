from typing import List
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from .db import get_db
from .models import Usuario
from .schema import UsuarioSchema

router = APIRouter(tags=['Usuario'])

#* Trae al usuario por id
@router.get("/usuarios/", response_model=List[UsuarioSchema])
def get_usuarios(db: Session = Depends(get_db)):
    usuarios = db.query(Usuario).all()
    return [UsuarioSchema.from_orm(usuario) for usuario in usuarios]

@router.post("/usuarios/", response_model=UsuarioSchema)
def _(usuario: UsuarioSchema, db: Session = Depends(get_db)):
    db_usuario = Usuario(**usuario.dict())
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario
