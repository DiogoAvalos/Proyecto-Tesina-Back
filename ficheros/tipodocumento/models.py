from sqlalchemy import Column, Integer, String, event, DDL, BOOLEAN
from ..db import Base

class TipoDoc(Base):
    __tablename__="tipo_doc"
    __table_args__= {'schema': 'public'}
    id = Column(Integer, primary_key=True, unique=True)
    cod_sunat = Column(String, unique=True)
    cod_corto = Column(String, unique=True)
    descripcion = Column(String)
    activo = Column(BOOLEAN)

event.listen(TipoDoc.__table__, 'after_create',
            DDL("""
                INSERT INTO tipo_doc (cod_sunat, cod_corto, descripcion, activo) VALUES ('0', 'OTROS', 'OTROS TIPOS DE DOCUMENTOS', true);
                INSERT INTO tipo_doc (cod_sunat, cod_corto, descripcion, activo) VALUES ('1', 'DNI', 'DOCUMENTO NACIONAL DE IDENTIDAD (DNI)', true);
                INSERT INTO tipo_doc (cod_sunat, cod_corto, descripcion, activo) VALUES ('4', 'CARNET', 'CARNET DE EXTRANJERIA', true);
                INSERT INTO tipo_doc (cod_sunat, cod_corto, descripcion, activo) VALUES ('6', 'RUC', 'REGISTRO ÚNICO DE CONTRIBUYENTES', true);
                INSERT INTO tipo_doc (cod_sunat, cod_corto, descripcion, activo) VALUES ('7', 'PAS', 'PASAPORTE', true);
                INSERT INTO tipo_doc (cod_sunat, cod_corto, descripcion, activo) VALUES ('A', 'CDI', 'CÉDULA DIPLOMÁTICA DE IDENTIDAD', true);
        """))