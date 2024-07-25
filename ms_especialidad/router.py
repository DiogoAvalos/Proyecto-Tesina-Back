from fastapi import Depends,APIRouter
from sqlalchemy.orm import Session
from typing import List
from .db import get_db
from .models import Especialidad
from .schema import EspecialidadOut
from .tokenJwt import Validacion

router = APIRouter(tags=['Citas'],route_class=Validacion)

@router.get("/especialidades", response_model=List[EspecialidadOut])
def listar_medicos(db: Session = Depends(get_db)):
    return db.query(Especialidad).filter(Especialidad.activo == True).order_by(Especialidad.descripcion).all()

