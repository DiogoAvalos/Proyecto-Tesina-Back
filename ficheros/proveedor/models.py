from sqlalchemy import Column, Integer, String, BOOLEAN, DateTime
from ..db import Base

class Marca(Base):
    __tablename__ = 'proveedor'
    __table_args__= {'schema': 'public'}
    id = Column(Integer, primary_key=True)
    nombre_prov = Column(String)
    ruc = Column(String)
    direccion = Column(String)
    contacto = Column(String) #* Correo
    telefono = Column(String) #* Numero telefonico
    estado = Column(BOOLEAN, server_default='true')
    creador = Column(String)
    creacion = Column(DateTime)
