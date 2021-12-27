from odoo import models, fields


class AcademyCourse(models.Model):
    _name = "academy.course"
    _inherit = 'res.partner'  #kế thừa

    name = fields.Char()
    start_date = fields.Date(string="Start Date", default=fields.Date.today())

    host_id = fields.Many2one('res.partner')