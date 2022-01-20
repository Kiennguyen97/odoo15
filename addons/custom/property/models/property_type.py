from odoo import models, fields, api

"""
create property type
"""


class PropertyType(models.Model):
    _name = "demo.property.type"
    _order = 'name desc'

    name = fields.Char(string='Title', required=True)
    sequence = fields.Integer('Sequence', default=1, help="Used to order stages. Lower is better.")

    property_ids = fields.One2many(comodel_name='demo.property', inverse_name='property_type_id', string='Property IDs')

    offer_ids = fields.One2many('demo.property.offer', 'property_type_id', 'Offers', required=True)
    offer_count = fields.Integer(compute='_compute_offer_count', string='Offer Count')
    offer_count_accepted = fields.Integer(compute='_compute_offer_count_accepted', string='Offer Count')
    offer_count_refuse = fields.Integer(compute='_compute_offer_count_refuse', string='Offer Count')

    _sql_constraints = [
        ('property_type_unique', 'Unique(name)',
         'Property Type must be Unique')
    ]

    @api.model
    def create(self, vals_list):
        res = super(PropertyType, self).create(vals_list)
        return res

    @api.depends('offer_ids.property_type_id')
    def _compute_offer_count(self):
        for property_type in self:
            property_type.offer_count = len(property_type.offer_ids)

    def _compute_offer_count_accepted(self):
        for property_type in self:
            property_type.offer_count_accepted = len(property_type.offer_ids.filtered(lambda offer: offer.status == 'accepted'))

    def _compute_offer_count_refuse(self):
        for property_type in self:
            property_type.offer_count_refuse = len(property_type.offer_ids.filtered(lambda offer: offer.status == 'refuse'))

    def action_view_offer_accepted(self):
        return self.action_view_offers('accepted')

    def action_view_offer_refuse(self):
        return self.action_view_offers('refuse')

    def action_view_offers(self, view_filter=False):
        if view_filter:
            offers = self.offer_ids.filtered(lambda offer: offer.status == view_filter)
        else:
            offers = self.env['demo.property.offer'].search([('property_type_id', '=', self.id)], offset=0)

        model_name = 'action_view_offers_'+view_filter
        return {
            'name': model_name,
            'type': 'ir.actions.act_window',
            'view_mode': 'tree,form',
            'res_model': 'demo.property.offer',
            'domain': [('id', 'in', offers.ids ), ]
        }