from odoo import http
from odoo.http import request


class Main(http.Controller):
    @http.route('/http/courses', type='http', auth=None)
    def course_html(self):
        courses = request.env['training_center.course'].sudo().search([])
        html_result = "<html><body><ul>"
        for course in courses:
            html_result += f"<li> {course.name} </li>"
            html_result += f"</ul> </body> </html>"

        return html_result

    # @http.route('/api/v1/courses', methods=['GET'], type='json', auth=None)
    # def courses_json(self):
    #     courses_obj = request.env['gca.training.center.course'].sudo().search([])
    #     return courses_obj.read(['name', 'level'])