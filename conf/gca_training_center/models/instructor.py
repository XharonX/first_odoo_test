from odoo import models, fields


class TrainingInstructor(models.Model):
    # _name = 'gca.training.instructor'
    _description = "GCA Training Instructor"
    _inherit = "res.partner"

    name = fields.Char('Name', required=True)
    email = fields.Char('Email')
    active = fields.Boolean(default=True)
    # bio = fields.Text()
    course_ids = fields.One2many('gca.training.course', 'instructor_id', 'course')