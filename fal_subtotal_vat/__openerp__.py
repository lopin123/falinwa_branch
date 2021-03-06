# -*- coding: utf-8 -*-
{
    "name": "GEN-14_Subtotal with VAT",
    "version": "1.0",
    'author': 'Falinwa Hans',
    "description": """
    Module to add subtotal with vat both on purchases and sales
    """,
    "depends" : ['base','purchase','sale','account','purchase_discount'],
    'init_xml': [],
    'update_xml': [
        'purchase_view.xml',
        'sale_view.xml',
        'invoice_view.xml',
    ],
    'css': [],
    'installable': True,
    'active': False,
    'application' : False,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: