from odoo import models, fields


class AcademyClass(models.Model):
    _name = 'employee'
    _inherit = 'academy.course'

    name = fields.Char(string=('name'))


