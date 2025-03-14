from sqlalchemy import Column, Integer, String, Float, BOOLEAN, DateTime, ForeignKey, Table
from .db import Base, engine

class UnidadVenta(Base):
    __table__ = Table('unidad_venta', Base.metadata,autoload_with=engine,extend_existing=True)

class Familia(Base):
    __table__ = Table('familia', Base.metadata,autoload_with=engine,extend_existing=True)

class SubFamilia(Base):
    __table__ = Table('subfamilia', Base.metadata,autoload_with=engine,extend_existing=True)

class Categoria(Base):
    __table__ = Table('categoria', Base.metadata, autoload_with=engine, extend_existing=True)

class Marca(Base):
    __table__ = Table('marca', Base.metadata, autoload_with=engine, extend_existing=True)

class Proveedor(Base):
    __table__ = Table('proveedor', Base.metadata, autoload_with=engine, extend_existing=True)

class Producto(Base):
    __tablename__ = 'producto'
    __table_args__= {'schema': 'public'}
    id = Column(Integer, primary_key=True)
    nombre = Column(String, index=True)
    descripcion = Column(String)
    precio = Column(Float, index=True)
    stock = Column(Integer, index=True)
    categoria_id = Column(Integer, ForeignKey('categoria.id'))
    marca_id = Column(Integer, ForeignKey('marca.id'))
    proveedor_id = Column(Integer, ForeignKey('proveedor.id'))
    unidad_venta_id = Column(String, ForeignKey('unidad_venta.id'))
    familia_id = Column(Integer, ForeignKey('familia.id'))
    subfamilia_id = Column(Integer, ForeignKey('subfamilia.id'))
    estado = Column(BOOLEAN, server_default='true')
    creador = Column(String)
    creacion = Column(DateTime)
