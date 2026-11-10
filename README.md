<div align="center">
  <img src="logo-hnh.png" alt="Hong Ngoc Ha Travel Logo" width="280"/>
  <h1>🛫 HNH Flight Hub API — B2B Partner Integration Guide</h1>
  <p><b>Cổng Tài Liệu & Hướng Dẫn Tích Hợp API Vé Máy Bay Dành Cho Đại Lý & Đối Tác OTA</b></p>
  <p><i>Tiêu chuẩn Quốc tế · Trực quan · Đa ngôn ngữ (Tiếng Việt · 中文 · English)</i></p>

  <p>
    <a href="https://flight-doc.tripota.com.vn/docs/intro/"><img src="https://img.shields.io/badge/Docs-TripOTA%20Flight%20Doc-0284c7?style=flat-square&logo=book" alt="Docs"></a>
    <a href="https://sandbox-apihub.tripota.com.vn"><img src="https://img.shields.io/badge/Sandbox-API%20Endpoint-059669?style=flat-square&logo=server" alt="Sandbox"></a>
    <a href="https://flight-api-hub-dev.tripota.com.vn/swagger/index.html"><img src="https://img.shields.io/badge/Swagger-UI%20Console-d97706?style=flat-square&logo=swagger" alt="Swagger"></a>
    <a href="https://flight-api-hub-dev.tripota.com.vn/swagger/flight-hub/swagger.json"><img src="https://img.shields.io/badge/OpenAPI-3.0%20JSON-7c3aed?style=flat-square" alt="OpenAPI"></a>
    <img src="https://img.shields.io/badge/Status-Active%20v1.0-blue?style=flat-square" alt="Status">
  </p>
</div>

---

## 📖 1. Giới thiệu Dự án

**HNH Flight Hub API Guide** là cổng thông tin và hướng dẫn kỹ thuật tích hợp API vé máy bay B2B của **Hồng Ngọc Hà Travel (HNH)**. 

Dự án được xây dựng nhằm mục đích tối ưu hóa trải nghiệm tích hợp của các kỹ sư phát triển phần mềm tại các **Đại lý du lịch nội địa Việt Nam (F1/F2/F3)**, các **Sàn thương mại điện tử**, cũng như các **Đối tác OTA hàng đầu Châu Á** (Trip.com/Ctrip, Qunar, Fliggy, Tongcheng...).

### 🔗 4 Cổng Tra Cứu Kỹ Thuật Trọng Tâm
1. **📘 Tài liệu kỹ thuật chi tiết:** [flight-doc.tripota.com.vn](https://flight-doc.tripota.com.vn/docs/intro/)
2. **🧪 Cổng Sandbox thử nghiệm:** [sandbox-apihub.tripota.com.vn](https://sandbox-apihub.tripota.com.vn)
3. **🛠️ Swagger UI Dev Console:** [flight-api-hub-dev.tripota.com.vn/swagger](https://flight-api-hub-dev.tripota.com.vn/swagger/index.html)
4. **📄 OpenAPI 3.0 Spec JSON:** [swagger/flight-hub/swagger.json](https://flight-api-hub-dev.tripota.com.vn/swagger/flight-hub/swagger.json)

---

## ✨ 2. Tính Năng Nổi Bật (Chuẩn 10-Sao Premium)

* **🎨 Giao diện Kép (Light Mode mặc định & Dark Mode):** Thiết kế thanh lịch, chuẩn mực thẩm mỹ cao cấp (Apple / Linear style), chuyển đổi linh hoạt qua nút bấm và lưu trạng thái vào `localStorage`.
* **🌐 Hỗ trợ 4 chế độ ngôn ngữ:**
  * 🇻🇳 **Tiếng Việt (`?lang=vi`)**: Được tối ưu sâu cho lập trình viên và chuyên viên nghiệp vụ vé của các đại lý Việt Nam.
  * 🇨🇳 **中文 (Chinese)**: Dành riêng cho đối tác OTA Trung Quốc.
  * 🇬🇧 **English**: Chuẩn kết nối hàng không quốc tế.
  * 🌐 **Tất cả (Song song)**: Đối chiếu thuật ngữ IATA và nghiệp vụ thực tế.
* **⚡ Interactive Sandbox cURL Generator:** Cho phép chọn chặng bay (`SGN-HAN`, `HAN-DAD`, `SGN-SIN`...), hệ thống hãng và số lượng hành khách $\to$ Sinh ngay lệnh cURL trỏ thẳng vào Sandbox kèm tính năng One-Click Copy.
* **🔄 Mô hình hóa Chuỗi Token (Token Chaining Visualizer):** Sơ đồ trực quan hành trình của chuỗi mã hóa `flightValue` qua các bước: `Search` $\to$ `Select` $\to$ `Book` $\to$ `Issue` $\to$ `Retrieve`.
* **🏢 Chuẩn hóa Danh Mục Nguồn Vé (Content Sources):**
  * *Hãng nội địa*: Vietnam Airlines (`VN`), Vietjet Air (`VJ`), Bamboo Airways (`QH`), Vietravel Airlines (`VU`), Sun Phu Quoc Airways (`9G`).
  * *GDS Toàn cầu*: Amadeus (`1A`), Travelport/Galileo (`1G`), Sabre/Abacus (`1B`/`1S`).
  * *Direct NDC*: Scoot (`TR`), Turkish Airlines (`TK`), Philippine Airlines (`PR`), Singapore Airlines (`SQ`).
  * *LCC (Hãng giá rẻ)*: AirAsia (`AK`), Spring Airlines (`9C`).
  * *Aggregators / Consolidators*: Scoot & Batik Hub (`TH`), SkyHub (`SH`), Flyone (`FO`).
* **⚠️ Từ điển Tra Cứu Mã Lỗi Thông Minh:** Tìm kiếm nhanh nguyên nhân và hướng khắc phục các mã lỗi hệ thống (`00001` – `00020+`, `ERR_SEAT`, `ERR_DRIFT`...).
* **🛡️ Báo cáo Kiểm toán Kỹ thuật Độc lập:** Đi kèm file `flight-hub-team-feedback.html` dành riêng cho đội ngũ core backend Flight Hub.

---

## 📂 3. Cấu Trúc Thư Mục

```text
API-HNH-Guide-EN-CN/
├── index.html                      # Cổng hướng dẫn tích hợp chính (Light/Dark, Đa ngôn ngữ, Sandbox Runner)
├── flight-hub-team-feedback.html   # Báo cáo thẩm định & góp ý kỹ thuật gửi riêng team Flight Hub
├── logo-hnh.png                    # Logo Hồng Ngọc Hà Travel
├── LOGO HNH_TV 1265x657.png        # Logo gốc chất lượng cao
├── build_index.py                  # Script tự động hóa sinh mã HTML
├── project-meta.json               # Metadata cấu hình dự án
├── .gitignore                      # Cấu hình bỏ qua thư mục rác
└── README.md                       # Tài liệu hướng dẫn dự án (File này)
```

---

## 🚀 4. Hướng Dẫn Sử Dụng & Triển Khai

### Xem trực tiếp trên máy cá nhân
Chỉ cần mở trực tiếp file `index.html` bằng bất kỳ trình duyệt nào (Google Chrome, Microsoft Edge, Safari, Firefox).
* Để xem trực tiếp bản Tiếng Việt cho đại lý: `index.html?lang=vi`
* Để xem bản Tiếng Trung cho đối tác OTA: `index.html?lang=cn`

### Triển khai lên Netlify (Production)
Dự án được cấu hình thuần tĩnh (Static SPA) với hiệu năng tải tức thì:
1. Đẩy code lên GitHub:
   ```bash
   git add .
   git commit -m "feat: release 10-star flight hub api integration guide"
   git push origin master
   ```
2. Netlify tự động kích hoạt tiến trình triển khai (`publish = "."`).

---

## 📞 5. Kênh Hỗ Trợ Kỹ Thuật

* **📧 Email Hỗ Trợ Tích Hợp:** `api-support@tripota.com.vn`
* **📞 Hotline Nghiệp Vụ Vé (24/7):** `+84 (0) 28 3914 9999`
* **💬 Kênh Hỗ Trợ Kỹ Sư:** `@HNH_FlightHub_Support` (WeChat / Telegram / Zalo)

---

<div align="center">
  <p><b>Hong Ngoc Ha Travel (HNH) © 2026</b></p>
  <p><i>Designed with ♥ by Trung Nguyễn - Platform Expert</i></p>
</div>
