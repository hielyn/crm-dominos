# CRM Domino's Pizza - EC213 (Odoo 17 trên Docker)

## Chạy lần đầu
1. `cp .env.example .env` rồi sửa mật khẩu
2. Sửa `admin_passwd` trong `config/odoo.conf`
3. `docker compose up -d`
4. Mở http://localhost:8069, tạo database tên `dominos` (trùng `DB_NAME`), chọn Tiếng Việt, tắt Demo data
5. Cài app: CRM, Sales, Inventory, Email Marketing

## Quyết định nền tảng (06/11/2026)
- Odoo **Community 17.0** tự cài (Docker), KHÔNG dùng Enterprise/bản dùng thử
- Ticket khiếu nại: module cộng đồng OCA `helpdesk_mgmt` (nhánh 17.0), đặt tại `addons/oca-helpdesk/`
- SLA, cảnh báo, leo thang: tự cấu hình/viết (trường hạn xử lý, Automated Action, Schedule Activity)
- Cài lại trên máy mới: `cd addons`, `git clone --depth 1 --branch 17.0 https://github.com/OCA/helpdesk.git oca-helpdesk`, xóa `oca-helpdesk/.git`, `docker compose restart odoo`, bật chế độ nhà phát triển > Apps > Cập nhật danh sách ứng dụng > cài Helpdesk Management

## Môi trường đã kiểm thử
- Odoo 17.0-20260908 Community, database `dominos`, ngôn ngữ Tiếng Việt, không demo data
- Đã cài: CRM, Bán hàng, Tồn kho, Email Marketing, Helpdesk Management (OCA) (kèm Xuất hóa đơn, Liên hệ, Lịch, Thảo luận)
- Windows, Docker 29.9.2, Docker Compose v5.6.1, Odoo 17.0 (image `odoo:17.0`), PostgreSQL 15
- Trên Windows dùng PowerShell: `copy .env.example .env`. Script `.sh` chạy bằng Git Bash hoặc WSL.

## Quy tắc làm việc nhóm
- Nhánh: `main` (ổn định, chỉ merge qua Pull Request), mỗi người 1 nhánh `ten/chuc-nang` (vd `lan/pipeline`)
- Commit: `[phan] noi dung` (vd `[4.7] cau hinh pipeline`)
- Cấu hình Odoo nằm trong DB: sau mỗi mốc chạy `./scripts/backup.sh`; 1 người giữ bản backup chính, chia sẻ qua Drive (file lớn, không commit)
- Ảnh chụp đặt tên theo mục báo cáo: `docs/screenshots/4.7_pipeline.png`
- Nhật ký làm việc: `docs/LOG.md`

## Cấu trúc
config/ cấu hình Odoo | addons/ module tùy chỉnh | data/ CSV mẫu | db_backup/ dump DB
scripts/ backup, restore | docs/report báo cáo | docs/bpmn sơ đồ | docs/screenshots ảnh | docs/reference tài liệu tham khảo