# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from odoo.exceptions import UserError


class ResConfigSettings(models.TransientModel):

    _inherit = 'res.config.settings'

    trial_period = fields.Integer(string='Trial period (days)', default=15)
    db_expiration_time = fields.Integer(string='Database expiration time (hours)', default=3)
    instance_removal_period = fields.Integer(string='Instance removal period  (days)', default=15)

