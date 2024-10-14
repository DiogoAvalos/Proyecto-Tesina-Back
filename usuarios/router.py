from faker import Faker #* Test con datos de pruebas
from typing import List
from fastapi import APIRouter, HTTPException, Depends, Body
from pydantic import ValidationError
from sqlalchemy.orm import Session
from datetime import timedelta
from .db import get_db
from .models import Usuario
from .schema import UsuarioSchema, LoginForm, Imagen64
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


#* Crear registro de usuario
@router.post("/usuarios/", response_model=UsuarioSchema)
def create_usuario(usuario: UsuarioSchema, db: Session = Depends(get_db)):
    existing_user = db.query(Usuario).filter(Usuario.username == usuario.username).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="El usuario ya existe.")
    hashed_password = seguridad.encriptar_clave(usuario.clave)
    db_usuario = Usuario(**usuario.dict(exclude={"clave"}), clave=hashed_password)
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return { "message": "Se registró correctamente el usuario." }


#* Verificación de usuario
@router.post("/login")
def login(data: LoginForm, db: Session = Depends(get_db)):
    user = db.query(Usuario).filter(Usuario.username == data.username).first()
    if not user.activo:
        raise HTTPException(status_code=403, detail="El usuario se encuentra inactivo, contacte con soporte.")
    if not seguridad.verificar_clave(data.password, user.clave):
        raise HTTPException(status_code=401, detail="¡Contraseña incorrecta!")
    
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
            "fecha_nacimiento": user.fecha_nacimiento,
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


#* Actualiza el registro del usuario
@router.put("/{id}")
async def update_usuario(id: str, usuarioSchema: UsuarioSchema, db: Session = Depends(get_db)):
    try:
        if usuarioSchema.clave:
            usuarioSchema.clave = seguridad.encriptar_clave(usuarioSchema.clave)
        await CrudBase(Usuario).put(db, usuarioSchema, id)
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=f"Error de formato: {e}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"{str(e)}")
    return {"message": "¡Se actualizó el usuario correctamente!"}


#* Actualiza la imagen del usuario
@router.put("/imagen/{user_id}", response_model=Imagen64)
def update_imagen(user_id: int, imagen_base64: str = Body(...), db: Session = Depends(get_db)):
    db_usuario = db.query(Usuario).filter(Usuario.id == user_id).first()
    if not db_usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    db_usuario.imagen_base64 = imagen_base64
    db.commit()
    db.refresh(db_usuario)
    return Imagen64(user_id=db_usuario.id, imagen_base64=db_usuario.imagen_base64)


#* Crea data fake si tiene menos de 10 registros
def create_fake_user(db: Session):
    fake_user = UsuarioSchema(
        id=None,
        username=fake.user_name(),
        nombres=fake.first_name(),
        apellidos=fake.last_name(),
        email=fake.email(),
        fecha_nacimiento=fake.date_of_birth(),
        clave="password",
        tipodoc=1,
        numdoc=fake.ssn(),
        pais_id=1,
        departamento=fake.state(),
        distrito=fake.city(),
        genero=fake.random_element(elements=('M', 'F')),
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