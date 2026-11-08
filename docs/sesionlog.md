# Nhật ký phiên làm việc - Đồ án CRM Domino's Pizza (EC213)

Hạn nộp: 16/11. Mỗi phiên ghi: mục tiêu, đã làm, kết quả/file, việc kế tiếp. Dán file này vào phiên chat mới (hoặc đính kèm) để tiếp tục mà không cần giải thích lại.

## Trạng thái hiện tại
- Chọn: Odoo 17 Community trên Docker, repo GitHub chung (crm-dominos-starter.zip)
- Đã có: báo cáo tuần trước (giới thiệu DN, yêu cầu FR/NFR, 5 Gaps, user classes, mô hình phân khúc)
- Còn thiếu: triển khai Odoo (ch.4), BPMN + demo (ch.5), CLV/chi phí (ch.6), báo cáo Odoo/Looker (ch.7), phân công, mã nguồn
- Việc kế tiếp: dựng Odoo bằng docker compose, tạo DB, cài CRM/Sales/Inventory/Email Marketing (mục 4.1-4.2)

---

## Phiên 1 - 29/10/2026
- Mục tiêu: lên kế hoạch và dựng khung đồ án
- Đã làm:
  - Rà soát CRM.zip (chỉ có tài liệu, không có mã nguồn)
  - Đọc đồ án mẫu Decharmix (84 trang, 8 phần) và lập bảng so khớp với phần nhóm đã có
  - Chốt đề bài: 1 PDF báo cáo + mã nguồn + demo Odoo
  - Tạo repo mẫu có docker-compose, scripts backup/restore, README quy tắc nhóm
- File tạo ra: CRM_LOG.md, crm-dominos-starter.zip, SESSION_LOG.md
- Ghi chú: link Drive không đọc được nội dung, chỉ thấy tên thư mục
- Kế tiếp: Phiên 2 bắt đầu từ cài đặt Odoo (4.1), sau đó 4.3-4.5

---

## Mẫu cho phiên mới
## Phiên N - dd/mm/2026
- Mục tiêu:
- Đã làm:
- File/kết quả:
- Vấn đề gặp phải:
- Kế tiếp:

- [Phiên 1, bổ sung] Đã chia việc cho 3 thành viên (xem PHAN_CONG.md, đặt vào docs/). A = Hà Yến Linh (Odoo, repo, ghép PDF), B = Trần Hoàng Ngọc Lan (sản phẩm, dữ liệu, CLV), C = Phạm Phương Ái Linh (BPMN, báo cáo, văn bản).

## Phiên 2 - 06/11/2026 (vai trò A: Odoo Developer & System Specialist)
- Mục tiêu: Bước 1 - dựng Odoo bằng Docker (mục 4.1)
- Đã làm: chạy docker compose up -d trên Windows (Docker 29.9.2, Compose v5.6.1); trang http://localhost:8069 hiện ra -> ĐẠT
- File cập nhật: README.md (thêm mục môi trường đã kiểm thử), CRM_LOG.md
- Kế tiếp: Bước 2 - tạo database, tiếng Việt, tắt demo data, cài CRM/Sales/Inventory/Email Marketing
- [Phiên 2, Bước 2 - ĐẠT] Database `dominos`, Odoo 17.0-20260908 Community, Tiếng Việt. Đã cài CRM, Bán hàng, Tồn kho, Email Marketing (+ Xuất hóa đơn, Liên hệ, Lịch, Thảo luận); không lỗi. Cập nhật README, .env.example (DB_NAME=dominos), backup.sh. Kế tiếp: Bước 3 - tạo user và phân quyền theo user classes.

## Phiên 2 (tiếp) - 06/11/2026: Rà soát bộ quy trình theo bộ tiêu chí chấm
- Tạm dừng Bước 3 (user/phân quyền, chờ xác nhận 5 user). Đọc Phan_5_Quy_trinh_CRM_Dominos.docx (9 as-is, QT-01/02/03) và tiêu chí A4.1-A4.12.
- Phát hiện chính: (1) Helpdesk là Enterprise, Community không có -> dùng CRM pipeline hoặc module tự viết; (2) thiếu quy trình lead->cơ hội->báo giá->đơn->hóa đơn + lý do thất bại; (3) cần 1 quy trình nhóm + mỗi người >=1 quy trình khác; (4) mới có Mermaid, chưa có .bpmn Camunda, chưa có phần "thực hiện quy trình" trên Odoo; (5) chưa thấy A4.7 API/webhook, A4.8 WP+Woo, A4.9 hai module, A4.5, A4.10, A4.11.
- Đề xuất: thêm QT-04 (nhóm, Lead-to-Loyalty, đa phòng ban); QT-01/02/03 làm quy trình cá nhân (mỗi người 1).
- Chờ nhóm thống nhất: số nhóm XX; chốt 6 điểm mâu thuẫn ở mục 5.4; nhãn nguồn T4 (EC213.Q11 Nhóm 2 hay R12 Nhóm 3); phân công QT cá nhân; cách xử lý Helpdesk/Zalo/Looker trên Community.
- Kế tiếp: sau khi nhóm chốt, quay lại Bước 3 và soạn QT-04.
- [Phiên 2, Bước 3b - ĐẠT] Chốt nền tảng: Odoo Community 17.0 + OCA helpdesk_mgmt (đã cài thành công, addons/oca-helpdesk). Cập nhật README, config/odoo.conf (addons_path). Việc kế: sửa mục 5.3 tài liệu quy trình (bỏ Helpdesk Enterprise), quay lại Bước 3 (user/phân quyền, chờ xác nhận 5 user + quy ước email).