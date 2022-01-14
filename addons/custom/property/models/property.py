from odoo import models, fields, api

"""
create property 
"""

class Property(models.Model):
    _name = "demo.property"

    name = fields.Char(name="Name", required=True)
    sale_man_id = fields.Many2one('res.users', string='Salesperson', index=True, required=True, tracking=True, default=lambda self: self.env.user)
    buyer_id = fields.Many2one('res.partner', string='Buyer', required=True)
    property_type_id = fields.Many2one('demo.property.type', string='Property Type', required=True)

    post_code = fields.Char(string='Post Code')
    is_good_choice = fields.Boolean(string='Good Choice')
    available_from = fields.Date(string='Available Form')
    expected_price = fields.Float(string='Expected Price')
    selling_price = fields.Float(string='Selling Price')
    description_property = fields.Text(string='Description')

    signature = fields.Image('Signature', help='Signature received through the portal.', copy=False, attachment=True,
                             max_width=1024, max_height=1024)
    signed_by = fields.Char('Signed By', help='Name of the person that signed the SO.', copy=False)
    signed_on = fields.Datetime('Signed On', help='Date of the signature.', copy=False)

    tag_ids = fields.Many2many('demo.property.tag', string='Property Tag')
    offer_ids = fields.One2many('demo.property.offer', 'property_id', 'Offers', required=True)


    @api.model
    def create(self, vals_list):
        res = super(Property, self).create(vals_list)
        return res