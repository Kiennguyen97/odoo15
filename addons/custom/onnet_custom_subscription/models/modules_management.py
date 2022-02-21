# -*- coding: utf-8 -*-
from odoo import api, fields, models

class ModulesManagement(models.Model):
    _name = "modules.management"
    _description = "Modules Management"
    _rec_name = 'module_name'

    module_name = fields.Char('Module Name', required=True)
    thumbnail_image = fields.Binary("Thumbnail Image", attachment=True, help="Thumbnail Image")