from sqlalchemy import Column, Integer, String, Date
from .db import Base

class Producto(Base):
    __tablename__ = 'persona'
    __table_args__= {'schema': 'public'}
    id = Column(Integer, primary_key=True)
    nombres = Column(String)
    apaterno = Column(String)
    amaterno = Column(String)
    doc_ident = Column(String, index=True)
    tipo_doc_id = Column(String)
    fecha_nacimiento = Column(Date)
    direccion = Column(String)
    telefono = Column(String)
    email = Column(String)
    genero = Column(String)
    activo = Column(String)