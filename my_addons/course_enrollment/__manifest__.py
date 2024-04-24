# -*- coding: utf-8 -*-
{
    'name': "course_enrollment",

    'author': "Ninux",
    'category': 'Training',

    'depends': ['training_center', 'mail'],

    'data': [
        'security/ir.model.access.csv',
        'views/enroll_course_views.xml',
        'views/course_inherit_view.xml',
        'views/menu_items.xml',
        'data/sequence.xml',
        'wizard/enroll_message_wizard.xml',
        'reports/course_enrollment_print.xml',
    ],
    'sequence': '-50'
}
