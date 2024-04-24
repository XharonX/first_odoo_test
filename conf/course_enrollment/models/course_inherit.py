from odoo import models, fields, api


class Course(models.Model):
    _inherit = 'gca.training.course'

    discount = fields.Integer("discount", Tracking=True)
    enroll_ids = fields.One2many("enroll.course", 'course_ids')
    early_bird_discount = fields.Integer("Early Bird Discount", Tracking=True)
    early_bird_end_date = fields.Date("Early Bird End Date: ")
    num_of_students_enroll = fields.Integer(compute="_compute_num_of_students")

    def _compute_num_of_students(self):
        for course in self:
            course.num_of_students_enroll = len(course.enroll_ids)

    def action_enrollment(self):
        domain = [('course_ids', '=', self.id)]
        action = self.env.ref("course_enrollment.enrollment_view")
        print(action)
        result = action.read()[0]
        print(result)
        result['domain'] = domain
        return result
        # result['context'] = {'default_course_id': self.id }