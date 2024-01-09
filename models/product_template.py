# -*- coding: utf-8 -*-
import base64

import requests
from odoo import SUPERUSER_ID, api, models


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    def get_products(self):
        response = requests.get('https://dummyjson.com/products')
        data = response.json()
        products = data['products']  # Accede a la lista de productos
        return products

    def load_products(self):
        products = self.get_products()
        for product in products:
            image_url = product['images'][0] if product['images'] else None
            if image_url:
                response = requests.get(image_url)
                image_content = response.content
                image_base64 = base64.b64encode(image_content).decode('utf-8')
                self.env['product.template'].sudo().with_context(detailed_type='product').create(
                    {
                        'name': product['title'],
                        'list_price': product['price'],
                        'image_1920': image_base64,
                        'default_code': product['id'],
                    }
                )
