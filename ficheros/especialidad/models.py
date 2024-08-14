from sqlalchemy import Column, String, event, DDL, BOOLEAN
from ..db import Base

class Especialidad(Base):
    __tablename__="especialidad"
    __table_args__= {'schema': 'public'}
    id = Column(String, primary_key=True, unique=True, autoincrement=True)
    descripcion = Column(String)
    estado = Column(BOOLEAN)

event.listen(Especialidad.__table__, 'after_create',
            DDL("""
                INSERT INTO public.especialidad (descripcion, estado) VALUES
                ('CARDIOLOGÍA', true),
                ('DERMATOLOGÍA', true),
                ('NEUROLOGÍA', true),
                ('PEDIATRÍA', true),
                ('GINECOLOGÍA', true);
        """))