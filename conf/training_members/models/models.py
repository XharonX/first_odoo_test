# -*- coding: utf-8 -*-

from odoo import models, fields, api


class TrainingMembers(models.Model):
    _name = 'training_members.member'
    _description = 'Training Members'

    card_num = fields.Char("Card")
    partner_id = fields.Many2one("res.partner", delegate=True, ondelete="cascade", required=True)
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
