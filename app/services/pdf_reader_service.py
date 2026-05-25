import pdfplumber


def extraer_texto_pdf(ruta_pdf: str) -> str:
    texto_total = ""

    with pdfplumber.open(ruta_pdf) as pdf:
        for pagina in pdf.pages:
            texto = pagina.extract_text()

            if texto:
                texto_total += texto + "\n"

    return texto_total.strip()