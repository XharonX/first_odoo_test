# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class TrainingCenter(http.Controller):
    @http.route('/html/courses', auth='none', type='http')
    def courses_html(self):
        courses = request.env['training.course'].sudo().search([])
        html_course_ls = "<html><body><ul>"
        for course in courses:
            html_course_ls += f"<li>{course.name}</li>"
        html_course_ls += "</ul></body></html>"
        return html_course_ls

    @http.route('/api/v1/login', methods=["POST"], auth='none', type='json')
    def login(self):
        try:
            req = request.get_json_data()
            if req['login'] and req['password']:
                if not 'database' in req:
                    req['database'] = request.session.db
                    login = request.session.authenticate(req['database'], req['login'].lower(), req['password'])
                    return login

        except Exception as e:
            return {"error_message": e}

    @http.route('/api/v1/courses', methods=["GET"], auth='user', type='json')
    def courses_json(self, **kwargs):
        course_obj = request.env['training.course'].sudo().search([])
        print(course_obj)
        return course_obj.read(['name', 'level', 'price', 'num_chapters'])