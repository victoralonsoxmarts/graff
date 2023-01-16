# -*- coding: utf-8 -*-
{
    'name': "graff_entrada_pt",

    'summary': """
        """,

    'description': """
        
    """,

    'author': "My Company",
    'website': "tuodoo.com",
    'category': 'Uncategorized',
    'version': '14.2',
    'depends': ['mrp'],
    'data': [
        'security/ir.model.access.csv',
        'views/reports_mrp.xml',
        'views/mrp_production.xml',
        'views/res_company.xml',
        'wizard/report_mrp.xml',
        'report/template_reports_mrp.xml',
    ],
}
