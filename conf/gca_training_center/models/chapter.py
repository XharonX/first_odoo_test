from odoo import fields, models


class Chapter(models.Model):
    _name = 'gca.training.course.chapter'
    _description = "Training Course Training"
    _order = 'order'

    title = fields.Char("Title")
    content = fields.Html()
    order = fields.Integer()
    course_id = fields.Many2one('gca.training.course', 'course', inverse_name='chapter_ids')

    # def __init__(self):
    #     self._compute_number_of_chapters()
    #
    # def _compute_number_of_chapters(self):
    #     for chapter in self:
    #         chapters = self.search_count(['course_id', '=', chapter.course_id.id])
    #         chapter.order = chapters + 1