from odoo import models, fields, api



class DemoAnimalTest(models.Model):
    _name = "demo.animal.test"

    name = fields.Char(name="Name", required=True)
    description = fields.Text(name="Description", required=False)

    @api.model
    def create(self, vals_list):
        res = super(DemoAnimalTest, self).create(vals_list)
        return res

    def write(self, vals):
        res = super(DemoAnimalTest, self).write(vals)
        return res

