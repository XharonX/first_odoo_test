# -*- coding: utf-8 -*-
{
    'name': "enrollment_account",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Ninux",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['course_enrollment'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        # 'views/account_move.xml',
        'views/course_enrollment_inherit.xml',
    ],
    'sequence': '-49'
}
