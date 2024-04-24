# -*- coding: utf-8 -*-
# from odoo import http


# class CourseEnrollment(http.Controller):
#     @http.route('/course_enrollment/course_enrollment', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/course_enrollment/course_enrollment/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('course_enrollment.listing', {
#             'root': '/course_enrollment/course_enrollment',
#             'objects': http.request.env['course_enrollment.course_enrollment'].search([]),
#         })

#     @http.route('/course_enrollment/course_enrollment/objects/<model("course_enrollment.course_enrollment"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('course_enrollment.object', {
#             'object': obj
#         })
