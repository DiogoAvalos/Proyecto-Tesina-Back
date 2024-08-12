from sqlalchemy import Column, Integer, String, Date, Boolean, Text, Table, ForeignKey
from .db import Base, engine

class Pais(Base):
    __table__ = Table("pais", Base.metadata,autoload_with=engine,extend_existing=True)

class TipoDoc(Base):
    __table__ = Table("tipo_doc", Base.metadata,autoload_with=engine,extend_existing=True)

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
    tipodoc = Column(String, ForeignKey("tipo_doc.id"), nullable=False)
    numdoc = Column(String, nullable=False)
    pais_id = Column(Integer, ForeignKey("pais.id"))
    departamento = Column(String)
    distrito = Column(String)
    genero = Column(String, nullable=False)
    telefono = Column(String)
    #*fecha_creacion = Column(Date)
    rol = Column(Integer)
    activo = Column(Boolean, server_default='true')
    imagen_base64 = Column(Text, nullable=True)