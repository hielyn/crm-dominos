# GUIDELINE V2 - Đồ án CRM Domino's Pizza (cập nhật 07/11/2026, nộp 23/11)

Thay thế phần "Guideline chi tiết" của CRM TỔNG 4. Ký hiệu: **(BB)** bắt buộc, **(TC)** tùy chọn khi còn thời gian. Mục [?] chờ nhóm chốt.
Vai trò: **A** = Odoo Developer & System Specialist (Hà Yến Linh) | **B** = Data & Analytics (Trần Hoàng Ngọc Lan) | **C** = BA & Process Lead (Phạm Phương Ái Linh).

## 0. Quy tắc chung
- Nền tảng: Odoo Community 17.0 (Docker) + OCA `helpdesk_mgmt`; WordPress + WooCommerce; Camunda Modeler (mức 1) + engine (mức 2, sau 13/11). Chi tiết: HE_THONG_VA_QUY_TRINH_V2.md.
- **Odoo riêng của mỗi người:** clone repo, `docker compose up -d`, tự tạo DB (hoặc restore backup của A), **đổi email admin thành email sinh viên của mình, đổi avatar tài khoản chính**, bật cả **Tiếng Anh và Tiếng Việt**, tiền tệ VND, múi giờ Việt Nam.
- Git: nhánh `main` chỉ merge qua Pull Request; mỗi người 1 nhánh `ten/chuc-nang`; commit `[mục] nội dung`.
- Tên file nộp: nhóm `[Tên] - Nhóm XX.ext`; cá nhân `[Tên] - MSSV - [Họ và tên].ext`. Ảnh chụp: `docs/screenshots/<mục>_<mô tả>.png`.
- Nhật ký: mỗi người ghi 3-5 dòng/ngày vào `docs/SESSION_LOG.md` (làm gì, kết quả, vướng gì).
- Họp nhóm 10 phút mỗi ngày: hôm qua làm gì, hôm nay làm gì, đang bị chặn ở đâu.
- Mỗi quy trình cá nhân đủ **5 thứ**: `.bpmn` (mở bằng Camunda Modeler bản cài máy), `.png/.pdf` xuất ra, mô tả chi tiết, thực hiện trên Odoo (có ảnh), API doc; cộng **video** A4.4 (quay màn hình, có mặt và giọng nói, thấy Odoo do chính mình cài).

## 1. Mốc chung (hạn nộp **23/11**, đã dời từ 16/11)
| Hạn | Mốc |
|---|---|
| 8-9/11 | Nhóm chốt GUIDELINE V2; số nhóm XX; A xong hạ tầng (Odoo, mail, WordPress) |
| 11/11 | **Dataset v1 (B), bảng quy tắc loyalty (C), backup DB + hướng dẫn restore (A), mẫu BPMN (C)** giao cho cả nhóm |
| 13/11 | BPMN nháp 4 quy trình bắt buộc; module khung (A, B); thử script Sheets/Looker (B) |
| 17/11 | Chạy xong quy trình trên Odoo + ảnh chụp; module hoàn chỉnh; bắt đầu Camunda mức 2 nếu phần bắt buộc đã xong |
| 20/11 | **Chốt tính năng:** nộp đủ ảnh, docx, video, API doc cho C; quy trình tùy chọn xong hoặc cắt |
| 21-22/11 | C ghép PDF; A đóng gói zip, thử clone repo sạch; rà soát chéo; đệm cho sự cố |
| 23/11 | Nộp (nên nộp sớm trong ngày) |

## 2. VAI TRÒ A - Odoo Developer & System Specialist
**Mục tiêu:** dựng và vận hành hệ thống Odoo + website, viết module, đóng gói mã nguồn; hoàn thành P1 (BB) và P5 (TC).
**Công việc**
1. **Hạ tầng (đang làm):** `docker compose up -d` với Odoo, PostgreSQL, Mailpit, WordPress, MariaDB; cấu hình máy chủ thư đi (SMTP `mailpit:1025`); bật module Automation Rules, Point of Sale, Discount & Loyalty, Leads, Mẫu báo giá. *Xong khi:* 5 dịch vụ Up, gửi mail thử thấy trong Mailpit.
2. **Cấu hình nền (A4.2.1):** ngôn ngữ EN+VI, VND, múi giờ; avatar admin; 7 user + RBAC (TN, CHT, CSKH, MKT, Sales B2B, KT, BQL) theo bảng quyền đã chốt; **Sales team** (Online, Hotline, POS, Đơn tiệc, hoặc theo cửa hàng); **pipeline** (stage), **lead**, **lý do thất bại**; **layout tài liệu** báo giá và hóa đơn (logo, màu, chân trang). Chụp ảnh từng mục.
3. **Customer 360:** trường tùy chỉnh trong module (sở thích món, ngày sinh, kênh đặt chính, hạng, điểm), nút xem đơn/ticket/lead trên hồ sơ khách.
4. **Module `dominos_crm_extension`:** ADT/EDT và cờ giao trễ trên đơn; SLA trên ticket `helpdesk_mgmt` (hạn xử lý, Automated Action, Schedule Activity "Xác minh sự cố" 15 phút cho CHT, cờ EX-2 tạo Activity khẩn cấp cho QC); nút **Duyệt đền bù 3 bước** sinh mã voucher WOW và gửi email; hạng thành viên và voucher sinh nhật tự động (phối hợp C về quy tắc). *Xong khi:* cài được trên Odoo sạch và chạy hết kịch bản QT-P5.
5. **Website:** WordPress + WooCommerce với 10-15 sản phẩm; Contact Form 7/WPForms cho form đơn tiệc; 1 plugin giỏ bị bỏ (chọn và thử ở bước này). **Tích hợp JSON-RPC** (`wp_remote_post` tới `http://odoo:8069/jsonrpc`, dùng API key): đơn Woo thành `sale.order` + khách; form thành `crm.lead` có trường nguồn/chiến dịch; giỏ bị bỏ thành nhãn/Activity trên khách để B làm email nhắc.
6. **Đơn đa kênh:** POS (app Point of Sale cho quầy), hotline nhập tay vào Sales, mô phỏng Grab/Shopee bằng nhập CSV.
7. **QT-P1 Đơn đa kênh + Customer 360 (BB), QT-P5 Khiếu nại WOW (TC):** BPMN, mô tả, thực hiện, **API doc `sale.order` create**, video.
8. **A4.7 nhóm:** file "Tìm hiểu API - Nhóm XX" giải thích cách khám phá API Odoo (XML-RPC/JSON-RPC, API key), ví dụ gọi thật; phần webhook ghi rõ Odoo 17.0 chưa có sẵn (cần kiểm tra) và cách thay thế.
9. **Camunda mức 2 (sau 17/11):** engine trong Docker, gọi Odoo qua REST/JSON-RPC cho 1 luồng đơn giản; chọn phiên bản Camunda hiện hành khi bắt đầu.
10. **Đóng gói:** `addons/` có module và OCA helpdesk; backup DB (`scripts/backup.sh`); README cập nhật; hướng dẫn B, C restore và đổi email admin; zip mã nguồn module (A4.9); thử clone sạch trên máy khác.
**Đầu ra:** hệ thống chạy, module (zip), ảnh cấu hình, QT-P1/P5 đủ bộ, tài liệu API nhóm, video A4.4.

## 3. VAI TRÒ B - Data & Analytics Specialist
**Mục tiêu:** dữ liệu chuẩn QSR dùng chung, RFM, CLV/ABC, báo cáo và Looker Studio; hoàn thành P3 (BB) và P4 (TC).
**Công việc**
1. **Dataset v1 (hạn 11/11), gợi ý cấu trúc:**
   - Khách: 50+, chia Gen Z / Văn phòng / Gia đình; tên, SĐT, email giả, ngày sinh, địa chỉ, sở thích món, kênh, ngày đăng ký, hạng, điểm.
   - Sản phẩm/combo: 30+; nhóm, giá bán, chi phí nguyên liệu (cho ABC).
   - Đơn: 100+ qua 4 kênh (Website, App, Hotline, POS), **trải 4-6 tháng** để có cửa sổ 30-60 ngày; ngày, kênh, cửa hàng, tổng tiền, ADT thực tế.
   - Ticket 15+ (loại, thời gian xử lý, CSAT), lead B2B 15+, giỏ bị bỏ 10+, thống kê email (gửi, mở, click).
   - Mọi bảng dùng chung mã khách/sản phẩm; file CSV theo thứ tự import Odoo. *Xong khi:* import sạch vào Odoo của B không lỗi và A, C dùng được.
2. **Import vào Odoo** (Odoo riêng của B), rồi bàn giao file cho A, C.
3. **Module `dominos_report`:** tác vụ định kỳ (cron) tính R, F, M, chấm điểm (quintile hoặc ngưỡng) và gán nhãn: mới, thường xuyên, VIP, at-risk (30-60 ngày không mua), không mua lại; lưu vào hồ sơ khách; có báo cáo pivot/đồ thị. Phối hợp A để không trùng trường.
4. **Email marketing:** danh sách theo segment; mẫu welcome, sinh nhật, newsletter, at-risk, nhắc giỏ bỏ; gửi qua Mailpit; thống kê mở/click của Odoo (cần thử xem chạy được trong môi trường local).
5. **QT-P3 RFM + tái kích hoạt (BB), QT-P4 Email marketing + analytics campaign (TC):** BPMN, mô tả, thực hiện, **API doc `search_read`/`read_group`**, video.
6. **CLV + ABC (A4.5):** CLV = AOV x tần suất/năm x thời gian gắn bó; ABC với bể chi phí (voucher đền bù, giao trễ, marketing); phân bổ vào sản phẩm/kênh. ABC làm trên Sheets từ dữ liệu Odoo; thử Odoo analytic nếu kịp [?].
7. **Báo cáo A4.6:** báo cáo CRM và Sales có sẵn của Odoo, nhóm theo team, theo tháng, biểu đồ phù hợp; chụp và giải thích.
8. **Looker Studio:** script Python (JSON-RPC) chạy trên máy, ghi vào Google Sheets (hoặc xuất CSV), lập lịch cập nhật; **thử sớm (13/11)**. Dashboard: DOT, SLA ticket, doanh thu theo kênh, CSAT/NPS, cộng open rate, CTR, repeat purchase, churn, CLV, doanh thu theo campaign.
9. **Viết báo cáo:** Phần 6, 7, A4.5, A4.6.
**Đầu ra:** dataset CSV, module báo cáo (zip), QT-P3/P4 đủ bộ, tài liệu CLV/ABC, link Looker, video A4.4.

## 4. VAI TRÒ C - BA & Process Lead
**Mục tiêu:** tài liệu nghiệp vụ nhất quán, chuẩn BPMN, quy trình nhóm, tổng hợp báo cáo và nộp; hoàn thành P2 (BB) và P6 (TC).
**Công việc**
1. **Tài liệu BA (Phần 1, 2, 3, 5):** FR/NFR, Use Cases, 5 Gaps, 3 personas; **A4.1 case study**; dọn ghi chú nội bộ (nhãn T4/B1/TK, "người viết"); **kiểm chứng từng trích dẫn** (hai nguồn trùng đường dẫn, một nguồn thiếu link).
2. **Chuẩn BPMN cho cả nhóm:** cài Camunda Modeler bản cài máy; mẫu file (lanes, ký hiệu, quy ước đặt tên và mã Activity); review BPMN của A, B trước 14/11.
3. **QT-T quy trình nhóm (BB):** hai tác nhân (30-60 ngày không mua; bỏ giỏ hàng); BPMN, mô tả chi tiết, bảng Activity, kịch bản test; A và B chạy trên Odoo chung, C tổng hợp ảnh.
4. **QT-P2 Loyalty (BB):**
   - Hạn 11/11: bảng quy tắc (tỷ lệ tích điểm, ngưỡng hạng, đổi quà, voucher sinh nhật) do nhóm quyết [?]; giao cho A để lập trình.
   - Cấu hình Discount & Loyalty trên Odoo riêng, BPMN, mô tả, thực hiện, **API doc** (`loyalty.card` hoặc `crm.lead`), video.
5. **QT-P6 Đơn tiệc B2B (TC)** + lead form WordPress: phối hợp A; pipeline, báo giá, hóa đơn, lý do thất bại.
6. **Ma trận truy vết:** FR/NFR, quy trình, tính năng Odoo, tiêu chí A4.x; cập nhật mục 5.4 theo rubric thật.
7. **A4.10 và A4.11:** đề xuất khác biệt (ví dụ WOW Service có tự động duyệt, hoặc quản lý đồng ý dữ liệu cá nhân) và đánh giá đề xuất CRM.
8. **Danh sách thành viên:** trách nhiệm từng người và **mức tham gia công việc chung** (rubric yêu cầu).
9. **Tổng hợp và nộp:** ghép PDF, thư mục `Cá nhân`, tên `Nhóm XX - Đồ án CRM.zip`; kiểm tra file nào cũng mở được; thử giải nén.
10. **Điều phối:** bảng theo dõi tiến độ, chạy họp 10 phút, chốt các điểm [?].
**Đầu ra:** tài liệu BA, QT-T và QT-P2 đủ bộ, ma trận, A4.1/4.10/4.11, danh sách thành viên, PDF cuối, video A4.4.

## 5. Bàn giao giữa các vai trò
| Từ | Cho | Gì | Hạn |
|---|---|---|---|
| C | A | Bảng quy tắc loyalty, Activity/SLA cho QT-P5 | 11/11 |
| B | A, C | Dataset v1 (CSV) | 11/11 |
| A | B, C | Backup DB + hướng dẫn restore, đổi email admin | 11/11 |
| A | B | Trường partner, quy ước tên trường RFM | 11/11 |
| C | A, B | Mẫu BPMN và quy ước đặt tên | 11/11 |
| B | cả nhóm | Kết quả thử script Sheets/Looker | 13/11 |
| Cả nhóm | C | Ảnh, docx, video, API doc | 20/11 |

## 6. Tiêu chí rubric và người phụ trách
| Tiêu chí | Chính | Phối hợp |
|---|---|---|
| A4.1 Case study | C | |
| A4.2.1 Cài đặt, cấu hình | A | mỗi người trên Odoo riêng |
| A4.2.2 Dữ liệu nhập | B | A, C |
| A4.3.1 Quy trình nhóm | C | A, B |
| A4.3.2 Quy trình cá nhân | mỗi người | |
| A4.4 Video | mỗi người | |
| A4.5 CLV, ABC | B | |
| A4.6 Báo cáo | B | |
| A4.7 API | A (nhóm), mỗi người (cá nhân, API khác nhau) | |
| A4.8 Lead form, Woo | A | C (form) |
| A4.9.1 Module chức năng | A | |
| A4.9.2 Module báo cáo | B | |
| A4.10, A4.11 | C | |
| Danh sách thành viên | C | |

## 7. Ưu tiên khi thiếu thời gian (cắt từ dưới lên)
1. Không cắt: A4.2 (cấu hình, dữ liệu), A4.3 (QT-T + 3 quy trình bắt buộc, đủ 5 thứ), A4.4 (video), A4.9 (hai module), A4.5, A4.6, A4.7.
2. Cắt thứ nhất: Camunda mức 2.
3. Cắt thứ hai: QT-P4, QT-P5, QT-P6 (tùy chọn).
4. Giữ phần Looker ở mức tối thiểu (4 khối) hoặc CSV nếu script Sheets không chạy.
