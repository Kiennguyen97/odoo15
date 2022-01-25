from odoo import models, fields, api, exceptions, Command

"""
Inheritance property 
"""


class EstateProperty(models.Model):
    _inherit = 'demo.property'

    def sold_property(self):
        res = super().sold_property()
        journal = self.env['account.move'].with_context(default_move_type='out_invoice')._get_default_journal()
        vals = {'partner_id': self.id, 'move_type': 'out_invoice', 'journal_id': journal.id,
                    "invoice_line_ids": [
                        (
                            Command.create({
                                "name": "Test",
                                "quantity": "3",
                                "price_unit": "100"
                            })
                        ),
                        (
                            Command.create({
                                "name": "selling",
                                "quantity": "1",
                                "price_unit": float(self.selling_price*6/100)
                            })
                        )
                    ]
                }
        # vals = {'partner_id': self.buyer_id, 'move_type': 'Customer Invoice'}
        self.env['account.move'].create(vals)
        return res

