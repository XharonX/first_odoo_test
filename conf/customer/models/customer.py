from odoo.odoo import models, fields
import re


class Validator:
    @staticmethod
    def email(email):
        return re.match(r'[^@]+@[^@]+\.[^@]+', email) is not None

    @staticmethod
    def phone(phone):
        return re.match(r'\d{11}', phone) is not None


class Customer(models.Model):
    _name = 'bookstore.customer'
    _description = "Book Store Customer"
    name = fields.Char(string='customer name')
    email = fields.Char(string='email', validator=Validator.email)
    gender = fields.Selection([
        ('male', 'male'),
        ('female', 'female'),
        ('other', 'other'),
    ], string='Gender')
    phone = fields.Char(string='phone', validator=Validator.phone)
    join_date = fields.Date(string='join date', default=fields.Date.today)
    purchase_history = fields.One2many(comodel_name='bookstore.book_order', inverse_name='customer_id', string='Purchase History')
    loyalty_points = fields.Integer(string='loyalty points')
