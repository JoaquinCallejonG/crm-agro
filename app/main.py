from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.database import engine, Base
from app.models.factura import Factura

from app.routes import views
from app.routes import facturas
from app.routes import ventas
from app.routes import proveedores

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.mount("/static", StaticFiles(directory="app/static"), name="static")
app.include_router(views.router)
app.include_router(facturas.router)
app.include_router(ventas.router)
app.include_router(proveedores.router)