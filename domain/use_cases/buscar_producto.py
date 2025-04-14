from domain.models.entities.product_entities import Product as ProductoDB
from ..services.producto_service import ProductoService
from sqlalchemy.orm import Session
from fastapi import HTTPException

def ejecutar_busqueda(nombre: str, barcode: str, service: ProductoService) -> list[ProductoDB]:
    if not nombre and not barcode:
        raise HTTPException(status_code=400, detail="Se requiere al menos un parámetro de búsqueda: nombre o código de barras.")
    
    resultados = service.buscar_productos(nombre, barcode)

    if not resultados:
        raise HTTPException(status_code=404, detail="No se encontraron productos que coincidan con los criterios de búsqueda.")
    
    return resultados