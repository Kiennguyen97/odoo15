from odoo import models, fields, api

class AnimalSale(models.Model):
    _inherit = "sale.order"

    sale_description = fields.Char(string='Animal Sale Description')
    date_order = fields.Char(string='Animal Order Date')

