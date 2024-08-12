from sqlalchemy import CHAR, Column, Integer, String, event, DDL
from ..db import Base

class Paises(Base):
    __tablename__="pais"
    __table_args__= {'schema': 'public'}
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre = Column(String, nullable=False)

event.listen(Paises.__table__, 'after_create',
            DDL("""
            INSERT INTO pais (id, nombre) values (1,'PERU');
            INSERT INTO pais (id, nombre) values (2,'ECUADOR');
            INSERT INTO pais (id, nombre) values (3,'MEXICO');
            INSERT INTO pais (id, nombre) values (4,'BOLIVIA');
            INSERT INTO pais (id, nombre) values (5,'VENEZUELA');
            INSERT INTO pais (id, nombre) values (6,'CHILE');
            INSERT INTO pais (id, nombre) values (7,'JAPON');
            INSERT INTO pais (id, nombre) values (8,'USA');
            INSERT INTO pais (id, nombre) values (9,'RUSIA');
            INSERT INTO pais (id, nombre) values (10,'COLOMBIA');
            INSERT INTO pais (id, nombre) values (11,'ARGENTINA');
            INSERT INTO pais (id, nombre) values (12,'URUGUAY');
            INSERT INTO pais (id, nombre) values (13,'PARAGUAY');
            INSERT INTO pais (id, nombre) values (14,'ALEMANIA');
            INSERT INTO pais (id, nombre) values (15,'BRASIL');
            INSERT INTO pais (id, nombre) values (16,'CANADA');
            INSERT INTO pais (id, nombre) values (17,'CUBA');
            INSERT INTO pais (id, nombre) values (18,'CHINA');
            INSERT INTO pais (id, nombre) values (19,'COREA');
            INSERT INTO pais (id, nombre) values (20,'ESPAÑA');
            INSERT INTO pais (id, nombre) values (21,'ALEMANIA');
            INSERT INTO pais (id, nombre) values (22,'PORTUGAL');
            INSERT INTO pais (id, nombre) values (23,'BELGICA');
            INSERT INTO pais (id, nombre) values (24,'SUECIA');
            INSERT INTO pais (id, nombre) values (25,'SUIZA');
            INSERT INTO pais (id, nombre) values (26,'INGLATERRA');
            INSERT INTO pais (id, nombre) values (27,'FRANCIA');
            INSERT INTO pais (id, nombre) values (28,'BULGARIA');
            INSERT INTO pais (id, nombre) values (29,'ITALIA');
            INSERT INTO pais (id, nombre) values (30,'AUSTRALIA');
            INSERT INTO pais (id, nombre) values (31,'RUSIA');
            INSERT INTO pais (id, nombre) values (32,'NICARAGUA');
            INSERT INTO pais (id, nombre) values (33,'PUERTO RICO');
            INSERT INTO pais (id, nombre) values (34,'RUMANIA');
            INSERT INTO pais (id, nombre) values (35,'MALAWI');
            INSERT INTO pais (id, nombre) values (36,'COSTA RICA');
            INSERT INTO pais (id, nombre) values (37,'FINLANDIA');
            INSERT INTO pais (id, nombre) values (38,'HOLANDA');
            INSERT INTO pais (id, nombre) values (39,'HONDURAS');
            INSERT INTO pais (id, nombre) values (40,'INDONESIA');
            INSERT INTO pais (id, nombre) values (41,'PANAMA');
            INSERT INTO pais (id, nombre) values (42,'GRECIA');
            INSERT INTO pais (id, nombre) values (43,'TURQUIA');
            INSERT INTO pais (id, nombre) values (44,'REP. DOMINICANA');
            INSERT INTO pais (id, nombre) values (45,'AUSTRIA');
            INSERT INTO pais (id, nombre) values (46,'GUATEMALA');
            INSERT INTO pais (id, nombre) values (47,'SUDAFRICA');
            INSERT INTO pais (id, nombre) values (48,'INDIA');
            INSERT INTO pais (id, nombre) values (49,'REPUBLICA CHECA');
            INSERT INTO pais (id, nombre) values (50,'ESCOCIA');
            INSERT INTO pais (id, nombre) values (51,'ISRAEL');
            INSERT INTO pais (id, nombre) values (52,'DINAMARCA');
            INSERT INTO pais (id, nombre) values (53,'LITUANIA');
            INSERT INTO pais (id, nombre) values (54,'JORDANIA');
            INSERT INTO pais (id, nombre) values (55,'BAHAMAS');
            INSERT INTO pais (id, nombre) values (56,'NUEVA ZELANDA');
            INSERT INTO pais (id, nombre) values (57,'IRAN');
            INSERT INTO pais (id, nombre) values (58,'POLONIA');
            INSERT INTO pais (id, nombre) values (59,'DINAMARCA');
            INSERT INTO pais (id, nombre) values (60,'LIBANO');
            INSERT INTO pais (id, nombre) values (61,'MARRUECOS');
            INSERT INTO pais (id, nombre) values (62,'REINO UNIDO');
            ALTER SEQUENCE pais_id_seq RESTART 63;
        """))