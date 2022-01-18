from odoo import models, fields, api
import datetime

"""
create property offer
"""


class PropertyOffer(models.Model):
    _name = 'demo.property.offer'

    price = fields.Float(string='Price', required=True)
    status = fields.Selection([
        ('accepted', 'Accepted'),
        ('confirm', 'Confirm')
    ], string='Status', default='accepted')
    partner_id = fields.Many2one('res.partner', required=True, string='Partner')
    property_id = fields.Many2one('demo.property', required=True, ondelete='cascade', string='Property')

    validity = fields.Integer(string='Validity (days)', default=7)
    deadline = fields.Date(string='Deadline', compute='_compute_deadline', inverse='_inverse_deadline')

    @api.model
    def create(self, vals_list):
        res = super(PropertyOffer, self).create(vals_list)
        return res

    @api.depends('create_date', 'validity')
    def _compute_deadline(self):
        offers = self.filtered(lambda l: l.validity and l.create_date)
        for offer in offers:
            if offer.validity < 0: offer.validity = 0
            create_date = offer.create_date
            deadline = create_date + datetime.timedelta(days=offer.validity)
            offer.deadline = deadline
            # date_create = fields.Datetime.from_string(offer.create_date).replace(microsecond=0)

    def _inverse_deadline(self):
        offers = self.filtered(lambda l: l.deadline and l.create_date)
        for record in offers:
            # date_format = "%m/%d/%Y"
            # deadline = record.deadline
            # create_date = record.create_date
            #
            # # string_time = deadline.strftime(date_format)
            # # deadline = datetime.datetime.strptime(string_time, date_format).timestamp()
            # # current_date = datetime.date.today()
            # # string_time = current_date.strftime(date_format)
            # # current_date = datetime.datetime.strptime(string_time, date_format).timestamp()
            #

            create_date = fields.Datetime.from_string(record.create_date).replace(microsecond=0)
            deadline = fields.Datetime.from_string(record.deadline)
            if deadline < create_date:
                record.validity = 0
            else:
                validity = deadline - create_date
                record.validity = validity.days

