# Nhật ký đồ án CRM - Domino's Pizza (EC213)

Nhóm: Hà Yến Linh (nhóm trưởng, 24520954), Trần Hoàng Ngọc Lan (24520944), Phạm Phương Ái Linh (24520967)
GVHD: ThS. Văn Đức Sơn Hà

## Bước 0 - Rà soát tài liệu hiện có (xong)
- CRM.zip chỉ có tài liệu, KHÔNG có mã nguồn:
  - Báo cáo chính (29 trang): giới thiệu doanh nghiệp, thu thập yêu cầu (phỏng vấn giả định), System Requirements (FR/NFR, ma trận truy vết)
  - 5 GAPS (12 trang): giải pháp G1.1-G5.4, gắn mã FR/NFR
  - Practice 6-7 (20 trang): user classes (KH, TN, CHT, CSKH, MKT, BQL, ADM, BEP)
  - Tuần 4: bảng mô hình phân khúc (RFM, VALS, K-Means, GMM, SOM) + bài báo tham khảo
- Link Drive tham khảo: thư mục "[EC213.Q11 - NHÓM 2] - BÁO CÁO ĐỒ ÁN CRM" (không đọc được nội dung file bên trong, chỉ thấy tên thư mục; cần liệt kê tên file hoặc tải lên)
- Kết luận: đồ án nghiêng về báo cáo phân tích/thiết kế CRM, chưa rõ có yêu cầu prototype hay không

## Cấu trúc thư mục đề xuất
```
CRM_Dominos/
├── 01_BaoCao/        # báo cáo chính (bản .docx + .pdf)
├── 02_BaiTapTuan/    # các bài tuần 1-4+, 5 Gaps, Practice 6-7
├── 03_ThamKhao/      # đồ án mẫu, bài báo, bảng mô hình
├── 04_ThietKe/       # use case, ERD, wireframe (khi tới bước này)
├── 05_Prototype/     # CHỈ tạo nếu đề yêu cầu có mã nguồn
└── LOG.md
```

## Dự định các bước tiếp theo
1. Xác nhận sản phẩm cuối (báo cáo thuần hay có prototype), hạn nộp, rubric
2. Lập bảng so khớp mục lục đồ án mẫu với phần nhóm đã có -> tìm phần còn thiếu
3. Viết các phần còn thiếu theo thứ tự ưu tiên
4. Thiết kế (use case, quy trình, ERD) bám theo mã FR/NFR hiện có
5. (Nếu cần) Prototype CRM
6. Rà soát nhất quán mã FR/NFR, tài liệu tham khảo, nộp bài

## Bước 1 - Chốt đề bài và so khớp đồ án mẫu (xong, 29/10)
- Sản phẩm nộp: 1 PDF báo cáo + mã nguồn liên quan + demo Odoo (ưu tiên Odoo). Hạn 16/11. Chưa có rubric.
- Đồ án mẫu (Decharmix, Nhóm 2, 84 trang) gồm: 1 Mở đầu/danh mục | 2 Tổng quan (lý do, mục tiêu, công cụ: Odoo Community + Camunda + Sheets/Canva/WordPress/Notion) | 3 Sản phẩm, phân khúc, persona | 4 Cấu hình Odoo (cài đặt, ngôn ngữ/tiền tệ, user/phân quyền, mail, sales team, pipeline, lead, lý do thất bại, layout, sản phẩm, NVL, BOM) | 5 Quy trình điển hình (BPMN + bảng mô tả + chạy thật trên Odoo) | 6 Chi phí, CLV | 7 Báo cáo có sẵn + Looker Studio | 8 Phân công/đánh giá
- Đã có từ các tuần trước: giới thiệu DN, SWOT, pain points (ch.1), phỏng vấn, FR/NFR (ch.2-3), 5 Gaps, user classes, bảng mô hình phân khúc (RFM, K-Means...)
- Còn thiếu (so với mẫu): triển khai Odoo (ch.4), quy trình BPMN + chạy demo (ch.5), CLV/chi phí (ch.6), báo cáo Odoo/Looker (ch.7), phân công, mã nguồn

## Cấu trúc mã nguồn/demo bổ sung
```
05_Prototype/
├── docker-compose.yml     # dựng Odoo + PostgreSQL
├── odoo.conf
├── data/                  # CSV/XML: sản phẩm, khách hàng mẫu, lead mẫu, pipeline stages
├── addons/                # module tùy chỉnh (nếu có)
├── db_backup/             # file dump DB sau khi cấu hình xong
└── screenshots/           # ảnh chụp cho báo cáo, đặt tên theo mục (4.3_user.png...)
```

## Lịch dự kiến (29/10 -> 16/11)
- 29/10-31/10: Bước 2 dựng Odoo + cấu hình nền (mục 4.1-4.5)
- 1/11-5/11: Bước 3 sales team, pipeline, lead, sản phẩm Domino's (4.6-4.13) + dữ liệu mẫu
- 6/11-9/11: Bước 4 quy trình BPMN + chạy demo end-to-end (ch.5)
- 10/11-12/11: Bước 5 CLV, báo cáo Odoo/Looker (ch.6-7)
- 13/11-15/11: Bước 6 ghép báo cáo PDF, đóng gói mã nguồn, rà soát
- 16/11: nộp

## Nhật ký chi tiết
- [Bước 0] Đã rà soát tài liệu, xem mục trên.
- [Bước 1] Đã đọc đồ án mẫu, lập bảng so khớp và lịch. Bước kế: dựng Odoo.
- [Bước 2a] Chốt: Odoo 17 Community trên Docker + GitHub chung. Đã tạo repo mẫu crm-dominos-starter.zip (docker-compose, config, scripts backup/restore, README quy tắc nhóm). Bước kế: giải nén, chạy docker compose up, tạo DB, cài app CRM/Sales/Inventory/Email Marketing (mục 4.1-4.2).
- [Bước 2b] Phân công 3 người, xem PHAN_CONG.md.
- [Bước 1 - A] Odoo 17 chạy trên Docker (Windows), truy cập localhost:8069 thành công (06/11).
- [Bước 2 - A] Tạo DB dominos, cài CRM/Sales/Inventory/Email Marketing thành công (06/11).
- [Bước 3b - A] Chốt Odoo Community 17.0 + OCA helpdesk_mgmt, cài thành công (06/11).