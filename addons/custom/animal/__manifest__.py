# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Demo_Animal',
    'version': '1.0',
    'summary': 'Demo Animal',
    'sequence': 10,
    'depends': ['sale'],
    'data': [
        'views/demo_animal.xml',
        'views/menu.xml',
        'views/animal_sale.xml'
    ],
    'demo': [
    ],
    'installable': True,
    'application': True,
    'auto_install': True
}
