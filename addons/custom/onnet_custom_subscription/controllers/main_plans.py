from builtins import print

import odoo
from odoo.http import Controller, request, Response, route

class MainPlans(odoo.http.Controller):
    @odoo.http.route('/plans',  type='http', auth='public', website=True, sitemap=True)
    def index(self, **kw):
        Subscription = request.env['product.template']

        return request.render('onnet_custom_subscription.website_index_plans', {
            'subscription_plans': Subscription.search([])
        })

