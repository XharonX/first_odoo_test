# -*- coding: utf-8 -*-

from odoo import models, fields, api


class EnrollCourse(models.Model):
    _inherit = 'enroll.course'

    def action_confirm(self):
        res = super().action_confirm()
        journal = self.env['account.journal'].search(['type','=', 'sale'], limit=1)

        for prop in self:
            self.env['account.move'].create(
                {
                    'partner_id': prop.member_id.partner_id.id,
                    'currency_id': prop.currency_id.id,
                    'name': prop.name,
                    'invoice_date': prop.enroll_date,
                    'move_type': 'out_invoice',
                    'journal_ids': journal.id,
                    'invoice_line_ids': [

                    ]
                }
            )

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100
