# -*- coding: utf-8 -*-

from re import T
from odoo import models, fields, api

class LibraryBook(models.Model):
    """Model for library books"""
    _name = 'library.book'
    _description = 'Library Book'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'name'

    # Basic Information
    name = fields.Char(string='Title', required=True, tracking=True)
    isbn = fields.Char(string='ISBN', copy=False)
    author = fields.Char(string='Author', required=True, tracking=True)
    publisher = fields.Char(string='Publisher')
    publish_date = fields.Date(string='Publish Date')
    pages = fields.Integer(string='Number of Pages')

    #Additional Information
    description = fields.Text(string='Description')
    cover_image = fields.Binary(string='Cover Image')

    # Rating Field
    rating = fields.Selection([
        ('0', 'No Rating'),
        ('1', '⭐'),
        ('2', '⭐⭐'),
        ('3', '⭐⭐⭐'),
        ('4', '⭐⭐⭐⭐'),
        ('5', '⭐⭐⭐⭐⭐'),
    ], string='Rating', default='0', help='Book rating from readers (1-5 stars)')
    
    # Status
    state = fields.Selection([
        ('available', 'Available'),
        ('borrowed', 'Borrowed'),
        ('lost', 'Lost'),
    ], string='Status', default='available', tracking=True)
    
    # Pricing
    cost_price = fields.Float(string='Cost Price')
    rental_price = fields.Float(string='Rental Price per Day')