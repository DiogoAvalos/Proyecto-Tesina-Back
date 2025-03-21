from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .pais.router import pais
from .tipodocumento.router import tipodoc
from .unidadventa.router import unidad_venta
from .familia.router import familia
from .marca.router import marca
from .categoria.router import categoria
from .proveedor.router import proveedor
from .db import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(pais)
app.include_router(tipodoc)
app.include_router(unidad_venta)
app.include_router(familia)
app.include_router(marca)
app.include_router(categoria)
app.include_router(proveedor)
