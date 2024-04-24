from odoo import fields, models, api


class CourseInherit(models.Model):
    _inherit = 'training.course'

    discount = fields.Integer('discount', tracking=True)
    early_bird_limit = fields.Integer('Early Bird Limit', tracking=True)
    early_bird_discount = fields.Integer('Early Bird Discount', tracking=True)
    early_bird_date = fields.Date(tracking=True)
    enroll_ids = fields.One2many("enroll.course", 'course_id')
    enrolled_students = fields.Integer(compute="_get_students")

    def _get_students(self):
        for course in self:
            course.enrolled_students = len(course.enroll_ids)

    def action_enrollment(self):
        domain = [('course_id', '=', self.id)]
        action = self.env.ref('course_enrollment.action_course_enroll')
        result = action.read()[0]
        result['domain'] = domain
        return result

