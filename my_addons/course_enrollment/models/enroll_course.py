from odoo import models, fields, api


class EnrollCourse(models.Model):
    _name = 'enroll.course'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char('Title')
    course_id = fields.Many2one('training.course', tracking=True, required=True)
    enroll_date = fields.Date(default=lambda x: fields.Date.today())
    state = fields.Selection([
        ('new', 'new'), ('confirm', 'confirm'), ('cancel', 'cancel'),
    ], default='new', tracking=True)
    price = fields.Monetary(related='course_id.price', currency_field='currency_id')
    currency_id = fields.Many2one(related='course_id.currency_id')
    student_id = fields.Many2one('training.student', 'Members', tracking=True, required=True)
    discount = fields.Integer(compute='_get_discount_price', store=True)
    total_amount = fields.Monetary('Total', 'currency_id', compute="_get_total", store=True)
    profile = fields.Image(related='student_id.profile')

    def name_get(self):
        result = []
        for course in self:
            instructor = str(course.course_id.instructor_id.name)
            name = f"{course.name}({instructor})"
            result.append((course.id, name))
        return result

    @api.depends('course_id.price', 'course_id.early_bird_discount', 'course_id.early_bird_date')
    def _get_discount_price(self):
        for enroll in self:
            price = enroll.course_id.price
            discount = enroll.course_id.discount
            total_course_enrollments = self.search_count([('course_id', '=', enroll.course_id.id)])
            if enroll.course_id.discount:
                discount = enroll.course_id.discount
            if enroll.course_id.early_bird_discount and (total_course_enrollments <= enroll.course_id.early_bird_limit):
                if enroll.course_id.early_bird_date:
                    if enroll.enroll_date > enroll.course_id.early_bird_date:
                        discount = 0
                    else:
                        discount = enroll.course_id.early_bird_discount
                else:
                    discount = enroll.course_id.early_bird_discount
            else:
                ...
            print(discount)
            price *= (1 - discount / 100)
            enroll.total_amount = price
            enroll.discount = discount

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            print(vals)
            vals['name'] = self.env['ir.sequence'].next_by_code('enroll.course')
        return super().create(vals_list)

    def action_confirm(self):
        self.write(
            {'state': 'confirm'}
        )

    def action_cancel(self):
        self.write(
            {'state': 'cancel'}
        )
