from odoo import models, fields, api



class DemoAnimal(models.Model):
    _name = "demo.animal"

    name = fields.Char(name="Name", required=True)
    description = fields.Text(name="Description", required=False)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ], required=False, default='male')
    age = fields.Integer(string='Age')

    @api.model
    def create(self, vals_list):
        res = super(DemoAnimal, self).create(vals_list)
        return res

    def write(self, vals):
        res = super(DemoAnimal, self).write(vals)
        return res

    def button_update_to_dog(self):
        self.write({'name': 'DOG'})
