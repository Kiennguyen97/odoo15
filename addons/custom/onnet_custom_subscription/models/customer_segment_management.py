# -*- coding: utf-8 -*-
from odoo import api, fields, models

class CustomerSegmentManagement(models.Model):
    _name = "customer.segment.management"
    _description = "Customer Segment Management"
    _rec_name = 'customer_segment_name'

    customer_segment_name = fields.Char('Module Name')
    subscription_plan = fields.One2many('product.template', 'customer_segment', string="Subscription Plan", ondelete="cascade")