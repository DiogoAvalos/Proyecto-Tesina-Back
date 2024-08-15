from sqlalchemy import Column, Integer, String, Date, Boolean, Text, Table, ForeignKey, ARRAY
from .db import Base, engine

class TipoDoc(Base):
    __table__ = Table("tipo_doc", Base.metadata,autoload_with=engine,extend_existing=True)

class Especialidad(Base):
    __table__ = Table("especialidad", Base.metadata,autoload_with=engine,extend_existing=True)

class Medico(Base):
    __tablename__ = 'medico'
    __table_args__ = {'schema': 'public'} 
    id = Column(Integer, primary_key=True, index=True)
    nombres = Column(String)
    apellido_p = Column(String, nullable=True)
    apellido_m = Column(String, nullable=True)
    tipodoc = Column(Integer, ForeignKey("tipo_doc.id"), nullable=False)
    numdoc = Column(String, nullable=False)
    especialidad_id = Column(Integer, ForeignKey("especialidad.id"), nullable=False)
    activo = Column(Boolean, server_default='true')