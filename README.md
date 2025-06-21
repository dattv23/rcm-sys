# 📦 User Review Filtering and Product Recommendation System

Hệ thống giúp:

- **Phân loại cảm xúc** từ bình luận người dùng (SVM model)
- **Lọc đánh giá không phù hợp**
- **Đề xuất sản phẩm cá nhân hóa** dựa trên hành vi người dùng (Matrix Factorization – SVD/NMF/KNN)

---

## 🚀 Yêu cầu hệ thống

- Python **3.10.8**
- Pip (>=22.x)
- Môi trường khuyên dùng: `venv` hoặc `pyenv`

---

## 📁 Cấu trúc thư mục

```
D:.
├───data/                 # Dữ liệu đầu vào
│   ├───labeled/          # Dữ liệu đã gán nhãn cảm xúc
│   ├───processed/        # Dữ liệu đã xử lý
│   └───raw/              # Dữ liệu thô
│       ├───products/     # Metadata sản phẩm
│       └───reviews/      # Đánh giá gốc từ Tiki
├───log/                  # Thư mục log huấn luyện & chạy mô hình
├───models/               # Lưu mô hình SVM và MF
├───preprocessing/        # Xử lý văn bản (TextProcessor)
├───resources/            # File hỗ trợ: teencode.csv, stopwords.txt, phrase_mapping.csv
└───README.md             # Hướng dẫn này
```

---

## 🧰 Cài đặt thư viện

```bash
pip install -r requirements.txt
```

Nếu bị lỗi phân quyền khi cài đặt, dùng:

```bash
pip install --user -r requirements.txt
```

---

## ✍️ Tác giả

- **Truong Van Dat**
- Đồ án tốt nghiệp – HUTECH 2025
- Đề tài: _"Xây dựng mô hình lọc đánh giá người dùng nhằm cải thiện chất lượng của hệ thống đề xuất"_
