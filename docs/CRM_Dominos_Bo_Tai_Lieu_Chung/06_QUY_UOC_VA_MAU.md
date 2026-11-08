# 06 - Quy ước và mẫu
## Đặt tên file nộp (theo rubric, thay XX bằng số nhóm khi có)
- Nhóm: `[Tên quy trình] - Nhóm XX.bpmn`, `... .png`, `Report - Nhóm XX.docx`
- Cá nhân: `[Tên quy trình] - MSSV - [Họ và tên].bpmn/.png/.docx`; video `Thao tác CRM - MSSV - [Họ và tên].mp4`; API `API - MSSV - [Họ và tên].docx`
- Ảnh chụp màn hình: `docs/screenshots/<mục>_<mô tả>.png` (vd `4.7_pipeline.png`)
## Git (repo nhóm trên GitHub)
- `main` chỉ merge qua Pull Request; mỗi người 1 nhánh `ten/chuc-nang` (vd `lan/rfm`); commit `[mục] nội dung`.
- KHÔNG commit: `.env`, mật khẩu, API key, file backup DB lớn (đã có trong `.gitignore`).
- Cấu trúc repo: `config/`, `addons/` (module + `oca-helpdesk/`), `data/` (CSV mẫu), `db_backup/`, `scripts/`, `docs/` (`report/`, `bpmn/`, `screenshots/`, `reference/`, `LOG.md`, `SESSION_LOG.md`).
## Nhật ký (mỗi bước, ghi vào `docs/SESSION_LOG.md`)
```
- [dd/mm] [Vai trò A/B/C] Việc: ... | Kết quả: đạt/không đạt | Vướng mắc: ... | Kế tiếp: ...
```
## BPMN
- Vẽ bằng **Camunda Modeler bản cài trên máy**; xuất `.png`/`.pdf` từ file `.bpmn`. C ban hành mẫu file (lanes, ký hiệu, mã Activity) trước 11/11; đến lúc đó theo khuôn quy trình trong `nguon/02`.
## Khung mô tả quy trình (theo khuôn QT trong `nguon/02`; không đổi tên mục khi chưa thống nhất)
Mục tiêu | Tác nhân | Điều kiện kích hoạt | Các bước (bảng Activity) | Ngoại lệ | Đầu ra | KPI | Ánh xạ FR/NFR | Cấu hình Odoo tương ứng. Phần "Thực hiện quy trình" = ảnh chụp từng bước trên Odoo của người làm, đánh số theo bước.
## Quy ước dữ liệu mẫu (xem thêm mục B1 của file 04)
- Mã khách/sản phẩm dùng thống nhất giữa mọi file CSV; email khách dùng địa chỉ giả; không dùng dữ liệu cá nhân thật.
- Ngày đơn trải 4-6 tháng để RFM có cửa sổ 30-60 ngày.
## Cách ghi điều chưa chắc
- Dùng nhãn `[CẦN XÁC NHẬN]` (chưa có thông tin), `[ĐỀ XUẤT]` (AI/người đề nghị, chưa chốt), `(chưa kiểm chứng)` (chưa chạy thử).
