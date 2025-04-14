from infrastructure.repository.producto_repository import ProductoRepository
from domain.schemas.producto_response import ProductoResponse as ProductoResponse

class ProductoService:
    def __init__(self, repo: ProductoRepository):
        self.repo = repo

    def buscar_productos(self, nombre: str = None, barcode: str = None) -> list[ProductoResponse]:
        productos = self.repo.get_producto_by_barcode_by_name(nombre, barcode)
        return [ProductoResponse.model_validate(p) for p in productos]