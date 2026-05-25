from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


@router.get("/login", response_class=HTMLResponse)
def login_view(request: Request):
    return templates.TemplateResponse(
        request,
        "login.html",
        {"error": None}
    )


@router.post("/login", response_class=HTMLResponse)
def login_submit(
    request: Request,
    email: str = Form(...),
    password: str = Form(...)
):
    if email == "admin" and password == "1234":
        return RedirectResponse(url="/dashboard", status_code=303)

    return templates.TemplateResponse(
        request,
        "login.html",
        {"error": "Usuario o contraseña incorrectos"}
    )


@router.get("/dashboard", response_class=HTMLResponse)
def dashboard_view(request: Request):
    return templates.TemplateResponse(
        request,
        "dashboard.html",
        {}
    )


@router.get("/facturas", response_class=HTMLResponse)
def facturas_view(request: Request):
    return templates.TemplateResponse(
        request,
        "facturas/index.html",
        {}
    )


