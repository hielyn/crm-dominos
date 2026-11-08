# CRM Domino's Pizza - Hệ thống và bộ quy trình V2 (07/11/2026)

Thay thế QUY_TRINH_CHOT.md. **Nhóm đã xác nhận 07/11/2026:** quy trình nhóm QT-T, phân công cá nhân, Camunda mức 1 và 2, giữ remarketing bỏ giỏ hàng (plugin WooCommerce). Còn [?]: số nhóm XX. Hạn nộp 23/11 (dời từ 16/11).

## 1. Phạm vi hệ thống: 7 module trên Odoo Community 17.0
| Module | Cách làm trên Odoo | Mức |
|---|---|---|
| Customer 360 | Contact + trường tùy chỉnh (sở thích món, ngày sinh, kênh đặt, điểm) trong module code; nút xem đơn, ticket, lead trên hồ sơ | Cấu hình + code |
| Order & POS | Bán hàng (web/Woo, call center nhập tay), app Point of Sale cho quầy, nhập CSV mô phỏng đơn từ Grab/Shopee | Cấu hình + script |
| Segmentation & RFM | Tác vụ định kỳ (cron) tính R, F, M; gắn nhãn VIP, thường xuyên, mới, at-risk (30-60 ngày), không mua lại | Code |
| Email marketing | App Email Marketing: danh sách/lọc theo segment, welcome, sinh nhật, newsletter; có thống kê mở, click | Cấu hình |
| Remarketing | Email cho khách lâu không mua, sau đơn đầu, từng mua combo (từ segment); bỏ giỏ hàng: plugin WooCommerce ghi nhận giỏ bị bỏ, gửi dữ liệu về Odoo qua API (chọn plugin cụ thể ở bước P3) | Cấu hình + script, **giữ lại** |
| Loyalty | App Discount & Loyalty (điểm, voucher) + trường hạng Bạc/Vàng/Kim Cương và voucher sinh nhật tự tính | Cấu hình + code |
| Analytics | Báo cáo CRM/Sales sẵn có của Odoo (bắt buộc A4.6) + Looker Studio (open rate, CTR, repeat rate, churn, CLV, doanh thu theo campaign) | Có sẵn + script |
| Khiếu nại | OCA `helpdesk_mgmt` + SLA tự dựng | Đã cài |

SMS, Zalo OA, Push: chỉ ghi là hướng mở rộng (cần dịch vụ ngoài), bản demo dùng email.

## 2. Kiến trúc chốt
```
Khách / Web WordPress+Woo / POS / Call center / Grab (CSV)
              |
        Odoo Community 17.0 (+ module OCA helpdesk_mgmt, dominos_crm_extension, dominos_report)
        Contact, Lead, Order, Loyalty, Segment, Campaign, Ticket
              |  XML-RPC / JSON-RPC
    +---------+-----------------+
    |                           |
 Script Python > Google Sheets > Looker Studio     Camunda (xem mục 4)
    |
 Email (Mailpit demo / SMTP)
```
Docker: `odoo`, `db` (PostgreSQL), `mailpit`, `wordpress` (cài plugin WooCommerce) + `mariadb`; Camunda tùy mức ở mục 4. OCA helpdesk là module trong `addons/`, không phải container.

## 3. Danh mục quy trình và phân công (ĐÃ XÁC NHẬN)
**Quy trình nhóm (A4.3.1):** QT-T - Vòng đời khách hàng: khách đặt món > ghi nhận đơn > cập nhật hồ sơ + điểm > phân loại RFM > 30-60 ngày không mua thì vào at-risk > gửi email ưu đãi cá nhân hóa > theo dõi đơn mới và chuyển đổi campaign. Có thêm tác nhân thứ hai: **khách bỏ giỏ hàng trên website** > plugin Woo ghi nhận > Odoo gắn nhãn > email nhắc giỏ hàng > theo dõi chuyển đổi (nhánh remarketing, do cả nhóm chịu trách nhiệm để chắc chắn có demo). Có đủ marketing, bán hàng, chăm sóc, nhiều phòng ban.

**Quy trình cá nhân (A4.3.2): bắt buộc 1 quy trình mỗi người, quy trình thứ 2 làm nếu còn thời gian.**
| Người | Bắt buộc | Tùy chọn | API riêng (A4.7) |
|---|---|---|---|
| A (Hà Yến Linh) | QT-P1 Đơn đa kênh + Customer 360 (Woo, POS, call center) | QT-P5 Khiếu nại giao trễ + WOW (từ QT-01 cũ) | `sale.order` create |
| B (Trần Hoàng Ngọc Lan) | QT-P3 RFM + tái kích hoạt khách at-risk | QT-P4 Email marketing (welcome, sinh nhật, newsletter) + analytics campaign | `search_read` / `read_group` |
| C (Phạm Phương Ái Linh) | QT-P2 Loyalty (tích điểm, hạng, đổi quà, voucher sinh nhật) | QT-P6 Đơn tiệc B2B: Lead > Báo giá > Hóa đơn, lý do thất bại (từ QT-04 cũ) | `crm.lead` create (từ form WP) hoặc `loyalty.card` |

Tái sử dụng nội dung cũ: QT-01 > QT-P5, QT-02 > QT-P1 và QT-P2, QT-03 > QT-P3, QT-04 > QT-P6.
Lưu ý: dù QT-P6 là tùy chọn, rubric A4.2.1 vẫn chấm pipeline, lead, lý do thất bại, nên phần cấu hình và dữ liệu mẫu cho CRM pipeline phải làm trong mọi trường hợp.

## 4. Camunda: chia mức để không rủi ro
- **Mức 1 (bắt buộc):** Camunda Modeler bản cài máy để vẽ và xuất `.bpmn`, `.png`. Rubric chỉ yêu cầu mở được file bằng Modeler.
- **Mức 2 (nhóm đồng ý làm, bắt đầu sau 17/11 nếu các phần bắt buộc đã xong):** chạy engine Camunda trong Docker, gọi Odoo qua REST/XML-RPC cho 1 luồng đơn giản (vd. email at-risk hoặc bỏ giỏ). Phiên bản Camunda (7 hay 8, bản chạy nhẹ) sẽ chọn và kiểm tra lúc bắt đầu mức 2.
- **Connector Tehuti: ĐÃ BỎ (07/11).** Nó dùng API JSON-2 của Odoo 19, không hợp Odoo 17.0. Mức 2 dùng REST/XML-RPC trực tiếp.

## 5. Sửa lại tài liệu gốc (Untitled document 12)
- Xóa ký hiệu thừa (`****&****`), định dạng lại thành báo cáo; ghi "Odoo webhook" là cách tích hợp hướng mở rộng (Odoo 17.0 chưa có webhook sẵn, cần kiểm tra).
- Danh mục trích dẫn: hai mục (Purnomo & Sfenrianto 2021; Dinasti 2025) đang trỏ cùng một đường dẫn, mục AccessOn không có link: kiểm tra từng nguồn, ghi đầy đủ tác giả, năm, tạp chí, DOI/URL trước khi dùng.
- Câu "phù hợp mô hình loyalty tích hợp CRM, POS, app, email/SMS" đang dựa vào một nguồn duy nhất (CyberLeninka): đọc lại nguồn để chắc nó nói đúng như vậy.
- "OCA helpdesk" ghi rõ là module, không phải dịch vụ Docker.

## 6. Chuẩn bị theo thứ tự
P1 bật module (Automation Rules, Loyalty, Mẫu báo giá, Leads, Point of Sale) > P2 Mailpit + SMTP > P3 WordPress/Woo trong Docker + API key + chọn plugin giỏ bị bỏ > P4 khung hai module > P5 dữ liệu mẫu chung > P6 Camunda Modeler, OBS, thử script Sheets/Looker > P7 mỗi người dựng Odoo riêng, đổi email admin.

## 7. Lịch (hạn nộp 23/11, dời từ 16/11)
| Ngày | Việc |
|---|---|
| 8-9/11 | Nhóm chốt hồ sơ; P1-P3 (module, mail, WordPress/Woo) |
| 10-11/11 | Dataset v1, bảng quy tắc loyalty, backup DB, mẫu BPMN |
| 12-13/11 | Vẽ BPMN 4 quy trình bắt buộc; khung module; thử script Sheets/Looker |
| 14-17/11 | Chạy quy trình + chụp ảnh; hoàn thiện module; bắt đầu Camunda mức 2 nếu dư |
| 18-20/11 | Video cá nhân; API; báo cáo A4.6; CLV/ABC; quy trình tùy chọn; chốt tính năng 20/11 |
| 21-22/11 | Ghép PDF, đóng gói zip, thử clone sạch, rà soát chéo, đệm sự cố |
| 23/11 | Nộp |
