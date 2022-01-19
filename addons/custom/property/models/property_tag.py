from odoo import models, fields, api

"""
create property tag
"""


class PropertyTag(models.Model):
    _name = 'demo.property.tag'

    name = fields.Char(string='Name Tag')
    type_tag = fields.Char(string='Type Tag')

    _sql_constraints = [
        ('property_tag_unique', 'Unique(name)',
         'Property Tag must be Unique')
    ]

    @api.model
    def create(self, vals_list):
        res = super(PropertyTag, self).create(vals_list)
        return res
