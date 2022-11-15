from odoo import models, fields, api


class MrpProduction(models.Model):
    _inherit = 'mrp.production'

    res_partner_id = fields.Many2one(
        'res.partner',
        string='Cliente',
    )
    sale_id = fields.Many2one(
        'sale.order',
        string='Venta',
    )