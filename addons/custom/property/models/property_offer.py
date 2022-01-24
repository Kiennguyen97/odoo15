from odoo import models, fields, api, exceptions
from odoo.tools import float_compare
import datetime

"""
create property offer
"""


class PropertyOffer(models.Model):
    _name = 'demo.property.offer'
    _order = 'price desc, sequence'

    price = fields.Float(string='Price', required=True)
    sequence = fields.Integer('Sequence', default=1, help="Used to order stages. Lower is better.")
    status = fields.Selection([
        ('accepted', 'Accepted'),
        ('confirm', 'Confirm'),
        ('refuse', 'Refuse')
    ], string='Status', readonly=True)
    partner_id = fields.Many2one('res.partner', required=True, string='Partner')
    property_id = fields.Many2one('demo.property', required=True, ondelete='cascade', string='Property')
    property_type_id = fields.Many2one('demo.property.type', string='Property Type',
                                       related='property_id.property_type_id', store=True)

    validity = fields.Integer(string='Validity (days)', default=7)
    deadline = fields.Date(string='Deadline', compute='_compute_deadline', inverse='_inverse_deadline')

    @api.model
    def create(self, vals_list):
        max_price = self.get_max_offer(vals_list['property_id'])
        if vals_list['price'] < max_price:
            raise exceptions.ValidationError("The offer must be than {} !".format(max_price))

        res = super(PropertyOffer, self).create(vals_list)
        if res.property_id.state == 'new' or res.property_id.state == False:
            res.property_id.state = 'processing'
        return res

    @api.depends('create_date', 'validity')
    def _compute_deadline(self):
        offers = self.filtered(lambda l: l.validity and l.create_date)
        for offer in offers:
            if offer.validity < 0:
                offer.validity = 0
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

    def refuse_offer(self):
        if self.status == 'refuse':
            return True
        if self.status == 'accepted':
            self.property_id.selling_price = 0
            self.property_id.buyer_id = False
        self.status = 'refuse'

    def accepted_offer(self):
        # offers = self.property_id.mapped('offer_ids')
        if self.status == 'accepted':
            return True
        offers = self.property_id.offer_ids
        for offer in offers:
            offer.status = 'refuse'
        self.status = 'accepted'
        self.property_id.selling_price = self.price
        self.property_id.buyer_id = self.partner_id

    @api.constrains('status')
    def check_price_expected(self):
        for record in self:
            if self.status == 'refuse':
                return True
            # Always use the float_compare() and float_is_zero() methods when working with floats
            if float_compare(record.property_id.expected_price * 90 / 100, record.price, precision_digits=2) == 1:
                raise exceptions.ValidationError(
                    "It will impossible to accept an offer lower than 90% of the expected price.")

    def get_max_offer(self, id):
        property = self.env['demo.property'].search([('id', '=', id)])
        best_offer = 0
        for price in property.offer_ids.mapped('price'):
            if best_offer < price:
                best_offer = price
        return best_offer;