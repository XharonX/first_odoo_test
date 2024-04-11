from odoo.odoo.tests.common import TransactionCase


class TestBook(TransactionCase):
    def setUp(self, *args, **kwargs):
        super().setUp(*args, **kwargs)
        self.Book = self.env['bookstore.book']
        self.book1 = self.Book.create(
            {
                'name': "Odoo 15 Development Essentials",
                'author': "Daniel Reis",
                'pages': 524,
            }
        )

    def test_book_create(self):
        "New Books are active by default"
        self.assertEquals(self.book1.active, True)