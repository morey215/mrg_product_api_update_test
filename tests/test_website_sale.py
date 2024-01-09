from odoo.tests.common import TransactionCase
from unittest.mock import patch, MagicMock

# Pruebas para el método get_products
class TestProductTemplateGetProducts(TransactionCase):

    # Prueba exitosa: Mockeando la respuesta de la API
    def test_get_products(self):
        # Inicializa el modelo de producto
        product_template = self.env['product.template']

        # Mockea la función 'requests.get' para retornar un JSON específico
        with patch('requests.get') as mock_get:
            mock_get.return_value.json.return_value = {'products': [{'title': 'Product1', 'price': 10, 'images': ['image_url'], 'id': '123'}]}

            # Llama al método que queremos probar
            products = product_template.get_products()

            # Afirmaciones sobre el resultado esperado
            self.assertTrue(isinstance(products, list))
