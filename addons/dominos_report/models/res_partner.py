from datetime import datetime
from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    # 3 trường điểm ngũ phân vị (1-5)
    x_dom_rfm_r = fields.Integer(string='Điểm R (Recency)', readonly=True)
    x_dom_rfm_f = fields.Integer(string='Điểm F (Frequency)', readonly=True)
    x_dom_rfm_m = fields.Integer(string='Điểm M (Monetary)', readonly=True)

    # 4 trường giá trị gốc
    x_dom_rfm_recency_days = fields.Integer(string='Số ngày từ đơn gần nhất', readonly=True)
    x_dom_rfm_order_count = fields.Integer(string='Tổng số đơn đã mua', readonly=True)
    x_dom_rfm_total_spent = fields.Float(string='Tổng chi tiêu (VNĐ)', readonly=True)
    x_dom_rfm_last_computed = fields.Datetime(string='Thời điểm tính RFM', readonly=True)

    # Nhãn phân khúc khách hàng
    x_dom_rfm_segment = fields.Selection([
        ('new', 'Mới'),
        ('regular', 'Thường xuyên'),
        ('vip', 'VIP'),
        ('at_risk', 'At-risk (30-60 ngày)'),
        ('lost', 'Không mua lại'),
    ], string='Phân khúc RFM', readonly=True, index=True)

    @api.model
    def _cron_compute_rfm(self):
        icp = self.env['ir.config_parameter'].sudo()

        as_of_str = icp.get_param('dominos_report.as_of_date', default=False)
        if as_of_str:
            as_of_date = fields.Date.from_string(as_of_str)
            ref_dt = datetime.combine(as_of_date, datetime.max.time())
        else:
            ref_dt = fields.Datetime.now()

        at_risk_min = int(icp.get_param('dominos_report.at_risk_min_days', default='30'))
        at_risk_max = int(icp.get_param('dominos_report.at_risk_max_days', default='60'))
        new_max_orders = int(icp.get_param('dominos_report.new_max_orders', default='2'))
        vip_min_orders = int(icp.get_param('dominos_report.vip_min_orders', default='8'))

        confirmed_orders = self.env['sale.order'].search([
            ('state', 'in', ['sale', 'done']),
            ('date_order', '<=', ref_dt),
        ])

        partner_metrics = {}
        for order in confirmed_orders:
            pid = order.partner_id.id
            if not pid:
                continue
            if pid not in partner_metrics:
                partner_metrics[pid] = {
                    'partner': order.partner_id,
                    'last_date': order.date_order,
                    'order_count': 0,
                    'total_spent': 0.0,
                }
            if order.date_order > partner_metrics[pid]['last_date']:
                partner_metrics[pid]['last_date'] = order.date_order
            partner_metrics[pid]['order_count'] += 1
            partner_metrics[pid]['total_spent'] += order.amount_total

        metrics_list = list(partner_metrics.values())
        n = len(metrics_list)
        if n == 0:
            return

        for item in metrics_list:
            delta_days = (ref_dt - item['last_date']).days
            item['recency_days'] = max(0, delta_days)

        # Chấm điểm ngũ phân vị 1-5 cho R (số ngày càng nhỏ điểm càng cao)
        by_recency = sorted(metrics_list, key=lambda x: x['recency_days'])
        for idx, item in enumerate(by_recency):
            item['r_score'] = 5 - int(idx * 5 / n)

        # Chấm điểm ngũ phân vị 1-5 cho F (số đơn càng nhiều điểm càng cao)
        by_freq = sorted(metrics_list, key=lambda x: x['order_count'])
        for idx, item in enumerate(by_freq):
            item['f_score'] = 1 + int(idx * 5 / n)

        # Chấm điểm ngũ phân vị 1-5 cho M (tổng chi càng lớn điểm càng cao)
        by_monetary = sorted(metrics_list, key=lambda x: x['total_spent'])
        for idx, item in enumerate(by_monetary):
            item['m_score'] = 1 + int(idx * 5 / n)

        now_ts = fields.Datetime.now()

        for item in metrics_list:
            recency = item['recency_days']
            count = item['order_count']

            if recency > at_risk_max:
                segment = 'lost'
            elif at_risk_min <= recency <= at_risk_max:
                segment = 'at_risk'
            elif count <= new_max_orders:
                segment = 'new'
            elif count >= vip_min_orders:
                segment = 'vip'
            else:
                segment = 'regular'

            item['partner'].write({
                'x_dom_rfm_r': item['r_score'],
                'x_dom_rfm_f': item['f_score'],
                'x_dom_rfm_m': item['m_score'],
                'x_dom_rfm_recency_days': recency,
                'x_dom_rfm_order_count': count,
                'x_dom_rfm_total_spent': item['total_spent'],
                'x_dom_rfm_segment': segment,
                'x_dom_rfm_last_computed': now_ts,
            })