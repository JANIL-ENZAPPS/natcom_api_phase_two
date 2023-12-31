# -*- coding: utf-8 -*-
{
    'name': "Enzapps Nactom Phase 2 Invoice API",
    'author':
        'Enzapps',
    'summary': """
    This is a module is for Nactom Phase 2 Invoice API
""",

    'description': """
        This is a module is for Phase 2 Invoice API
    """,
    'website': "www.enzapps.com",
    'category': 'base',
    'version': '14.0',
    'depends': ['base', 'contacts', 'sale', 'sale_management', 'sale_stock', 'stock', 'product', 'account','account_invoice_ubl','natcomjson',
                'natcomsfeb_email_form', 'natcoms_jan_mou_enz','ksa_zatca_integration','enz_natcom_pahse_one_deactivate'],
    "images": ['static/description/icon.png'],
    'data': [
        'reports/natcom_pdf_mou.xml',
    ],
    'demo': [
    ],
    'installable': True,
    'application': True,
}
