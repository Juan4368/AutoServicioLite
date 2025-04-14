from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from config import get_db
from infrastructure.repository.producto_repository import ProductoRepository
from domain.services.producto_service import ProductoService
from domain.schemas.producto_response import ProductoResponse

def get_producto_service(db: Session = Depends(get_db)) -> ProductoService:
    try:
        repo = ProductoRepository(db)
        return ProductoService(repo)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"No se pudo inicializar el servicio de productos: {str(e)}"
        )
