from sqlalchemy import Column, Integer, String, Date, Boolean, Text
from .db import Base

class Usuario(Base):
    __tablename__ = 'usuario'
    __table_args__ = {'schema': 'public'} 
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    nombres = Column(String, nullable=False)
    apellidos = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    birthdate = Column(Date, nullable=True)
    clave = Column( String, nullable=True)
    tipodoc = Column(Integer, nullable=False)
    numdoc = Column(String, nullable=False)
    pais_id = Column(String)
    departamento_id = Column(String)
    distrito_id = Column(String)
    genero = Column(String, nullable=False)
    telefono = Column(String)
    fecha_creacion = Column(Date)
    rol = Column(Integer)
    activo = Column(Boolean, server_default='true')
    imagen_base64 = Column(Text, nullable=True)