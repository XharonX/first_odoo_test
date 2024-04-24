# -*- coding: utf-8 -*-
{
    'name': "training_center",

    'author': "Htet Myat",
    'website': "https://github.com/XharonX/",
    'category': 'Training',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['mail'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/course_security.xml',
        'views/training_course_view.xml',
        'views/menu_items.xml',
        'views/course_chapter_view.xml',
        'views/training_center_view.xml',
        'views/categories.xml',
        'data/training_category.xml'
    ],
    'sequence': '-100'
}
