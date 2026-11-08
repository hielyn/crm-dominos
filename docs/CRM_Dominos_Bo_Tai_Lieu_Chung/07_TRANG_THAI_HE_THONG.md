# 07 - Trạng thái hệ thống thật (A cập nhật; đây là nguồn đúng nhất về kỹ thuật)
Cập nhật lần cuối: 08/11/2026. Mục ghi `[A cập nhật]` = A chưa công bố; AI không được tự điền.

## Phiên bản
| Thành phần | Giá trị |
|---|---|
| Odoo | 17.0 Community (image `odoo:17.0`, bản đang chạy 17.0-20260908) |
| CSDL | PostgreSQL 15 |
| Database Odoo của A | `dominos` |
| Ngôn ngữ | Tiếng Việt đang bật; **Tiếng Anh cần bật thêm** (rubric) |
| Demo data | Tắt |
| Môi trường của A | Windows, Docker 29.9.2, Docker Compose v5.6.1 |

## Dịch vụ Docker (repo `docker-compose.yml`)
| Dịch vụ | Địa chỉ | Ghi chú |
|---|---|---|
| odoo | http://localhost:8069 | addons: `addons/` và `addons/oca-helpdesk` |
| db | (nội bộ) | PostgreSQL |
| mailpit | http://localhost:8025 | SMTP trong mạng Docker: `mailpit:1025` |
| wordpress | http://localhost:8080 | cài plugin WooCommerce |
| wp-db | (nội bộ) | MariaDB 11 |
WordPress gọi Odoo tại `http://odoo:8069/jsonrpc` (JSON-RPC, dùng API key của Odoo).

## Module Odoo
- **Đã cài (A xác nhận):** CRM, Bán hàng (Sales), Xuất hóa đơn (Invoicing), Tồn kho (Inventory), Email Marketing, Thảo luận, Liên hệ, Lịch, OCA `helpdesk_mgmt`.
- **Đang cài / chưa xác nhận:** Automation Rules (`base_automation`), Point of Sale, Discount & Loyalty, bật Leads trong CRM, Mẫu báo giá, ngôn ngữ Tiếng Anh, máy chủ thư đi (Mailpit). `[A cập nhật]`
- **Sẽ viết:** `dominos_crm_extension` (A), `dominos_report` (B).

## Người dùng và quyền `[A cập nhật]`
Danh sách đề xuất: TN, CHT, CSKH, MKT, Sales B2B, KT, BQL + admin chính (email sinh viên). Bảng quyền chi tiết **chưa chốt**.

## Sales team, pipeline, lý do thất bại, layout `[A cập nhật]`
Chưa công bố. Không tự đặt tên stage hay team.

## Trường tùy chỉnh (ĐỀ XUẤT, chờ A xác nhận trước khi B và C dùng)
| Đối tượng | Tên kỹ thuật đề xuất | Ý nghĩa |
|---|---|---|
| Khách (res.partner) | `x_dom_fav_food`, `x_dom_birthday`, `x_dom_pref_channel`, `x_dom_tier` | sở thích món, ngày sinh, kênh đặt ưu tiên, hạng thành viên |
| Khách | `x_dom_rfm_r`, `x_dom_rfm_f`, `x_dom_rfm_m`, `x_dom_rfm_segment` | điểm R/F/M và nhãn phân khúc |
| Đơn bán (sale.order) | `x_dom_channel`, `x_dom_edt`, `x_dom_adt`, `x_dom_is_late` | kênh, thời gian giao dự kiến/thực tế, cờ trễ |
| Ticket | `x_dom_sla_deadline` | hạn xử lý SLA |
Giá trị `x_dom_rfm_segment` (nhãn theo tài liệu nguồn): mới, thường xuyên, VIP, at-risk (30-60 ngày không mua), không mua lại. Mã giá trị kỹ thuật `[A cập nhật]`.
Điểm loyalty lưu ở module Discount & Loyalty (nếu có trên Community 17.0, chưa kiểm chứng), không tạo trường điểm riêng khi A chưa quyết.
