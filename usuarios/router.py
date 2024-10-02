from faker import Faker #* Test con datos de pruebas
from typing import List
from fastapi import APIRouter, HTTPException, Depends, Body
from sqlalchemy.orm import Session
from datetime import timedelta
from .db import get_db
from .models import Usuario
from .schema import UsuarioSchema, LoginForm
from .security import token, seguridad
import os
from .crud.crudBase import CrudBase

router = APIRouter(tags=['Usuario'])
fake = Faker()

# @router.get("/usuarios/", response_model=List[UsuarioSchema])
# def get_usuarios(db: Session = Depends(get_db)):
#     usuarios = db.query(Usuario).all()
#     return [UsuarioSchema.from_orm(usuario) for usuario in usuarios]

#* Endpoint de prueba
@router.get("/usuarios/", response_model=List[UsuarioSchema])
def get_usuarios(db: Session = Depends(get_db)):
    usuarios = db.query(Usuario).all()
    if len(usuarios) < 10:
        for _ in range(100 - len(usuarios)):
            create_fake_user(db)
        usuarios = db.query(Usuario).all()
    return [UsuarioSchema.from_orm(usuario) for usuario in usuarios]

@router.post("/usuarios/", response_model=UsuarioSchema)
def create_usuario(usuario: UsuarioSchema, db: Session = Depends(get_db)):
    hashed_password = seguridad.encriptar_clave(usuario.clave)
    db_usuario = Usuario(**usuario.dict(exclude={"clave"}), clave=hashed_password)
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return { "message": "Se registró correctamente el usuario." }

@router.post("/login")
def login(data: LoginForm, db: Session = Depends(get_db)):
    user = db.query(Usuario).filter(Usuario.username == data.username).first()
    if not user or not seguridad.verificar_clave(data.password, user.clave):
        raise HTTPException(status_code=401, detail="¡Nombre de usuario o contraseña incorrectos!")
    access_token_expires = timedelta(minutes=int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30)))
    access_token = token.create_access_token(data={"sub": user.username}, expires_delta=access_token_expires)
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user": {
            "id_usuario": user.id,
            "username": user.username,
            "nombres": user.nombres,
            "apellidos": user.apellidos,
            "imagen_base64": user.imagen_base64,
            "correo": user.email,
            "birthdate": user.birthdate,
            "clave": user.clave,
            "tipodoc": user.tipodoc,
            "numdoc": user.numdoc,
            "pais_id": user.pais_id,
            "departamento": user.departamento,
            "distrito": user.distrito,
            "genero": user.genero,
            "telefono": user.telefono,
            "rol": user.rol,
            "activo": user.activo
            }
    }

@router.put("/{id}")
async def _(id:str, usuarioSchema:UsuarioSchema, db:Session = Depends(get_db)):
    await CrudBase(Usuario).put(db, usuarioSchema, id)
    return {"message":"Se actualizo el usuario"}

@router.put("/imagen/{user_id}", response_model=UsuarioSchema)
def update_imagen(user_id: int, imagen_base64: str = Body(...), db: Session = Depends(get_db)):
    db_usuario = db.query(Usuario).filter(Usuario.id == user_id).first()
    if not db_usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    db_usuario.imagen_base64 = imagen_base64
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

def create_fake_user(db: Session):
    fake_user = UsuarioSchema(
        id=None,
        username=fake.user_name(),
        nombres=fake.first_name(),
        apellidos=fake.last_name(),
        email=fake.email(),
        birthdate=fake.date_of_birth(),
        clave="password",
        tipodoc=1,
        numdoc=fake.ssn(),
        pais_id=1,
        departamento=fake.state(),
        distrito=fake.city(),
        genero=fake.random_element(elements=('MASCULINO', 'FEMENINO')),
        telefono=fake.phone_number(),
        rol=1,
        activo=True,
        imagen_base64=None
    )

    hashed_password = seguridad.encriptar_clave(fake_user.clave)
    db_usuario = Usuario(**fake_user.dict(exclude={"clave"}), clave=hashed_password)
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    print(f"Usuario falso creado: {db_usuario.username}")  # Print para depuración
    return db_usuario