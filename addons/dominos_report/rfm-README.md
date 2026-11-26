# Module `dominos_report` — Phân tích & Báo cáo RFM (Odoo 17.0)

Module tùy chỉnh phục vụ đồ án **CRM Domino's Pizza (EC213 - Task A4.9.2)**, tự động hóa việc tính toán chỉ số **RFM (Recency – Frequency – Monetary)**, chấm điểm ngũ phân vị (1–5), phân loại tệp khách hàng định kỳ và cung cấp báo cáo trực quan (Pivot Table & Bar Chart) trên Odoo Community 17.0.

---

## 1. Thông tin chung

* **Tên kỹ thuật:** `dominos_report`
* **Phiên bản Odoo:** `17.0.1.0.0`
* **Phụ thuộc (`depends`):** `base`, `contacts`, `sale_management`
* **Phụ trách phát triển:** Trần Hoàng Ngọc Lan (`tlan/rfm`)

---

## 2. Cấu trúc thư mục

```text
addons/dominos_report/
├── __init__.py                 # Khai báo nạp thư mục models
├── __manifest__.py             # Khai báo metadata, dependencies và danh sách file XML
├── README.md                   # Tài liệu hướng dẫn kỹ thuật và vận hành module
├── data/
│   └── ir_cron.xml             # Cấu hình Scheduled Action chạy tự động mỗi ngày
├── models/
│   ├── __init__.py             # Khai báo nạp res_partner.py
│   └── res_partner.py          # Logic tính RFM, chấm điểm 1-5 và phân khúc khách hàng
└── views/
    ├── res_partner_views.xml   # Giao diện tab RFM trên hồ sơ khách & bộ lọc Contacts
    └── rfm_report_views.xml    # Giao diện báo cáo Pivot, biểu đồ cột và menu Báo cáo RFM
```

---

## 3. Trường dữ liệu mở rộng trên `res.partner`

Module kế thừa model `res.partner` và bổ sung 8 trường dữ liệu chỉ đọc (`readonly=True`) với tiền tố `x_dom_rfm_` để tránh xung đột với các module khác của nhóm:

| Tên trường (Technical Name) | Kiểu dữ liệu | Nhãn hiển thị | Mô tả |
| :--- | :--- | :--- | :--- |
| `x_dom_rfm_segment` | `Selection` | Phân khúc RFM | Nhãn phân loại: `Mới`, `Thường xuyên`, `VIP`, `At-risk (30-60 ngày)`, `Không mua lại` |
| `x_dom_rfm_r` | `Integer` | Điểm R (Recency) | Điểm ngũ phân vị độ mới mua hàng (thang 1–5) |
| `x_dom_rfm_f` | `Integer` | Điểm F (Frequency) | Điểm ngũ phân vị tần suất mua hàng (thang 1–5) |
| `x_dom_rfm_m` | `Integer` | Điểm M (Monetary) | Điểm ngũ phân vị giá trị chi tiêu (thang 1–5) |
| `x_dom_rfm_recency_days` | `Integer` | Số ngày từ đơn gần nhất | Khoảng cách ngày từ đơn xác nhận gần nhất đến ngày tham chiếu |
| `x_dom_rfm_order_count` | `Integer` | Tổng số đơn đã mua | Tổng số đơn hàng ở trạng thái `sale` hoặc `done` |
| `x_dom_rfm_total_spent` | `Float` | Tổng chi tiêu (VNĐ) | Tổng giá trị `amount_total` của các đơn đã xác nhận |
| `x_dom_rfm_last_computed` | `Datetime` | Thời điểm tính RFM | Dấu thời gian lần chạy Cron cập nhật dữ liệu gần nhất |

---

## 4. Phương pháp tính điểm & Phân khúc RFM

### 4.1. Phạm vi dữ liệu đầu vào
* Chỉ tổng hợp các đơn bán hàng (`sale.order`) đã xác nhận (`state` thuộc `['sale', 'done']`) và có ngày đặt hàng `date_order <= ref_dt`.
* Bỏ qua các đơn ở trạng thái báo giá nháp (`draft`) hoặc đã hủy (`cancel`).

### 4.2. Chấm điểm ngũ phân vị (Quintile Scoring 1–5)
Tập khách hàng có phát sinh đơn hàng được sắp xếp và chia thành 5 nhóm bằng nhau (mỗi nhóm 20%):
* **Điểm R (`x_dom_rfm_r`):** Sắp xếp tăng dần theo `recency_days` — khách mua càng gần đây điểm càng cao (`5` là mới nhất, `1` là lâu nhất).
* **Điểm F (`x_dom_rfm_f`):** Sắp xếp tăng dần theo `order_count` — số đơn càng nhiều điểm càng cao (`1` đến `5`).
* **Điểm M (`x_dom_rfm_m`):** Sắp xếp tăng dần theo `total_spent` — tổng chi tiêu càng lớn điểm càng cao (`1` đến `5`).

### 4.3. Quy tắc gán nhãn phân khúc (theo thứ tự ưu tiên)

| Mã lưu (`key`) | Nhãn hiển thị | Điều kiện áp dụng mặc định | Ý nghĩa nghiệp vụ |
| :--- | :--- | :--- | :--- |
| `lost` | **Không mua lại** | `recency_days > 60` | Khách rời bỏ (> 60 ngày chưa phát sinh đơn mới) |
| `at_risk` | **At-risk (30-60 ngày)** | `30 <= recency_days <= 60` | Khách có nguy cơ rời bỏ — đầu vào cho chiến dịch tái kích hoạt (QT-P3) |
| `new` | **Mới** | `recency_days < 30` và `order_count <= 2` | Khách mới mua trong vòng 30 ngày với tối đa 2 đơn |
| `vip` | **VIP** | `recency_days < 30` và `order_count >= 8` | Khách hàng trung thành tần suất cao (từ 8 đơn trở lên) |
| `regular` | **Thường xuyên** | `recency_days < 30` và `3 <= order_count <= 7` | Khách hàng duy trì mua sắm ổn định |

### 4.4. Tham số hệ thống (`ir.config_parameter`)
Có thể điều chỉnh linh hoạt mốc thời gian và ngưỡng phân khúc tại **Thiết lập $\rightarrow$ Kỹ thuật $\rightarrow$ Tham số hệ thống**:

| Key | Giá trị mặc định | Ghi chú |
| :--- | :--- | :--- |
| `dominos_report.as_of_date` | *(Trống = ngày hiện tại)* | Đặt `2026-11-10` để cố định mốc kiểm thử khớp với bộ Dataset v1 |
| `dominos_report.at_risk_min_days` | `30` | Ngưỡng ngày tối thiểu của nhóm At-risk |
| `dominos_report.at_risk_max_days` | `60` | Ngưỡng ngày tối đa của nhóm At-risk (vượt ngưỡng chuyển sang `lost`) |
| `dominos_report.new_max_orders` | `2` | Số đơn tối đa để xếp vào nhóm Mới |
| `dominos_report.vip_min_orders` | `8` | Số đơn tối thiểu để xếp vào nhóm VIP |

---

## 5. Hướng dẫn cài đặt và chạy kiểm thử

1. **Nạp module vào môi trường Odoo Docker:**
   * Đảm bảo thư mục `dominos_report` nằm trong đường dẫn `addons` đã khai báo ở `odoo.conf`.
   * Khởi động lại container Odoo (`docker compose restart odoo` hoặc `docker restart <tên_container>`).
2. **Kích hoạt module:**
   * Đăng nhập Odoo $\rightarrow$ **Thiết lập (Settings)** $\rightarrow$ bật **Chế độ nhà phát triển (Developer Mode)**.
   * Vào **Ứng dụng (Apps)** $\rightarrow$ bấm **Cập nhật danh sách ứng dụng (Update Apps List)** $\rightarrow$ tìm `dominos_report` và bấm **Kích hoạt (Activate)**.
3. **Cấu hình ngày tham chiếu cho Dataset v1:**
   * Vào **Thiết lập $\rightarrow$ Kỹ thuật $\rightarrow$ Tham số hệ thống (System Parameters)** $\rightarrow$ tạo mới tham số với Key `dominos_report.as_of_date` và Value `2026-11-10`.
4. **Chạy Cron tính RFM:**
   * Đảm bảo các đơn hàng đã import đang ở trạng thái **Đơn bán hàng (`sale`)**.
   * Vào **Thiết lập $\rightarrow$ Kỹ thuật $\rightarrow$ Tác vụ đã lên lịch (Scheduled Actions)** $\rightarrow$ mở **`Dominos: Tính RFM và gán phân khúc khách hàng`** $\rightarrow$ bấm **Chạy thủ công (Run Manually)** (hệ thống cũng tự động chạy định kỳ 1 ngày/lần).
5. **Xem kết quả:**
   * **Hồ sơ khách hàng:** Vào **Liên hệ (Contacts)** $\rightarrow$ mở một khách hàng $\rightarrow$ xem tab **RFM**.
   * **Lọc & Gom nhóm:** Tại danh sách **Liên hệ**, sử dụng bộ lọc nhanh (`RFM: VIP`, `RFM: At-risk`...) hoặc chọn **Nhóm theo (Group By) $\rightarrow$ Phân khúc RFM**.
   * **Báo cáo tổng hợp:** Vào **Bán hàng (Sales) $\rightarrow$ Báo cáo (Reporting) $\rightarrow$ Báo cáo RFM** để xem **Bảng Pivot** và **Biểu đồ cột (Bar Chart)**.