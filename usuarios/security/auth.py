from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session
from .token import create_access_token
from .seguridad import verificar_clave, get_user
from ..db import get_db

def authenticate_user(db: Session, username: str, password: str):
    user = get_user(db, username)
    if not user or not verificar_clave(password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Incorrect username or password")
    return user

def login(username: str, password: str, db: Session = Depends(get_db)):
    user = authenticate_user(db, username, password)
    access_token = create_access_token({"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}
