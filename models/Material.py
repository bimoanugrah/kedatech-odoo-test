# -*- coding: utf-8 -*-

from odoo import models, fields, api


class material(models.Model):
    _name = 'material'
    _description = 'Model Material'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    material_code = fields.Char('Material Code', required=True)
    material_name = fields.Char('Material Name', required=True)
    material_type = fields.Selection([('fabric', 'Fabric'),
                               ('jeans', 'Jeans'),
                               ('cotton', 'Cotton')],
                              'Material Type', default='fabric')
    material_buy_price = fields.Float('Material Buy Price')
    related_supplier = fields.Many2one('supplier', 'Supplier', required=True)



