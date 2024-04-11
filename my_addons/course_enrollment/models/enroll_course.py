from odoo import models, fields, api


class EnrollCourse(models.Model):
    _name = 'enroll.course'
    _description = "Enrollment Training Course"

    enroll_date = fields.Date(default=lambda x: fields.Date.today())
    price = fields.Monetary('price', 'currency_id')
    currency_id = fields.Many2one('res.currency')
    state = fields.Selection(selection=[
        ('new','New'), ('confirmed', 'confirmed'), ('canceled', 'canceled')
    ], default='new')
    course_ids = fields.Many2one('gca.training.course')

    def action_confirm(self):
        return self.write({"state": "confirm"})

    def action_enrollment(self):
        return None

    # def num_of_students_enrolls(self):
    #     ...
