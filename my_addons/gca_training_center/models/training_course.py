from odoo import fields, models, api
from datetime import datetime, timedelta


class Course(models.Model):
    _name = 'gca.training.course'
    _description = 'GCA Training Course'

    name = fields.Char("Course Title", required=True)
    level = fields.Selection(
        [
            ('beginner', 'Beginner'),
            ('intermediate', 'Intermediate'),
            ('advanced', 'Advanced'),
            ('expert', 'Expert'),
        ],
        'Course Level')
    active = fields.Boolean('active', default=True)
    price = fields.Monetary('Price', 'currency_id')  ## currency_field='currency_id')
    discount = fields.Float(string='discount')
    category_id = fields.Many2many('course.category', )
    currency_id = fields.Many2one('res.currency')
    manager_remark = fields.Text()
    instructor_id = fields.Many2one('res.partner', string='Instructor')
    chapter_ids = fields.One2many('gca.training.course.chapter', 'course_id')
    training_center_id = fields.Many2one('gca.training.center', 'training center')
    # cover = fields.Image()
    startDate = fields.Date()
    is_importance = fields.Boolean()
    duration_week = fields.Integer()
    num_chapters = fields.Integer(compute="_compute_num_of_chapters", string='numbers of chapter')
    desc = fields.Html("Description")
    state = fields.Selection([("new", "new"),
            ("completed", "completed"),
            ("developing", "developing"),
            ("upgrading", "upgrading"),
            ("canceled", "canceled")], default='new'
                             )
    # num_of_students_enrolls =fields.Integer(compute=num_of_students_enrolls)

    def action_do_new(self):
        if self.state not in ['developing', 'upgrading', 'completed'] or self.create_date == datetime.today:
            return self.write({
                    'state': 'new'
                }
            )

    def action_do_cancel(self):
        if self.state != 'completed':
            self.state = 'canceled'
        return True

    def action_do_completed(self):
        return self.write({
            'state': "completed"
        })

    def action_enrollment(self):
        return None

    # def num_of_students_enrolls(self):
    #     return None

    @api.depends('chapter_ids')
    def _compute_num_of_chapters(self):

        for course in self:
            print(self)
            course.num_chapters = len(course.chapter_ids)

    @api.onchange('price')
    def _onchange_price(self):
        return {'warning': {'title': 'Invalid Price', 'message': "Price cannot be negative"}} if self.price < 0 else None

    @api.constrains('price')
    def _constraint_price(self):
        if self.price < 0:
            raise models.ValidationError("Price must be positive value")
        else:
            return None


class TrainingCenter(models.Model):
    _name = 'gca.training.center'
    _description = "GCA Training Center"
    name = fields.Char('Training Center: ', required=True)
    logo = fields.Image()
    email = fields.Char("Email")
    website = fields.Char("Website")
    address = fields.Char('Address')
    course_ids = fields.One2many('gca.training.course', 'training_center_id')


