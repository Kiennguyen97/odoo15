# -*- coding: utf-8 -*-
from odoo import api, fields, models

class SubscriptionPlansManagement(models.Model):
    _inherit = 'product.template'
    _description = "Subscription Plans Management"
    _order = "id desc"

    detailed_type = fields.Selection([
        ('consu', 'Consumable'),
        ('service', 'Service')], string='Product Type', default='service', required=True,
        help='A storable product is a product for which you manage stock. The Inventory app has to be installed.\n'
             'A consumable product is a product for which stock is not managed.\n'
             'A service is a non-material product you provide.')
    is_subscription_plans = fields.Boolean(string='Subscription Plans', default=False)
    customer_segment = fields.Many2one(comodel_name='customer.segment.management',  string='Customer Segment',  required=False,
                                                    delegate=True, auto_join=True, index=True, ondelete="cascade")
    tab_module = fields.One2many('tab.module', 'sub_plans', string='Tab Module', ondelete="cascade" )