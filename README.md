# 🧮 Project Minh họa Tích phân trong Không gian - Giải Tích 2

Chào mừng bạn đến với project mô phỏng đồ họa Toán học! Project này được xây dựng bằng Python nhằm mục đích trực quan hóa các vật thể 3D, các mặt cong, đường cong giao tuyến và các miền phẳng 2D phục vụ cho Bài tập lớn môn Toán / Giải tích 2.

Dự án sử dụng **Streamlit** để tạo giao diện Web App thân thiện và **Plotly** để kết xuất đồ họa tương tác mượt mà.

---

## ✨ Tính năng nổi bật

* **Tương tác 3D toàn diện:** Cho phép người dùng dùng chuột để xoay đa chiều, thu phóng (zoom) và trỏ chuột (hover) để xem tọa độ chính xác của từng điểm trên mặt cong.
* **Giao diện Web trực quan:** Menu bên trái dạng sidebar giúp chuyển đổi qua lại giữa các Đề tài và Câu hỏi chỉ với một cú click chuột.
* **Hệ trục tọa độ chuẩn mực:** Tự động mô phỏng các trục tọa độ Ox (Đỏ), Oy (Xanh lá), Oz (Xanh dương) đâm xuyên qua gốc tọa độ kèm theo mũi tên chỉ chiều dương.
* **Tổ chức code Module hóa:** Logic toán học được tách riêng vào các file `topic` riêng biệt, giúp dễ dàng mở rộng và bảo trì.

---

## 📂 Cấu trúc thư mục

Project được thiết kế với cấu trúc tối giản và rõ ràng:

```text
├── main.py       # File chạy chính, chứa giao diện Streamlit và hàm xử lý trục tọa độ
├── requirements.txt # Danh sách các thư viện cần cài đặt (Streamlit, Plotly, NumPy)
├── topic1.py     # Chứa logic và hàm vẽ đồ thị cho 4 câu của Đề tài 1
├── topic2.py     # Chứa logic và hàm vẽ đồ thị cho 4 câu của Đề tài 2
├── topic3.py     # Chứa logic và hàm vẽ đồ thị cho 4 câu của Đề tài 3
└── README.md     # Tài liệu hướng dẫn (File này)
```

---

## 🛠️ Hướng dẫn cài đặt

Để chạy được project này, máy tính của bạn cần được cài đặt sẵn **Python 3**. Thực hiện theo các bước sau:

**Bước 1:** Clone hoặc tải toàn bộ thư mục mã nguồn về máy tính.

**Bước 2:** Mở Terminal (Command Prompt / PowerShell) tại thư mục chứa mã nguồn.

**Bước 3:** Cài đặt các thư viện cần thiết bằng lệnh pip:
```bash
pip install -r requirements.txt
```

---

## 🚀 Hướng dẫn sử dụng

Sau khi đã cài đặt xong các thư viện, bạn tiến hành khởi chạy ứng dụng web.

**Bước 1:** Tại Terminal (đang trỏ đúng vào thư mục project), gõ lệnh sau:
```bash
python -m streamlit run main.py
```

**Bước 2:** Đợi trong giây lát, trình duyệt web của bạn sẽ tự động bật lên và truy cập vào địa chỉ Localhost (thường là `http://localhost:8501`).

**Bước 3:** Trải nghiệm ứng dụng:
1. Nhìn sang Menu bên trái, chọn Đề tài (Ví dụ: Đề Tài 1).
2. Chọn Câu hỏi tương ứng cần xem đồ thị.
3. Ở khung vẽ đồ thị bên phải:
   * **Chuột trái + Kéo:** Để xoay đồ thị theo nhiều góc nhìn.
   * **Con lăn chuột:** Để phóng to / thu nhỏ.
   * **Biểu tượng Camera (Góc trên bên phải đồ thị):** Nhấn vào đây để tải hình ảnh dưới dạng file PNG chất lượng cao, có thể chèn trực tiếp vào báo cáo.

---