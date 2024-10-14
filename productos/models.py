from sqlalchemy import Column, Integer, String, Float, BOOLEAN, Date, ForeignKey, Table, Numeric, DATE
from .db import Base, engine

class Productos(Base):
    __tablename__ = "productos"
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    descripcion = Column(String)
    precio = Column(Numeric)
    fecha_salida = Column(DATE)

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
    unidad_venta_id = Column(String, ForeignKey('unidad_venta.id'))
    familia_id = Column(Integer, ForeignKey('familia.id'))
    subfamilia_id = Column(Integer, ForeignKey('subfamilia.id'))
    estado = Column(BOOLEAN, server_default='true')
    creacion = Column(Date)
