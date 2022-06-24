# -*- coding: utf-8 -*-

from odoo import fields, models, api


class ResCompany(models.Model):

    _inherit = 'res.company'

    ceo_name = fields.Char('CEO')
    bank_name = fields.Char('Bank Name')
    bank_acc_number = fields.Char('Bank Account Number')
    bank_acc_bic = fields.Char('BIC')
