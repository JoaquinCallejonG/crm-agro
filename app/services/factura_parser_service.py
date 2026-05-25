import re


def limpiar_monto(valor: str):
    if not valor:
        return None

    valor = valor.replace(".", "")
    valor = valor.replace(",", ".")

    try:
        return float(valor)
    except ValueError:
        return None


def buscar_patron(patron: str, texto: str):
    resultado = re.search(patron, texto, re.IGNORECASE)

    if resultado:
        return resultado.group(1).strip()

    return None


def parsear_factura(texto: str) -> dict:
    numero_factura = buscar_patron(
        r"(?:N[°º]\s*Factura|Factura\s*N[°º]?|Folio)\s*[:\-]?\s*(\d+)",
        texto
    )

    rut_empresa = buscar_patron(
        r"RUT\s*[:\-]?\s*([\d\.]+-[\dkK])",
        texto
    )

    fecha_emision = buscar_patron(
        r"(?:Fecha\s*Emisi[oó]n|Fecha\s*de\s*Emisi[oó]n)\s*[:\-]?\s*(\d{2}[-/]\d{2}[-/]\d{4})",
        texto
    )

    fecha_vencimiento = buscar_patron(
        r"(?:Fecha\s*Vencimiento|Vencimiento)\s*[:\-]?\s*(\d{2}[-/]\d{2}[-/]\d{4})",
        texto
    )

    monto_neto_texto = buscar_patron(
        r"(?:Monto\s*Neto|Neto)\s*[:\$]?\s*([\d\.\,]+)",
        texto
    )

    monto_neto = limpiar_monto(monto_neto_texto)

    return {
        "numero_factura": numero_factura,
        "rut_empresa": rut_empresa,
        "fecha_emision": fecha_emision,
        "fecha_vencimiento": fecha_vencimiento,
        "monto_neto": monto_neto,
        "texto_extraido": texto[:2000]
    }