# -*- coding: utf-8 -*-
{
    'name': "My Reports",

    'summary': """
        Custom reports will be installed.""",

    'description': """
        The following custom reports will be installed: Sales Order, Invoice, Picking List, Purchase Order, 
        custom footer, custom paperformat
    """,

    'author': "K.Sander",
    'website': "-",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Customizations',
    'version': '14.0',
    'images': ['static/description/title_image.png'],
    'license': ['OPL-1'],
    'price': '19.99',
    'support': ['sander.digital.services@gmail.com'],


    # any module necessary for this one to work correctly
    'depends': ['base', 'sale', 'account', 'purchase', 'stock'],
    'installable': True,

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/res_company_view.xml',
        'views/mysalesorder.xml',
        'views/mypaperformat.xml',
        'views/myinvoice.xml',
        'views/mypickinglist.xml',
        'views/mypurchaseorder.xml',
        'views/myfooter.xml',
        'reports/report.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
