# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Supplier(models.Model):
    _name = 'supplier'
    _description = 'Model Supplier'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Supplier', required=True)


