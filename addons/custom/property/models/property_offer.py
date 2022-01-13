from odoo import models, fields, api

"""
create property offer
"""

class PropertyOffer(models.Model):
    _name = 'demo.property.offer'

    price = fields.Float(string='Price')
    status = fields.Selection([
        ('accepted', 'Accepted'),
        ('confirm', 'Confirm')
    ],)
    partner_id = fields.Many2one('res.partner', required=True)
    property_id = fields.Many2one('demo.property', required=True)

    @api.model
    def create(self, vals_list):
        res = super(PropertyOffer, self).create(vals_list)
        return res
