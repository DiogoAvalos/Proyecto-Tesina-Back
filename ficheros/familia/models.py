from sqlalchemy import Column, Integer, String, event, DDL, BOOLEAN, Date, ForeignKey
from ..db import Base

class Familia(Base):
    __tablename__ = 'familia'
    __table_args__= {'schema': 'public'}
    id = Column(Integer, primary_key=True)
    codigo_familia = Column(String, index=True)
    descripcion = Column(String)
    estado = Column(BOOLEAN, server_default='true')
    creador = Column(String)
    creacion = Column(Date)

class SubFamilia(Base):
    __tablename__ = 'subfamilia'
    __table_args__= {'schema': 'public'}
    id = Column(Integer, primary_key=True)
    familia_id = Column(Integer, ForeignKey('public.familia.id'), index=True)
    codigo_subfamilia = Column(String, index=True)
    descripcion = Column(String)
    creador = Column(String)
    creacion = Column(Date)
