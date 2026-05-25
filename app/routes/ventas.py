from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


@router.get("/ventas", response_class=HTMLResponse)
def ventas_index(request: Request):
    return templates.TemplateResponse(
        request,
        "ventas/index.html",
        {}
    )


@router.get("/ventas/caja", response_class=HTMLResponse)
def ventas_caja(request: Request):
    return templates.TemplateResponse(
        request,
        "ventas/caja.html",
        {}
    )


@router.get("/ventas/productos-caja", response_class=HTMLResponse)
def productos_caja(request: Request):
    return templates.TemplateResponse(
        request,
        "ventas/productos_caja.html",
        {}
    )