import unittest
from unittest.mock import MagicMock
from domain.services.producto_service import ProductoService
from domain.schemas.producto_response import ProductoResponse

class TestProductoService(unittest.TestCase):
    def setUp(self):
        # Creamos un mock del repositorio
        self.repo_mock = MagicMock()
        self.service = ProductoService(self.repo_mock)

    def test_buscar_productos_devuelve_lista_valida(self):
        # Datos simulados del repositorio
        producto_fake = {
            "id": 1,
            "name": "Pan Bimbo",
            "price": 4500.0,
            "barcode": "1234567890"
        }

        # El mock devuelve una lista de objetos tipo dict o SQLAlchemy-like
        self.repo_mock.get_producto_by_barcode_by_name.return_value = [producto_fake]

        # Ejecutamos el método a probar
        resultado = self.service.buscar_productos("Pan", "1234567890")

        # Verificamos el resultado
        self.assertEqual(len(resultado), 1)
        self.assertIsInstance(resultado[0], ProductoResponse)
        self.assertEqual(resultado[0].name, "Pan Bimbo")

    def test_buscar_productos_sin_resultados(self):
        self.repo_mock.get_producto_by_barcode_by_name.return_value = []
        resultado = self.service.buscar_productos("NoExiste", "000")
        self.assertEqual(resultado, [])

if __name__ == "__main__":
    unittest.main()

