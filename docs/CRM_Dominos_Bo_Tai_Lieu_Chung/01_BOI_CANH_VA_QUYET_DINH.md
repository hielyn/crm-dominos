# 01 - Bối cảnh và quyết định
## Bối cảnh
- Đồ án cuối kỳ môn CRM (mã EC213): triển khai giải pháp CRM cho 1 doanh nghiệp; nhóm chọn **Domino's Pizza** (case giả định, không có dữ liệu thật của doanh nghiệp).
- Nhóm 3 người: **A** = Odoo Developer & System Specialist (Hà Yến Linh), **B** = Data & Analytics Specialist (Trần Hoàng Ngọc Lan), **C** = BA & Process Lead (Phạm Phương Ái Linh).
- Hạn nộp: **23/11/2026** (đã dời từ 16/11). Chưa có số nhóm chính thức để đặt tên file: `[?]` số nhóm XX.
- Sản phẩm nộp: 1 file zip `Nhóm XX - Đồ án CRM.zip` gồm báo cáo PDF/docx, mã nguồn, demo trên Odoo, BPMN, video; có thư mục `Cá nhân` (chi tiết: file 02).

## ĐÃ CHỐT (không tự thay đổi)
1. **Nền tảng:** Odoo **Community 17.0**, tự cài bằng Docker; module cộng đồng OCA `helpdesk_mgmt` (nhánh 17.0) cho ticket. KHÔNG dùng Odoo Enterprise/bản dùng thử, KHÔNG dùng Helpdesk gốc của Odoo.
2. **Website:** 1 site WordPress + WooCommerce (10-15 sản phẩm Domino's), Contact Form 7 hoặc WPForms cho form đơn tiệc, 1 plugin giỏ bị bỏ; chạy cùng mạng Docker với Odoo; WordPress gọi Odoo bằng JSON-RPC. Không dùng Odoo Website/eCommerce.
3. **Camunda:** mức 1 (bắt buộc) = Camunda Modeler bản cài trên máy để vẽ `.bpmn`; mức 2 = chạy engine trong Docker, bắt đầu sau 17/11 nếu phần bắt buộc xong. **Đã bỏ** connector Tehuti (dành cho Odoo 19, không hợp Odoo 17.0).
4. **Báo cáo:** báo cáo có sẵn của Odoo (CRM, Sales) là bắt buộc; **Looker Studio được giữ lại**, dữ liệu đưa qua script Python chạy trên máy (hoặc xuất CSV) lên Google Sheets.
5. **Mail demo:** Mailpit (SMTP `mailpit`, cổng 1025). SMS, Zalo OA, Push chỉ ghi là **hướng mở rộng**.
6. **Quy trình:** 1 quy trình nhóm **QT-T** (vòng đời khách hàng, có nhánh bỏ giỏ hàng) + mỗi người 1 quy trình cá nhân bắt buộc + 1 tùy chọn: A: P1 (bắt buộc), P5 (tùy chọn); B: P3, P4; C: P2, P6. Chi tiết: file 03, 05.
7. **Mỗi người tự cài Odoo riêng**, email admin là email sinh viên của mình, tự quay video, tự viết API doc (mỗi người một API khác nhau).
8. Phân công theo `04_GUIDELINE_V2.md`; ghép PDF cuối do C; đóng gói mã nguồn/zip do A.

## CHƯA CHỐT `[?]` (AI phải hỏi, không tự quyết)
- Số nhóm XX.
- Bảng quyền chi tiết của 7 user Odoo (TN, CHT, CSKH, MKT, Sales B2B, KT, BQL) và tài khoản admin chính.
- Bảng quy tắc loyalty (tỷ lệ tích điểm, ngưỡng hạng, đổi quà, voucher sinh nhật): C chốt cùng nhóm, hạn 11/11.
- ABC Costing làm trên Odoo hay trên Sheets.
- Plugin giỏ bị bỏ cụ thể; phiên bản Camunda cho mức 2.
- Tên các stage pipeline, Sales team, tên trường tùy chỉnh chính thức (A công bố trong file 07).
- Các điểm mâu thuẫn trong tài liệu nguồn 02 mục 5.4: định nghĩa ADT/EDT/OTD, mốc SLA, bộ trạng thái ticket, hệ mã FR/NFR (99,9% hay 99,5%), vai trò QC, tên Activity.

## ĐÃ KIỂM CHỨNG và CHƯA KIỂM CHỨNG
- Đã chạy thật: Odoo 17.0 Community trên Docker (Windows), cài CRM, Bán hàng, Tồn kho, Email Marketing; cài `helpdesk_mgmt` thành công.
- **Chưa kiểm chứng (đừng coi là chắc chắn):** webhook gốc của Odoo 17.0 (nhiều khả năng chưa có); module Loyalty có trên Community 17.0 hay không; thống kê mở/click email khi chạy local; cấu hình ABC/analytic trên Community; script Odoo > Google Sheets; plugin giỏ bị bỏ; Camunda engine với Odoo 17.
- Ghi chú: Apps Script của Google không gọi được Odoo chạy localhost, nên dùng script trên máy hoặc CSV.

## Giới hạn tài liệu nguồn
- `nguon/04` (ý tưởng hệ thống ban đầu) có các ý đã bị thay thế: Camunda 8 + connector Tehuti, kiến trúc "Odoo webhook". Trích dẫn trong đó chưa được kiểm chứng.
- `nguon/02` (quy trình) đã sửa nhưng danh mục quy trình trong đó (QT-01..04) khác danh mục mới (QT-T, P1..P6); xem bảng đối chiếu ở file 03.
