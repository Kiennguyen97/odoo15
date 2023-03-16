from odoo import models, fields


class BaoSonEmployee(models.Model):
    _inherit = "hr.employee"

    # category_ids = fields.One2many('hr.employee.category', 'employee_id', string='Tags')




