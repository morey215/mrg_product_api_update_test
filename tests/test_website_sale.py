# Importamos la clase de prueba y algunas utilidades de Odoo
from unittest.mock import MagicMock, patch

from odoo.tests import common


# Creamos nuestra propia clase de prueba y heredamos de common.TransactionCase
class TestProductTemplate(common.TransactionCase):
    # Este método se ejecuta antes de cada prueba
    def setUp(self):
        super(TestProductTemplate, self).setUp()

        # Simulamos la respuesta de la API con 30 productos
        self.mock_response = MagicMock()
        self.mock_response.json.return_value = {
            'products': [
                {'id': i, 'title': f'Producto{i}', 'price': i, 'images': []} for i in range(30)
            ]
        }

        # Parcheamos (simulamos) la función 'requests.get' para que devuelva nuestra respuesta simulada
        self.patcher = patch('requests.get', return_value=self.mock_response)
        self.mock_requests_get = self.patcher.start()

    # Este método se ejecuta después de cada prueba
    def tearDown(self):
        super(TestProductTemplate, self).tearDown()

        # Detenemos el parche para restaurar la funcionalidad original de 'requests.get'
        self.patcher.stop()

    # Este es nuestro caso de prueba
    def test_load_products(self):
        # Llamamos a la función que obtiene y carga productos desde la API
        self.env['product.template'].sudo().load_products()

        # Verificamos que la función 'get_products' fue llamada correctamente
        self.mock_requests_get.assert_called_once_with('https://dummyjson.com/products')

        # Contamos cuántos productos hay en la base de datos
        product_count = self.env['product.template'].search_count([])

        # Verificamos que se hayan creado exactamente 30 productos
        self.assertEqual(product_count, 30)
