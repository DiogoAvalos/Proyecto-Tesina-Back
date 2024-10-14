from typing import List
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from datetime import date
from .db import get_db
from .models import Producto, Productos
from .schema import ProductoSchema

router = APIRouter(tags=['Producto'], prefix="/producto" )

@router.get("/", response_model=List[ProductoSchema])
def get_productos(db: Session = Depends(get_db)):
    listas = db.query(Productos).all()
    return [ProductoSchema.from_orm(lista) for lista in listas]

# @router.get("/ventapormes")
# def _(db: Session = Depends(get_db)):
#     query = f"""
#             SELECT 
#                 TO_CHAR(fecha_salida, 'YYYY-MM') AS mes,
#                 COUNT(*) AS "Total de productos por mes"
#             FROM 
#                 productos
#             WHERE 
#                 fecha_salida BETWEEN '2023-01-01' AND '2024-12-31'
#             GROUP BY 
#                 mes
#             ORDER BY 
#                 mes;
#     """
#     result = db.execute(query).all()
#     return result

@router.get("/ventapormes")
def ventas_por_mes(
    fecha_inicio: date = Query(..., description="Fecha de inicio en formato YYYY-MM-DD"),
    fecha_fin: date = Query(..., description="Fecha de fin en formato YYYY-MM-DD"),
    db: Session = Depends(get_db)
):
    query = f"""
        SELECT 
            TO_CHAR(fecha_salida, 'YYYY-MM') AS mes,
            COUNT(*) AS "Total de productos por mes"
        FROM 
            productos
        WHERE 
            fecha_salida BETWEEN :fecha_inicio AND :fecha_fin
        GROUP BY 
            mes
        ORDER BY 
            mes;
    """
    result = db.execute(query, {"fecha_inicio": fecha_inicio, "fecha_fin": fecha_fin}).all()
    return result