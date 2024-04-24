{
    'name': "Training Center",
    'author': "Helloworld funny",
    'summary': "Easy to control odoo Training Center ",
    'category':  "Training",
    'data': [
        'security/course_security.xml',
        'security/ir.model.access.csv',
        'views/training_course.xml',
        'views/course_chapter_view.xml',
        'views/course_view_ui.xml',
        'views/training_center_view_ui.xml'
        # 'views/.xml'
    ],
    'depends': ['mail'],
    'sequence': '-10',
}