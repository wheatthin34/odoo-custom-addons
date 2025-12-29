# -*- coding: utf-8 -*-
{
    'name': "Library Management",

    'summary': "Manage Library books and members",

    'description': """
        Library Management System
        =========================
        * Manage books
        * Track borrowing
        * Member management
    """,

    'author': "Matt Wheatley",
    'website': "https://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/library_book_views.xml',
        'views/library_menu.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}

