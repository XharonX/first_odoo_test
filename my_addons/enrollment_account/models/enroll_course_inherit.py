from odoo import fields, models, api


class EnrollCourseInherit(models.Model):
    _inherit = 'enroll.course'
    state = fields.Selection([
        ('new', 'new'), ('draft', 'draft'), ('confirm', 'confirm'), ('cancel', 'cancel'),
    ], tracking=True)

    def action_confirm(self):
        res = super().action_confirm()
        journal = self.env['account.journal'].search([('type', '=', 'sale')], limit=1)
        if journal:
            for prop in self:
                moves = prop.env['account.move'].search([('name', '=', prop.name)])
                if moves:
                    print('This account has been already exist.')
                else:
                    self.env['account.move'].create(
                        {
                            'partner_id': prop.student_id.student_id.id,
                            'currency_id': prop.currency_id.id,
                            'name': prop.name,
                            'invoice_date': prop.enroll_date,
                            'move_type': 'out_invoice',
                            'journal_id': journal.id,
                            'invoice_line_ids': [
                                (0, 0, {
                                    'name': prop.name,
                                    'quantity': 1.0,
                                    'price_unit': prop.total_amount,
                                }),
                                (0, 0, {
                                    'name': 'Administrative Fee',
                                    'quantity': 1.0,
                                    'price_unit': 10.0,
                                })
                            ]
                        })
        else:
            "There is no journal"
        return res

    def action_reset_to_draft(self):
        self.write(
            {'state': 'draft'}
        )
        for prop in self:
            try:
                acc_move = self.env['account.move'].search([('name','=', prop.name)])
                if acc_move.state == 'posted':
                    acc_move.write({'state': 'draft'})
                else:
                    ...

            except Exception as e:
                print(f'Returning -> {e}')