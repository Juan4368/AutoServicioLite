from app.cargar_productos import cargar_productos_desde_xml
from infrastructure.repository.producto_repository import ProductoRepository
from domain.schemas.producto_response import ProductoResponse

# Cargar datos desde XML al iniciar
#cargar_productos_desde_xml()
#ProductoRepository()

class test:
    def __init__(self, repo: ProductoRepository):
        self.repo = repo
        productos = self.repo.get_producto_by_barcode_by_name("pan", "12345")
        print (productos)

        #deseo poner un try except para que si no encuentra nada no rompa el programa
        #productos = self.repo.get_producto_by_barcode_by_name("pan", "12345")
        #print (productos)
        #productos = self.repo.get_producto_by_barcode_by_name("pan", "12345")  
        #print (productos)
        #productos = self.repo.get_producto_by_barcode_by_name("pan", "12345")
        #print (productos)
