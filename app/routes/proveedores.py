from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


@router.get("/proveedores", response_class=HTMLResponse)
def proveedores_index(request: Request):
    return templates.TemplateResponse(
        request,
        "proveedores/index.html",
        {}
    )