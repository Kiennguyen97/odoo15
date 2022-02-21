# -*- coding: utf-8 -*-
from odoo import api, fields, models

class TabModule(models.Model):
    _name = "tab.module"
    _description = "Tab Module"
    _rec_name = 'tab_name'

    tab_name = fields.Char('Module Name', required=True)
    module_management = fields.Many2many('modules.management', 'product_modules_management', 'product_template_id',
                                         'modules_management_id', string='Related Module', ondelete="cascade")
    sub_plans = fields.Many2one('product.template', string='Subscription', invisible=True, ondelete="cascade")