from app.services.pdf_reader_service import extraer_texto_pdf
import os

# Carpeta donde están tus PDFs
carpeta = "app/uploads/facturas"

# Buscar el primer PDF disponible
archivos = os.listdir(carpeta)

pdfs = [f for f in archivos if f.endswith(".pdf")]

if not pdfs:
    print("❌ No hay PDFs en la carpeta")
    exit()

archivo_pdf = pdfs[0]
ruta_pdf = os.path.join(carpeta, archivo_pdf)

print(f"\n📄 Leyendo: {archivo_pdf}\n")

# 🔥 EXTRAER TEXTO
texto = extraer_texto_pdf(ruta_pdf)

# Mostrar en consola (preview)
print("\n===== TEXTO EXTRAÍDO =====\n")
print(texto[:2000])
print("\n==========================\n")

# 💾 Guardar en archivo .txt
ruta_txt = ruta_pdf.replace(".pdf", ".txt")

with open(ruta_txt, "w", encoding="utf-8") as f:
    f.write(texto)

print(f"✅ Texto guardado en: {ruta_txt}")