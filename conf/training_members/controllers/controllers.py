# -*- coding: utf-8 -*-
# from odoo import http


# class TrainingMembers(http.Controller):
#     @http.route('/training_members/training_members', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/training_members/training_members/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('training_members.listing', {
#             'root': '/training_members/training_members',
#             'objects': http.request.env['training_members.training_members'].search([]),
#         })

#     @http.route('/training_members/training_members/objects/<model("training_members.training_members"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('training_members.object', {
#             'object': obj
#         })
