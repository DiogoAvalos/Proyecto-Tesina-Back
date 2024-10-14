from sqlalchemy import Column, String, event, DDL, Date
from ..db import Base

class UnidadVenta(Base):
    __tablename__ = 'unidad_venta'
    __table_args__= {'schema': 'public'}
    id = Column(String, primary_key=True)
    descripcion = Column(String)
    creador = Column(String)
    creacion = Column(Date)


# event.listen(UnidadVenta.__table__, 'after_create',
#             DDL("""
#         """))