from pydantic import BaseModel
from datetime import date, datetime

class ORMBaseModel(BaseModel):
    class Config:
        orm_mode = True

class OrdenSchema(ORMBaseModel):
    oc_id: int | None
    oc_tipoorden: str
    oc_fecoc: date
    oc_invent: int | None
    oc_ppresup: str | None
    oc_ccosto: str | None
    oc_presup: int | None
    oc_personaid: int
    oc_vendedor: str | None
    oc_vendtel: str | None
    oc_vendmail: str | None
    oc_monedaid: int
    oc_tcaoc: float
    oc_mediopagoid: int
    oc_formapago: str | None
    oc_estoc: str
    oc_equipo: str
    oc_usuoc: str
    oc_fecpro: datetime | None
    oc_fecmod: datetime | None
    oc_usumod: str | None
    oc_banco: str | None
    oc_tipocuenta: str | None
    oc_nrocuenta: str | None
    oc_cci: str | None
    oc_monbanco: int | None
    oc_ref: str | None
    oc_obs: str | None
    oc_autoriza: str | None
    oc_cargo: str
    oc_descg: float | None
    oc_remitente: str | None
    oc_autoriza2: str | None
    oc_cargo2: str | None
    usuario_conformidad: str | None
    conformidad: datetime | None
    oc_autorizacion1: datetime | None
    oc_autorizacion2: datetime | None
    solicita_aut: bool | None
    obs_autoriza1: str | None
    obs_autoriza2: str | None
    oc_obs2: str | None
    ruc: str | None
    razonsocial: str | None
    ncargo: str | None
    ncargo2: str | None
    nmoneda: str | None
    estadoaut: str | None
    totalneto: float | None