from sqlalchemy import Column, Integer, String, Boolean
from .db import Base

class Especialidad(Base):
    __tablename__ = 'especialidad'

    id = Column(Integer, primary_key=True)
    descripcion = Column(String, nullable=True)
    activo = Column(Boolean, nullable=True, default=True)
