# -*- coding: utf-8 -*-
# from odoo import http


# class Siswa(http.Controller):
#     @http.route('/siswa/siswa/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/siswa/siswa/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('siswa.listing', {
#             'root': '/siswa/siswa',
#             'objects': http.request.env['siswa.siswa'].search([]),
#         })

#     @http.route('/siswa/siswa/objects/<model("siswa.siswa"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('siswa.object', {
#             'object': obj
#         })
