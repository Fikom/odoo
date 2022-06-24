# -*- coding: utf-8 -*-
# from odoo import http


# class VipReports(http.Controller):
#     @http.route('/vip_reports/vip_reports/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/vip_reports/vip_reports/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('vip_reports.listing', {
#             'root': '/vip_reports/vip_reports',
#             'objects': http.request.env['vip_reports.vip_reports'].search([]),
#         })

#     @http.route('/vip_reports/vip_reports/objects/<model("vip_reports.vip_reports"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('vip_reports.object', {
#             'object': obj
#         })
