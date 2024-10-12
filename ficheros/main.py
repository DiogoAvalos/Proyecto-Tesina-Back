from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .pais.router import router
from .tipodocumento.router import tipodoc
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

app.include_router(router)
app.include_router(tipodoc)