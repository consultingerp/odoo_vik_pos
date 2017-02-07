# -*- coding: utf-8 -*-

{
    'name': 'POS Sort',
    'version': '1.0',
    'category': 'Point of Sale',
    'sequence': 6,
    'summary': 'POS Sort method for the Point of Sale ',
    'description': """

=======================

This module adds POS sorf by code or name features to the Point of Sale:


""",
    'author': 'Viktor Vorobjov',
    'depends': ['point_of_sale'],
    
    'license': 'LGPL-3',
    'website': 'https://straga.github.io',
    'support': 'vostraga@gmail.com',

    'data': [
        'views/templates.xml',
        'views/views.xml',
       
    ],
    'qweb':[

        'static/src/xml/sort.xml',
    ],
    'installable': True,
    'auto_install': False,
}

