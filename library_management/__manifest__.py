# -*- coding: utf-8 -*-
{
    'name': "Library Management",

    'summary': "Manage Library books and members",

    'description': """
        Library Management System
        =========================
        * Manage books and authors
        * Track borrowing and returns
        * Book ratings
        * Messaging and activities
        * Professional module for library operations
    """,

    'author': "Matt Wheatley",
    'website': "https://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '1.0.1',
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/library_book_views.xml',
        'views/library_menu.xml',
        'data/sequence.xml',
        'views/library_member_views.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}

