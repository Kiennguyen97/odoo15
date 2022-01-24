from odoo import models, fields, api

"""
User property

"""


class PropertyUser(models.Model):
    _inherit = 'res.users'

    property_ids = fields.One2many('demo.property', 'sale_man_id', 'Properties')
