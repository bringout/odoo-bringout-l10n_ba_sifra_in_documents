from odoo import api, fields, models
import re

PATTERN = r'^\[.*?\]\s*'


class PurchaseOrderLine(models.Model):
    """ class for inherited model purchase order line. Contains a field for line
        numbers and a function for computing line numbers.
    """

    _inherit = 'purchase.order.line'

    product_code = fields.Char(string='Code', compute='_compute_product_code', help='Product code', store=False)
    
    name_without_ref = fields.Char(
        string="Name without REF",
        compute='_compute_name_without_ref',
        store=False)
    
    @api.depends('product_id')
    def _compute_product_code(self):
        #for order in self.mapped('order_id'):
        #    sequence_number = 1
        for line in self:
            if line.product_id:
                line.product_code = line.product_id.default_code
            else:
                line.product_code = ''

    @api.depends('name')
    def _compute_name_without_ref(self):
        for line in self:
            line.name_without_ref = re.sub(PATTERN, '', line.name)
