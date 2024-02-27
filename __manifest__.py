# -*- coding: utf-8 -*-
{
    'name': "Carga de Productos desde API Externa",
    'summary': """
        Testeo de producto desde una api""",
    'description': """
        Testeo de productos cargados desde una api externa
    """,
    'author': "Mario Roberto Gómez",
    'website': "https://mrgomezsv.github.io/",
    'category': 'Website/Website',
    'version': '0.1',
    'depends': ['website', 'stock'],
    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/product_template.xml',
    ],
}
