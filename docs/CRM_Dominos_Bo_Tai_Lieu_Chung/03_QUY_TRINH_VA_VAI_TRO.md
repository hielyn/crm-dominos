# 03 - Quy trình và vai trò (danh mục chính thức)
## Quy trình
| Mã | Tên | Loại | Chủ | API riêng (A4.7) | Nguồn nội dung cũ trong `nguon/02` |
|---|---|---|---|---|---|
| QT-T | Vòng đời khách hàng: đặt món > ghi nhận đơn > cập nhật hồ sơ + điểm loyalty > phân loại RFM > 30-60 ngày không mua thì vào at-risk > email ưu đãi cá nhân hóa > theo dõi đơn mới và chuyển đổi campaign; **nhánh 2: khách bỏ giỏ hàng > plugin Woo ghi nhận > Odoo gắn nhãn > email nhắc > theo dõi chuyển đổi** | Nhóm (BB) | C vẽ BPMN; A và B chạy trên Odoo chung | `crm.lead` create (ví dụ nhóm, A4.7) | một phần QT-02, QT-03 |
| P1 | Đơn đa kênh + Customer 360 (Website/Woo, POS, hotline nhập tay, Grab/Shopee mô phỏng CSV) | Cá nhân A (BB) | A | `sale.order` create | QT-02 |
| P5 | Khiếu nại giao trễ và đền bù WOW (ticket `helpdesk_mgmt`, SLA, voucher) | Cá nhân A (TC) | A | `helpdesk` ticket | QT-01 |
| P3 | Phân nhóm RFM và tái kích hoạt khách at-risk | Cá nhân B (BB) | B | `search_read` / `read_group` | QT-03 |
| P4 | Email marketing (welcome, sinh nhật, newsletter, remarketing) + analytics campaign | Cá nhân B (TC) | B | (cùng API của B hoặc khác, B hỏi A) | một phần QT-03 |
| P2 | Loyalty: tích điểm, hạng thành viên, đổi quà, voucher sinh nhật | Cá nhân C (BB) | C | `loyalty.card` hoặc `crm.lead` | một phần QT-02 |
| P6 | Đơn tiệc / doanh nghiệp B2B: Lead > Cơ hội > Báo giá > Đơn > Hóa đơn, có lý do thất bại | Cá nhân C (TC) | C | `crm.lead` | QT-04 |
BB = bắt buộc; TC = tùy chọn. Các bước chi tiết từng quy trình: lấy từ `nguon/02` mục 5.2.x, sửa theo quyết định mới; không tự thêm bước nằm ngoài tài liệu mà không ghi `[ĐỀ XUẤT]`.
## Tác nhân/phòng ban trong quy trình (theo nguồn)
Khách hàng, Thu ngân (TN), Cửa hàng trưởng (CHT), CSKH, Marketing (MKT), Sales B2B, Kế toán (KT), Ban quản lý (BQL), QC; hệ thống ngoài: WordPress/WooCommerce, POS, mail. Nghĩa đầy đủ các thuật ngữ khác (ADT, EDT, DOT, OTD, WOW, EX-2, SLA): lấy từ `nguon/02`; **định nghĩa chưa thống nhất** (xem mục chưa chốt ở file 01).
## Vai trò (tóm tắt, chi tiết ở file 04)
- **A:** hạ tầng, cấu hình nền A4.2.1, Customer 360, module `dominos_crm_extension` (A4.9.1), WordPress/Woo + tích hợp (A4.8), đơn đa kênh, tài liệu API nhóm (A4.7), đóng gói zip.
- **B:** dataset chung, import, module `dominos_report` (A4.9.2, RFM), email marketing, CLV + ABC (A4.5), báo cáo A4.6, Looker Studio.
- **C:** tài liệu BA (FR/NFR, UC, 5 Gaps, personas), A4.1, chuẩn BPMN, QT-T, loyalty, A4.10/A4.11, danh sách thành viên, ghép PDF.
