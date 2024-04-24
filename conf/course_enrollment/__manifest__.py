{
    'name': 'Course Extend',
    'category': "Training",
    'summary': "This module is extends with GCA training center course",
    'author': 'Training Center',
    'depends': ['gca_training_center', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'security/course_security.xml',
        'views/course_inherit.xml',
        'views/enroll_course.xml',
        'data/enroll_sequence_data.xml',
        'wizard/enrollment_message_wizard.xml',
        # 'views/enrollment_menu_items.xml',

    ]
}

