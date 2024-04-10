from odoo import fields, models, api


class CourseCategory(models.Model):
    _name = 'course.category'
    _description = "Course Category"
    _parent_store = True

    name = fields.Char(translate=True, required=True)
    parent_id = fields.Many2one('course.category', 'Parent Category', onDelete='restrict')
    parent_path = fields.Char(index=True)
    child_ids = fields.One2many('course.category', 'parent_id', 'Subcategories')