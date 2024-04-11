from odoo import models, fields, api


class Course(models.Model):
    _inherit = 'gca.training.course'

    discount = fields.Integer("discount")
    enroll_ids = fields.One2many("enroll.course", 'course_ids')