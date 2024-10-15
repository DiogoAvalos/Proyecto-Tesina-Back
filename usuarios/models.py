from sqlalchemy import Column, Integer, String, Date, Boolean, Table, ForeignKey, Text, BOOLEAN
from sqlalchemy.orm import relationship
from .db import Base, engine

class Pais(Base):
    __table__ = Table("pais", Base.metadata,autoload_with=engine,extend_existing=True)

class TipoDoc(Base):
    __table__ = Table("tipo_doc", Base.metadata,autoload_with=engine,extend_existing=True)

#* Tabla de roles
class Rol(Base):
    __tablename__ = 'rol'
    __table_args__ = {'schema': 'public'}
    id = Column(Integer, primary_key=True)
    nombre_rol = Column(String)
    menus = relationship('RoleMenu', back_populates='role')
    users = relationship('UserRole', back_populates='role')

class Usuario(Base):
    __tablename__ = 'usuario'
    __table_args__ = {'schema': 'public'} 
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    nombres = Column(String, nullable=False)
    apellidos = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    fecha_nacimiento = Column(Date, nullable=True)
    clave = Column( String, nullable=True)
    tipodoc = Column(Integer, ForeignKey("tipo_doc.id"), nullable=False, index=True)
    numdoc = Column(String, nullable=False)
    pais_id = Column(Integer, ForeignKey("pais.id"), index=True)
    departamento = Column(String)
    distrito = Column(String)
    genero = Column(String, nullable=False)
    telefono = Column(String)
    activo = Column(Boolean, server_default='true')
    imagen_base64 = Column(Text, nullable=True)
    roles = relationship('UserRole', back_populates='user')

class UserRole(Base):
    __tablename__ = 'user_role'
    __table_args__ = {'schema': 'public'}
    user_id = Column(Integer, ForeignKey('public.usuario.id'), primary_key=True)
    role_id = Column(Integer, ForeignKey('public.rol.id'), primary_key=True)
    user = relationship('Usuario', back_populates='roles')
    role = relationship('Rol', back_populates='users')

#TODO: Generación de tablas para la relacion de los roles
class MenuItems(Base):
    __tablename__ = 'menu_items'
    __table_args__ = {'schema': 'public'}
    id = Column(Integer, primary_key=True)
    label = Column(String, index=True)
    icon = Column(String)
    router_link = Column(String)
    activo = Column(BOOLEAN, server_default='true')
    roles = relationship('RoleMenu', back_populates='menu_item')


class RoleMenu(Base):
    __tablename__ = 'role_menu'
    __table_args__ = {'schema': 'public'}
    role_id = Column(Integer, ForeignKey('public.rol.id'), primary_key=True)
    menu_id = Column(Integer, ForeignKey('public.menu_items.id'), primary_key=True)
    role = relationship('Rol', back_populates='menus')
    menu_item = relationship('MenuItems', back_populates='roles')
