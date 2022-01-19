from odoo import models, fields, api, exceptions

"""
create property 
"""


class Property(models.Model):
    _name = "demo.property"

    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(name="Name", required=True)
    state = fields.Selection([
        ('new', 'New'),
        ('canceled', 'Canceled'),
        ('processing', 'Processing'),
        ('sold', 'Sold')
    ], readonly=True, string='Status', default='new')
    sale_man_id = fields.Many2one('res.users', string='Salesperson', index=True, required=True, tracking=True,
                                  default=lambda self: self.env.user)
    buyer_id = fields.Many2one('res.partner', string='Buyer')
    property_type_id = fields.Many2one('demo.property.type', string='Property Type', required=True)
    tag_ids = fields.Many2many('demo.property.tag', string='Property Tag')
    offer_ids = fields.One2many('demo.property.offer', 'property_id', 'Offers', required=True)

    post_code = fields.Char(string='Post Code')
    is_good_choice = fields.Boolean(string='Good Choice')
    available_from = fields.Date(string='Available Form')
    expected_price = fields.Float(string='Expected Price')
    best_offer = fields.Float(compute='_compute_best_offer', string='Best Offer')
    selling_price = fields.Float(string='Selling Price', readonly=True, default=0)

    description_property = fields.Text(string='Description')
    bedrooms = fields.Integer(string='Bedrooms')
    live_area = fields.Integer(string='Live Area (sqm)')
    facades = fields.Integer(string='Facades')
    garage = fields.Boolean(string='Garage')
    garden = fields.Boolean(string='Garden')
    garden_area = fields.Integer(string='Garden Area (sqm)')
    garden_orientation = fields.Selection([
        ('east', 'East'),
        ('west', 'West'),
        ('south', 'South'),
        ('north', 'North')
    ], string='Garden Orientation')
    total_area = fields.Integer(string='Total Area (sqm)', compute='_compute_total_area')

    signature = fields.Image('Signature', help='Signature received through the portal.', copy=False, attachment=True,
                             max_width=1024, max_height=1024)
    signed_by = fields.Char('Signed By', help='Name of the person that signed the SO.', copy=False)
    signed_on = fields.Datetime('Signed On', help='Date of the signature.', copy=False)

    @api.model
    def create(self, vals_list):
        res = super(Property, self).create(vals_list)
        return res

    @api.depends('offer_ids.price')
    def _compute_best_offer(self):
        for record in self:
            best_offer = 0
            # for offer_obj in record.offer_ids:
            #     if best_offer < offer_obj.price:
            #         best_offer = offer_obj.price
            # record.best_offer = best_offer
            for price in record.offer_ids.mapped('price'):
                if best_offer < price:
                    best_offer = price
            record.best_offer = best_offer

    @api.depends('garden_area', 'live_area')
    def _compute_total_area(self):
        for record in self:
            record.total_area = record.live_area + record.garden_area

    @api.onchange('garden')
    def have_garden(self):
        for record in self:
            if record.garden:
                record.garden_orientation = 'north'
                record.garden_area = 10
            else:
                record.garden_orientation = False
                record.garden_area = 0

    def sold_property(self):
        if self.state == 'canceled':
            raise exceptions.ValidationError("Canceled property can't sold !!!")
            return true
        self.state = 'sold'

    def cancel_property(self):
        self.state = 'canceled'

    def un_cancel_property(self):
        self.state = 'processing'

    def un_sold(self):
        self.state = 'processing'


