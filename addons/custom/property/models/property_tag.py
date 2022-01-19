from odoo import models, fields, api

"""
create property tag
"""


class PropertyTag(models.Model):
    _name = 'demo.property.tag'
    _order = 'name desc'

    name = fields.Char(string='Name Tag')
    color = fields.Integer(string='Color')

    _sql_constraints = [
        ('property_tag_unique', 'Unique(name)',
         'Property Tag must be Unique')
    ]

    @api.model
    def create(self, vals_list):
        res = super(PropertyTag, self).create(vals_list)
        return res
