from fastapi import APIRouter, Depends, Query, HTTPException, status
from domain.schemas.producto_response import ProductoResponse
from domain.services.producto_service import ProductoService
from sqlalchemy.orm import Session
from config import get_db
from infrastructure.repository.producto_repository import ProductoRepository
from app.helpers.get_producto_service import get_producto_service
from typing import List

router = APIRouter(prefix="/productos", tags=["productos"])

""" def get_producto_service(db: Session = Depends(get_db)) -> ProductoService:
    try:
        repo = ProductoRepository(db)
        return ProductoService(repo)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"No se pudo inicializar el servicio de productos: {str(e)}"
        ) """

@router.get("/buscar", response_model=List[ProductoResponse])
def buscar_producto(
    nombre: str = Query(None, description="Nombre del producto"),
    barcode: str = Query(None, description="Código de barras del producto"),
    service: ProductoService = Depends(get_producto_service)
):
    try:
        return service.buscar_productos(nombre, barcode)
    except ValueError as ve:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Error de validación: {str(ve)}"
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error interno del servidor: {str(e)}"
        )
