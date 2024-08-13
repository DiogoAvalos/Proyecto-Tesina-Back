from passlib.context import CryptContext
from typing import Optional
from sqlalchemy.orm import Session
from ..models import Usuario

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def encriptar_clave(password: str) -> str:
    return pwd_context.hash(password)

def verificar_clave(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def get_user(db: Session, username: str) -> Optional[Usuario]:
    return db.query(Usuario).filter(Usuario.username == username).first()
