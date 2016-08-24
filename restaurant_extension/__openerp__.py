# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Restaurant Extension',
    'summary': 'Allow to transfer/ merge/ split table; Allow to connect directly to printer by using Order function',
    'version': '1.0',
    'category': 'Point of Sale',
    'description': """
    """,
    'author': "Hanel Software Solutions",
    'website': 'http://www.hanelsoft.vn/',
    'depends': ['point_of_sale'],
    'data': [
        'restaurant_view.xml',
        'security/ir.model.access.csv',
        'views/templates.xml',
    ],
    'qweb':[
        'static/src/xml/multiprint.xml',
        'static/src/xml/splitbill.xml',
        'static/src/xml/printbill.xml',
        'static/src/xml/notes.xml',
        'static/src/xml/floors.xml',
    ],
    'demo': [
        'restaurant_demo.xml',
    ],
    'installable': True,
    'auto_install': False,
    'price': 39.99,
    'currency': 'EUR',
}