from odoo import models, fields, api

"""
create property 
"""

class Property(models.Model):
    _name = "demo.property"

    name = fields.Char(name="Name", required=True)
    sale_man_id = fields.Many2one('res.partner', string='Saleman')
    buyer_id = fields.Many2one('res.partner', string='Buyer')
    property_type_id = fields.Many2one('demo.property.type', string='Property Type')

    post_code = fields.Char(string='Post Code')
    is_good_choice = fields.Boolean(string='Good Choice')
    available_from = fields.Date(string='Available Form')
    expected_price = fields.Float(string='Expected Price')
    selling_price = fields.Float(string='Selling Price')
    description_property = fields.Text(string='Description')



    @api.model
    def create(self, vals_list):
        res = super(Property, self).create(vals_list)
        return res