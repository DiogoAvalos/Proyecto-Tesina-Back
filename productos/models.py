from sqlalchemy import Column, Integer, String, DATE, Numeric
from .db import Base, engine

class Producto(Base):
    __tablename__ = "productos"
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    descripcion = Column(String)
    precio = Column(Numeric)
    fecha_salida = Column(DATE)