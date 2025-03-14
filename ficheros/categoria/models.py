from sqlalchemy import Column, Integer, String, event, DDL, BOOLEAN, Date, ForeignKey
from ..db import Base

class Categoria(Base):
    __tablename__ = 'categoria'
    __table_args__= {'schema': 'public'}
    id = Column(Integer, primary_key=True)
    descripcion = Column(String)
    estado = Column(BOOLEAN, server_default='true')
    creador = Column(String)
    creacion = Column(Date)
