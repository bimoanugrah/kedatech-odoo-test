# -*- coding: utf-8 -*-
{
    'name': "Material Registration",

    'summary': """
        Modul material""",

    'description': """
        Modul material
    """,

    'author': "Bimo Anugrah Prasetyo",
    'website': "http://www.yourcompany.com",


    'category': 'test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail'],

    'test': [
        'tests/supplier_test.py',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/material_supplier.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
