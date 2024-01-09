# -*- coding: utf-8 -*-
{
    'name': "Carga de Productos",
    'summary': """
        Testeo de producto desde una api""",
    'description': """
        Testeo de productos cargados desde una api externa
    """,
    'author': "Sistemas en linea",
    'website': "https://sistemas-en-linea.com/",
    'category': 'Website/Website',
    'version': '0.1',
    'depends': ['website', 'product'],
    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/product_template.xml',
    ],
}
