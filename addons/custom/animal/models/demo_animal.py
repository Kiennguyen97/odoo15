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
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirm', 'Confirm'),
        ('block', 'Block')
    ],)

    @api.model
    def create(self, vals_list):
        res = super(DemoAnimal, self).create(vals_list)
        return res

    def write(self, vals):
        res = super(DemoAnimal, self).write(vals)
        return res

    # write lại data
    def button_update_to_dog(self):
        self.write({'name': 'DOG'})

    # thay đổi state hiện tại thành block
    def change_block(self):
        self.state = 'block'

    # Mỗi khi Name thay đổi thì state sẽ chuyển về confirm
    @api.constrains('name')
    def change_state(self):
        self.state = 'confirm'

    # copy record hiện tại nhưng thay name = harrypotter
    def duplicate_animal(self):
        self.copy({'name': 'HarryPotter'})

    # Tạo create default name sẽ là Naruto
    def default_get(self, fields_list):
        res = super(DemoAnimal, self).default_get(fields_list)
        res['name'] = 'Naruto'
        return res

    # Create new record voi name
    def name_create(self, name):
        res =  super(DemoAnimal, self).name_create(name)
        return res

    def create_new_ninja(self):
        self.name_create('Sasuke')



