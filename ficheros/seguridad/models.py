from sqlalchemy import Column, String, Integer, ForeignKey, BOOLEAN
from sqlalchemy.orm import relationship
from ..db import Base

class Rol(Base):
    __tablename__ = 'rol'
    __table_args__ = {'schema': 'public'}
    
    id = Column(Integer, primary_key=True)
    nombre_rol = Column(String)
    menus = relationship('RoleMenu', back_populates='role')

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
