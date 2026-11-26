{
    'name': "Domino's RFM Analytics & Reporting",
    'version': '17.0.1.0.0',
    'category': 'Sales/CRM',
    'summary': 'Cron tính chỉ số R, F, M, chấm điểm và báo cáo phân khúc khách hàng',
    'depends': ['base', 'contacts', 'sale_management'],
    'data': [
        'data/ir_cron.xml',
        'views/res_partner_views.xml',
        'views/rfm_report_views.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}