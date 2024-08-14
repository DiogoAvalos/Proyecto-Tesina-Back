from sqlalchemy import Column, Integer, String, Date, Boolean, Text, Table, ForeignKey, ARRAY
from .db import Base, engine

class Especialidad(Base):
    __table__ = Table("especialidad", Base.metadata,autoload_with=engine,extend_existing=True)

class Medico(Base):
    __tablename__ = 'medico'
    __table_args__ = {'schema': 'public'} 
    id = Column(Integer, primary_key=True, index=True)