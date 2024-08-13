from typing import List
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from datetime import timedelta
from .db import get_db
from .models import Usuario
from .schema import UsuarioSchema, LoginForm
from .security import token, seguridad
import os

router = APIRouter(tags=['Usuario'])

@router.get("/usuarios/", response_model=List[UsuarioSchema])
def get_usuarios(db: Session = Depends(get_db)):
    usuarios = db.query(Usuario).all()
    return [UsuarioSchema.from_orm(usuario) for usuario in usuarios]

@router.post("/usuarios/", response_model=UsuarioSchema)
def create_usuario(usuario: UsuarioSchema, db: Session = Depends(get_db)):
    hashed_password = seguridad.get_password_hash(usuario.clave)
    db_usuario = Usuario(
        **usuario.dict(exclude={"clave"}),
        clave=hashed_password
    )
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario


@router.post("/login")
def login(form_data: LoginForm, db: Session = Depends(get_db)):
    user = db.query(Usuario).filter(Usuario.username == form_data.username).first()
    if not user or not seguridad.verify_password(form_data.password, user.clave):
        raise HTTPException(status_code=401, detail="¡Nombre de usuario o contraseña incorrectos!")
    access_token_expires = timedelta(minutes=int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30)))
    access_token = token.create_access_token(data={"sub": user.username}, expires_delta=access_token_expires)
    return {"access_token": access_token, "token_type": "bearer"}
