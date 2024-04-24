from odoo import fields, models, api


class TrainingCourse(models.Model):
    _name = 'training.course'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    name = fields.Char('Course Title', required=True)
    active = fields.Boolean(default=True)
    level = fields.Selection([
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ], 'Course Level', default='beginner', tracking=True)
    price = fields.Monetary('Price', 'currency_id', tracking=True)
    start_date = fields.Date()
    num_chapters = fields.Integer(compute='_get_num_of_chapter', string="Num: Chapter")
    state = fields.Selection([
        ("new", "new"),
        ("developing", "developing"),
        ("complete", "complete"),
        ("cancel", "cancel")
    ], default='new', tracking=True)
    currency_id = fields.Many2one('res.currency')
    category_ids = fields.Many2many('course.category', tracking=True)
    training_center_id = fields.Many2one('training.center', 'Training Center')
    chapter_ids = fields.One2many('course.chapter', 'course_id', 'Chapter', tracking=True)
    instructor_id = fields.Many2one('res.partner', )

    @api.depends('chapter_ids')
    def _get_num_of_chapter(self):
        for course in self:
            course.num_chapters = len(course.chapter_ids)

    def action_cancel(self):
        self.write(
            {'state': 'cancel'}
        )

    def action_complete(self):
        self.write(
            {'state': 'complete'}
        )

    def action_developing(self):
        self.write(
            {'state': 'developing'}
        )


class TrainingCenter(models.Model):
    _name = 'training.center'
    name = fields.Char('Training Center: ', required=True)
    logo = fields.Image()
    email = fields.Char("Email")
    website = fields.Char("Website")
    course_ids = fields.One2many('training.course', 'training_center_id', 'Courses')


class Chapters(models.Model):
    _name = 'course.chapter'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'order'
    name = fields.Char('Title')
    content = fields.Html(tracking=True)
    order = fields.Integer(tracking=True)
    due_date = fields.Date()
    course_id = fields.Many2one('training.course', 'Course', tracking=True, ondelete='cascade')


class CourseCategory(models.Model):
    _name = 'course.category'
    name = fields.Char(required=True)
    parent_id = fields.Many2one('course.category', 'Parent', ondelete='restrict')
    parent_path = fields.Char(index=True)
    child_ids = fields.One2many('course.category', 'parent_id', 'Sub')