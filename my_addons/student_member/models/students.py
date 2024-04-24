from odoo import models, fields, api


class StudentsMember(models.Model):
    _name = 'training.student'
    _description = 'Students'

    card_no = fields.Char('Card NO:',)
    profile = fields.Image()
    student_id = fields.Many2one('res.partner', delegate=True, ondelete='cascade', required=True)
    # enroll_id = fields.Many2one('enroll.course')
