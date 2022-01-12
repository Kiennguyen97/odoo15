from odoo import models, fields, api

"""
create property type
"""
class PropertyType(models.Model):

    _name = "demo.property.type"

    name = fields.Char(name="Name", required=True)


    @api.model
    def create(self, vals_list):
        res = super(PropertyType, self).create(vals_list)
        return res

