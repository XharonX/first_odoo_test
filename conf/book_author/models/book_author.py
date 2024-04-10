from odoo import fields, models


class BookAuthor(models.Model):
    _name = 'bookstore.author'
    _description = 'bookstore.author'
    # _inherit = 'res.users'

    name = fields.Char(string='name')
    email = fields.Char(string='email', )
    nickname = fields.Char(string='nickname')
    age = fields.Integer(string='age')
    native_town = fields.Char(string='native_town')
    books_ids = fields.Many2one(comodel_name='bookstore.book', inverse_name='author_id', string='Books')
    biography = fields.Text(string='biography')
    # bookstore.author model
    # groups_id = fields.Many2many(comodel_name='ir.model.group', relation='author_group_rel', string='Groups')
    # company_ids = fields.Many2many(comodel_name='ir.users.company_ids', default=None)


