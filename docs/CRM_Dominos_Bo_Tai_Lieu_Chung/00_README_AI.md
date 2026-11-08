# 00 - ĐỌC TRƯỚC: Bộ tài liệu chung đồ án CRM Domino's Pizza (môn EC213)
Phiên bản bộ tài liệu: 08/11/2026 | Hạn nộp đồ án: **23/11/2026** | Người điều phối kỹ thuật: A (Odoo Developer & System Specialist)

Bộ này dành cho **AI trợ lý của thành viên B (Data & Analytics) và C (BA & Process Lead)** (và cả A). Mục tiêu: mọi người làm đúng một dự án, không tự suy diễn.

## Thứ tự đọc (bắt buộc, đọc hết trước khi làm)
1. `00_README_AI.md` (file này)
2. `01_BOI_CANH_VA_QUYET_DINH.md` - bối cảnh, cái đã chốt, cái CHƯA chốt
3. `07_TRANG_THAI_HE_THONG.md` - hiện trạng hệ thống thật (A cập nhật liên tục)
4. `02_RUBRIC_VA_YEU_CAU_NOP.md` - tiêu chí chấm và quy cách nộp
5. `03_QUY_TRINH_VA_VAI_TRO.md`, rồi `04_GUIDELINE_V2.md` (nhiệm vụ từng vai trò), `05_HE_THONG_VA_QUY_TRINH_V2.md`
6. `06_QUY_UOC_VA_MAU.md` - quy ước đặt tên, Git, nhật ký
7. Thư mục `nguon/` - tài liệu gốc của nhóm (chỉ dùng để lấy chi tiết nghiệp vụ, xem thứ bậc bên dưới)

## Thứ bậc nguồn khi có mâu thuẫn (số nhỏ thắng)
1. `07_TRANG_THAI_HE_THONG.md` và `01_BOI_CANH_VA_QUYET_DINH.md`
2. `04_GUIDELINE_V2.md`, `05_HE_THONG_VA_QUY_TRINH_V2.md`, `03_...`
3. `02_RUBRIC...` (tiêu chí chấm là bắt buộc; nếu mâu thuẫn với mục 2 thì BÁO NGAY cho người dùng)
4. Tài liệu trong `nguon/` (có thể đã lỗi thời; đặc biệt `nguon/03` và `nguon/04` đã bị thay thế một phần)

## Quy tắc làm việc cho AI (bắt buộc)
1. **Không suy diễn, không bịa.** Số liệu, tên trường, tên stage pipeline, quy tắc loyalty, mốc SLA, ngưỡng RFM, tên người, đường dẫn: nếu KHÔNG có trong bộ tài liệu thì ghi `[CẦN XÁC NHẬN]` và hỏi người dùng. Không tự điền cho đẹp.
2. **Không đổi quyết định đã chốt** (mục "ĐÃ CHỐT" trong file 01). Muốn đề xuất đổi: nêu lý do, để người dùng chuyển cho A.
3. **Trước khi làm việc**, trả lời 3 phần: (a) tóm tắt hiểu biết về dự án trong tối đa 10 dòng, (b) nhiệm vụ của vai trò mình (theo `04_GUIDELINE_V2.md`) và hạn, (c) danh sách điều chưa rõ / mục `[?]` cần hỏi. Chờ người dùng xác nhận.
4. **Odoo Community 17.0 only.** Không đề xuất tính năng Enterprise/Studio/Marketing Automation/SMS gốc/Helpdesk gốc. Nếu không chắc một tính năng có trên Community 17.0 hay không: nói rõ "chưa kiểm chứng" và đưa cách kiểm tra trong Odoo của người dùng. Không dùng cách làm của Odoo 18/19 mà không nói rõ.
5. **Làm từng bước ngắn**, chờ người dùng báo kết quả rồi mới sang bước kế (người dùng muốn tiết kiệm token). Không viết dài khi không cần.
6. **Ghi nguồn:** khi nêu một quy định của dự án, ghi rõ lấy từ file nào, mục nào. Khi dùng kiến thức bên ngoài, nói đó là kiến thức chung, chưa kiểm chứng với dự án.
7. **Giữ thống nhất tên gọi** theo `06_QUY_UOC_VA_MAU.md` và `07_TRANG_THAI_HE_THONG.md`. Cần trường/tên mới chưa có trong đó: hỏi A, không tự đặt.
8. **Không ghi mật khẩu, API key, token** vào bất kỳ tài liệu nào; không yêu cầu người dùng dán chúng vào chat.
9. **Ngôn ngữ:** trả lời tiếng Việt; tên tính năng Odoo ghi kèm tên tiếng Anh. Câu chữ trong báo cáo: học thuật, súc tích, không cường điệu.
10. **Cuối mỗi bước hoàn thành:** đề xuất 3-5 dòng nhật ký để người dùng dán vào `docs/SESSION_LOG.md` (ngày, việc, kết quả, vướng mắc).
11. **Không tự nhận đã kiểm tra** thứ chưa kiểm tra. Phân biệt rõ: "đã chạy thử", "đọc từ tài liệu", "kiến thức chung".
