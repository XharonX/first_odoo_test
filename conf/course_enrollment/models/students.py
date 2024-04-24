from odoo import models, fields, api


class Student(models.Model):
    _name = "enrolled.student"
    _description = "Training Student"
    _inherit = "res.partner"

    student_id = fields.Char('Student ID')
    date_of_birth = fields.Date()
