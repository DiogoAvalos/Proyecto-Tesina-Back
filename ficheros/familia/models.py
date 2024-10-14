from sqlalchemy import Column, Integer, String, event, DDL, BOOLEAN, Date
from ..db import Base

class Familia(Base):
    __tablename__ = 'familia'
    __table_args__= {'schema': 'public'}
    id = Column(Integer, primary_key=True)
    codigo_familia = Column(String, index=True)
    descripcion = Column(String)
    estado = Column(BOOLEAN, server_default='true')
    creador = Column(String)
    creacion = Column(Date)

# event.listen(Familia.__table__, 'after_create',
#             DDL("""
#         """))