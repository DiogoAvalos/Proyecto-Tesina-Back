from sqlalchemy import Column, Integer, String, Float, BOOLEAN, Date, ForeignKey, Table
from .db import Base, engine

# class Producto(Base):
#     __tablename__ = "productos"
#     id = Column(Integer, primary_key=True)
#     nombre = Column(String)
#     descripcion = Column(String)
#     precio = Column(Numeric)
#     fecha_salida = Column(DATE)

class UnidadVenta(Base):
    __table__ = Table('unidad_venta', Base.metadata,autoload_with=engine,extend_existing=True)

class Familia(Base):
    __table__ = Table('familia', Base.metadata,autoload_with=engine,extend_existing=True)

class SubFamilia(Base):
    __table__ = Table('subfamilia', Base.metadata,autoload_with=engine,extend_existing=True)

class Producto(Base):
    __tablename__ = 'producto'
    __table_args__= {'schema': 'public'}
    id = Column(Integer, primary_key=True)
    nombre = Column(String, index=True)
    descripcion = Column(String)
    precio = Column(Float, index=True)
    stock = Column(Integer, index=True)
    unidad_venta_id = Column(Integer, ForeignKey('unidad_venta.id'), index=True)
    familia_id = Column(Integer, ForeignKey('familia.id'), index=True)
    subfamilia_id = Column(Integer, ForeignKey('subfamilia.id', index=True))
    estado = Column(BOOLEAN, server_default='true')
    creacion = Column(Date)
