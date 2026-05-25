from sqlalchemy import Column, Integer, String, Numeric, Date
from app.database import Base

class Factura(Base):
    __tablename__ = "facturas"

    id = Column(Integer, primary_key=True, index=True)

    nombre = Column(String(150), nullable=False)
    rut_empresa = Column(String(20), nullable=False)

    numero_factura = Column(String(50), nullable=False)
    fecha_emision = Column(Date, nullable=False)
    fecha_vencimiento = Column(Date, nullable=True)

    estado = Column(String(30), nullable=False, default="pendiente")

    monto_neto = Column(Numeric(12, 2), nullable=False)

    item_factura = Column(String(300), nullable=True)

    archivo_path = Column(String(300), nullable=True)