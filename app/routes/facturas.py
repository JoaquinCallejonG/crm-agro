import os

from fastapi import APIRouter, Request, UploadFile, File
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from app.services.pdf_reader_service import extraer_texto_pdf
from app.services.factura_parser_service import parsear_factura

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

# Carpeta donde se guardan PDFs
UPLOAD_DIR = "app/uploads/facturas"
os.makedirs(UPLOAD_DIR, exist_ok=True)


# =========================================================
# VISTA PRINCIPAL DEL MÓDULO FACTURAS
# =========================================================
@router.get("/facturas", response_class=HTMLResponse)
def facturas_index(request: Request):
    return templates.TemplateResponse(
        request,
        "facturas/index.html",
        {
            "mensaje": None,
            "error": None,
            "datos": None
        }
    )


# =========================================================
# VISTA CARGA MANUAL
# =========================================================
@router.get("/facturas/carga", response_class=HTMLResponse)
def facturas_carga(request: Request):
    return templates.TemplateResponse(
        request,
        "facturas/carga.html",
        {}
    )


# =========================================================
# SUBIDA + PROCESAMIENTO PDF
# =========================================================
@router.post("/facturas/upload", response_class=HTMLResponse)
async def facturas_upload(request: Request, archivo: UploadFile = File(...)):

    # Validación 1
    if not archivo.filename:
        return templates.TemplateResponse(
            request,
            "facturas/index.html",
            {"error": "No se seleccionó archivo", "datos": None}
        )

    # Validación 2
    if not archivo.filename.lower().endswith(".pdf"):
        return templates.TemplateResponse(
            request,
            "facturas/index.html",
            {"error": "El archivo debe ser PDF", "datos": None}
        )

    # Guardar archivo
    ruta_archivo = os.path.join(UPLOAD_DIR, archivo.filename)

    contenido = await archivo.read()

    with open(ruta_archivo, "wb") as f:
        f.write(contenido)

    # 🔥 EXTRAER TEXTO
    texto = extraer_texto_pdf(ruta_archivo)

    # 🔥 PARSEAR DATOS
    datos = parsear_factura(texto)

    # 🔥 DEVOLVER A LA VISTA
    return templates.TemplateResponse(
        request,
        "facturas/index.html",
        {
            "mensaje": "Factura procesada correctamente",
            "error": None,
            "datos": datos
        }
    )


# =========================================================
# VISTA REVISIÓN
# =========================================================
@router.get("/facturas/revision", response_class=HTMLResponse)
def facturas_revision(request: Request):
    return templates.TemplateResponse(
        request,
        "facturas/revision.html",
        {}
    )


# =========================================================
# VISTA APROBACIÓN
# =========================================================
@router.get("/facturas/aprobacion", response_class=HTMLResponse)
def facturas_aprobacion(request: Request):
    return templates.TemplateResponse(
        request,
        "facturas/aprobacion.html",
        {}
    )