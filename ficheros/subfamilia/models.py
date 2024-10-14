from sqlalchemy import Column, Integer, String, event, DDL, Date, ForeignKey
from ..db import Base

class SubFamilia(Base):
    __tablename__ = 'subfamilia'
    __table_args__= {'schema': 'public'}
    id = Column(Integer, primary_key=True)
    familia_id = Column(Integer, ForeignKey('familia.id'), index=True)
    codigo_subfamilia = Column(String, index=True)
    descripcion = Column(String)
    creador = Column(String)
    creacion = Column(Date)

# event.listen(SubFamilia.__table__, 'after_create',
#             DDL("""
#         """))