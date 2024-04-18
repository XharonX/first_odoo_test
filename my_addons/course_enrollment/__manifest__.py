{
    'name': 'Course Extend',
    'category': "Training",
    'summary': "This module is extends with GCA training center course",
    'author': 'Training Center',
    'depends': [
        'gca_training_center',
    ],
    'data': [
        'security/ir.model.access.csv',
        'security/course_security.xml',
        'views/course_inherit.xml',
        'views/enroll_course.xml',

        # 'views/enrollment_menu_items.xml',

    ]
}

