from odoo import models, fields, api
from datetime import date, timedelta


class LibraryMember(models.Model):
    """Model for library members/borrowers"""
    _name = 'library.member'
    _description = 'Library Member'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'name'
    _order = 'membership_number desc'

    # Basic Information
    name = fields.Char(
        string='Member Name',
        required=True,
        tracking=True,
        help="Full name of the library member"
    )
    
    photo = fields.Binary(
        string='Photo',
        help="Member photo for identification"
    )
    
    # Contact Information
    email = fields.Char(
        string='Email',
        help="Primary email address"
    )
    
    phone = fields.Char(
        string='Phone',
        help="Primary phone number"
    )
    
    mobile = fields.Char(
        string='Mobile',
        help="Mobile phone number"
    )
    
    address = fields.Text(
        string='Address',
        help="Full residential address"
    )
    
    # Membership Details
    membership_number = fields.Char(
        string='Membership Number',
        required=True,
        copy=False,
        readonly=True,
        index=True,
        default=lambda self: 'New',
        help="Auto-generated unique membership number"
    )
    
    status = fields.Selection([
        ('active', 'Active'),
        ('suspended', 'Suspended'),
        ('expired', 'Expired'),
    ], string='Status', default='active', required=True, tracking=True,
       help="Current membership status")
    
    joined_date = fields.Date(
        string='Joined Date',
        default=fields.Date.today,
        required=True,
        help="Date when member joined the library"
    )
    
    expiry_date = fields.Date(
        string='Expiry Date',
        help="Membership expiration date"
    )
    
    # Additional Information
    notes = fields.Text(
        string='Internal Notes',
        help="Internal notes about the member"
    )
    
    # Computed Fields
    active = fields.Boolean(
        string='Active',
        default=True,
        help="Uncheck to archive the member"
    )
    
    membership_days_left = fields.Integer(
        string='Days Until Expiry',
        compute='_compute_membership_days_left',
        store=False,
        help="Number of days until membership expires"
    )
    
    is_expired = fields.Boolean(
        string='Is Expired',
        compute='_compute_is_expired',
        store=False,
        help="True if membership has expired"
    )
    
    @api.depends('expiry_date')
    def _compute_membership_days_left(self):
        """Calculate days until membership expires"""
        today = date.today()
        for member in self:
            if member.expiry_date:
                delta = member.expiry_date - today
                member.membership_days_left = delta.days
            else:
                member.membership_days_left = 0
    
    @api.depends('expiry_date', 'status')
    def _compute_is_expired(self):
        """Check if membership has expired"""
        today = date.today()
        for member in self:
            if member.expiry_date:
                member.is_expired = member.expiry_date < today
            else:
                member.is_expired = False
    
    @api.model
    def create(self, vals):
        """Override create to generate membership number"""
        if vals.get('membership_number', 'New') == 'New':
            vals['membership_number'] = self.env['ir.sequence'].next_by_code('library.member.sequence') or 'New'
        return super(LibraryMember, self).create(vals)
    
    def action_suspend(self):
        """Suspend the membership"""
        self.write({'status': 'suspended'})
        return True
    
    def action_activate(self):
        """Activate the membership"""
        self.write({'status': 'active'})
        return True
    
    def action_mark_expired(self):
        """Mark membership as expired"""
        self.write({'status': 'expired'})
        return True