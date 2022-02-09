# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Demo_Property',
    'version': '1.0',
    'summary': 'Demo Property',
    'sequence': 10,
    'depends': [
        'mail'
    ],
    'data': [
        'views/menu.xml',
        'views/demo_property.xml',
        'security/ir.model.access.csv',
        'security/property_security.xml',
    ],
    'demo': [
    ],
    'installable': True,
    'application': True,
    'auto_install': True
}
