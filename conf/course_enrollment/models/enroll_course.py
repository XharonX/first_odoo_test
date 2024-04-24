from odoo import models, fields, api


class EnrollCourse(models.Model):
    _name = 'enroll.course'
    _description = "Enrollment Training Course"
    _rec_name = 'member_id'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    name = fields.Char('Title')
    enroll_date = fields.Date(default=lambda x: fields.Date.today())
    price = fields.Monetary('price', 'currency_id', related='course_ids.price')
    currency_id = fields.Many2one('res.currency', related='course_ids.currency_id')
    state = fields.Selection(selection=[
        ('new','New'), ('confirmed', 'confirmed'), ('canceled', 'canceled')
    ], default='new')
    course_ids = fields.Many2one('gca.training.course', tracking=True, required=True)
    member_id = fields.Many2one('training_members.member', tracking=True, required=True)
    total_amount = fields.Monetary('Total', 'currency_id', compute='_get_total', store=True)
    discount = fields.Integer('Discount', compute='_get_total', store=True)

    def action_confirm(self):
        return self.write({"state": "confirmed"})

    def action_enrollment(self):
        domain = [('course_ids', '=', self.id)]
        action = self.env.ref("course_enrollment.enrollment_view")
        print(action)
        result = action.read()[0]
        print(result)
        result['domain'] = domain
        return result


    @api.depends('course_ids.price', 'course_ids.discount', 'course_ids.early_bird_discount')
    def _get_total(self):
        for enroll in self:
            price = enroll.course_ids.price
            discount = enroll.course_ids.discount
            total_course_enrollments = self.search_count([('course_ids', '=', enroll.course_ids.id)])
            if enroll.course_ids.discount:
                discount = enroll.course_ids.discount
            if enroll.course_ids.early_bird_discount and total_course_enrollments <= 5:
                if enroll.early_bird_end_date:
                    if enroll.enroll_date > enroll.course_ids.early_bird_end_date:
                        discount = 1
                else:
                    discount = enroll.course_ids.early_bird_discount
            else:
                ...

            price *= (1 - discount / 100)
            enroll.total_amount = price
            enroll.discount = discount

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            vals['name'] = self.env['ir.sequence'].next_by_code('enroll.course') or '/'
        return super().create(vals_list)

    # def num_of_students_enrolls(self):
    #     ...
