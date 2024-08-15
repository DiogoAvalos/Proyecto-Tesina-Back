from sqlalchemy import CHAR, Column, Integer, String, event, DDL
from ..db import Base

class TipoDoc(Base):
    __tablename__="tipo_doc"
    __table_args__= {'schema': 'public'}
    id = Column(Integer, primary_key=True, unique=True)
    cod_sunat = Column(String, unique=True)
    descripcion = Column(String)

event.listen(TipoDoc.__table__, 'after_create',
            DDL("""
                INSERT INTO tipo_doc (cod_sunat, descripcion) VALUES ('0', 'OTROS TIPOS DE DOCUMENTOS');
                INSERT INTO tipo_doc (cod_sunat, descripcion) VALUES ('1', 'DOCUMENTO NACIONAL DE IDENTIDAD (DNI)');
                INSERT INTO tipo_doc (cod_sunat, descripcion) VALUES ('4', 'CARNET DE EXTRANJERIA');
                INSERT INTO tipo_doc (cod_sunat, descripcion) VALUES ('6', 'REGISTRO ÚNICO DE CONTRIBUYENTES');
                INSERT INTO tipo_doc (cod_sunat, descripcion) VALUES ('7', 'PASAPORTE');
                INSERT INTO tipo_doc (cod_sunat, descripcion) VALUES ('A', 'CÉDULA DIPLOMÁTICA DE IDENTIDAD');
        """))