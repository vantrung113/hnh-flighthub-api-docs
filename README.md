<div align="center">
  <img src="logo-hnh.png" alt="Hong Ngoc Ha Travel Logo" width="280"/>
  <h1>🛫 HNH Flight Hub API — B2B Partner Integration Portal</h1>
  <p><b>Cổng Tài Liệu & Hướng Dẫn Tích Hợp API Vé Máy Bay Dành Cho Đại Lý & Đối Tác OTA Quốc Tế</b></p>
  <p><i>Tiêu chuẩn Doanh nghiệp · Trực quan · Đa ngôn ngữ (Tiếng Việt · English · 简体中文)</i></p>

  <p>
    <a href="https://flight-doc.tripota.com.vn/docs/intro/"><img src="https://img.shields.io/badge/Docs-TripOTA%20Flight%20Doc-0284c7?style=flat-square&logo=book" alt="Docs"></a>
    <a href="https://sandbox-apihub.tripota.com.vn"><img src="https://img.shields.io/badge/Sandbox-API%20Endpoint-059669?style=flat-square&logo=server" alt="Sandbox"></a>
    <a href="https://flight-api-hub-dev.tripota.com.vn/swagger/index.html"><img src="https://img.shields.io/badge/Swagger-UI%20Console-d97706?style=flat-square&logo=swagger" alt="Swagger"></a>
    <a href="https://flight-api-hub-dev.tripota.com.vn/swagger/flight-hub/swagger.json"><img src="https://img.shields.io/badge/OpenAPI-3.0%20JSON-7c3aed?style=flat-square" alt="OpenAPI"></a>
    <img src="https://img.shields.io/badge/Status-Active%20v1.0-blue?style=flat-square" alt="Status">
  </p>
</div>

---

## 📖 1. Giới Thiệu Dự Án

**HNH Flight Hub API Integration Portal** là hệ thống tài liệu và cổng thử nghiệm tương tác chuẩn doanh nghiệp của **Hồng Ngọc Hà Travel (HNH)**, phục vụ kết nối phân phối vé máy bay cho:
* **Đại lý du lịch nội địa Việt Nam (F1/F2/F3)**: Tích hợp giữ chỗ, kiểm giá, xuất vé tự động.
* **Đối tác OTA Quốc tế (Trip.com, Ctrip, Qunar, Fliggy, Tongcheng, Traveloka, Agoda...)**: Kết nối trực tiếp qua chuẩn NDC và GDS.
* **Doanh nghiệp TMĐT & Fintech**: Tích hợp luồng đặt vé máy bay vào ứng dụng và hệ sinh thái tài chính.

### 🔗 4 Cổng Tra Cứu Kỹ Thuật Trọng Tâm
1. **📘 Tài liệu kỹ thuật chi tiết:** [flight-doc.tripota.com.vn](https://flight-doc.tripota.com.vn/docs/intro/)
2. **🧪 Cổng Sandbox thử nghiệm:** [sandbox-apihub.tripota.com.vn](https://sandbox-apihub.tripota.com.vn)
3. **🛠️ Swagger UI Dev Console:** [flight-api-hub-dev.tripota.com.vn/swagger](https://flight-api-hub-dev.tripota.com.vn/swagger/index.html)
4. **📄 OpenAPI 3.0 Spec JSON:** [flight-api-hub-dev.tripota.com.vn/swagger/flight-hub/swagger.json](https://flight-api-hub-dev.tripota.com.vn/swagger/flight-hub/swagger.json)

---

## ✨ 2. Tính Năng Nổi Bật (Chuẩn Premium UI/UX)

* **🎨 Giao Diện Chuẩn Apple / Vercel (Light Mode & Dark Mode):** 
  * Tinh chỉnh màu sắc theo chuẩn cao cấp, hỗ trợ Light Mode mặc định và Dark Mode mượt mà (lưu trạng thái tự động qua `localStorage`).
* **🌐 Hỗ Trợ Đa Ngôn Ngữ Hoàn Chỉnh (100% Trilingual Dynamic Switcher):**
  * 🇻🇳 **Tiếng Việt (`?lang=vi`)**: Ngữ nghĩa nghiệp vụ vé máy bay chuẩn xác cho thị trường Việt Nam.
  * 🇬🇧 **English (`?lang=en`)**: Chuẩn kết nối hàng không quốc tế (IATA terminology).
  * 🇨🇳 **简体中文 (`?lang=cn`)**: Tối ưu riêng cho các đối tác công nghệ và OTA Trung Quốc.
  * 🌐 **Tất cả / Song song (`?lang=all`)**: Đối chiếu trực quan mọi thông số và trường dữ liệu.
* **⚡ Interactive Sandbox cURL Generator (Bộ Tạo Lệnh Test Nhanh):**
  * **Hành trình**: Hỗ trợ đầy đủ **Một chiều (One-Way)**, **Khứ hồi (Round-Trip)** và **Đa chặng (Multi-City)**.
  * **Ngày bay động**: Tự động tính ngày tương lai (Hôm nay + 7, + 10, + 14 ngày), loại trừ hoàn toàn rủi ro test bằng ngày quá khứ.
  * **Bộ chọn khách chuẩn IATA (Counter Stepper Card)**:
    * Người lớn (ADT, từ 12 tuổi): Tối thiểu 1.
    * Trẻ em (CHD, 2 đến dưới 12 tuổi).
    * Trẻ sơ sinh (INF, dưới 2 tuổi, ngồi cùng ghế).
    * *Quy tắc hàng không áp dụng nghiêm ngặt*: Tổng khách có ghế $\text{ADT} + \text{CHD} \le 9$; Em bé sơ sinh $\text{INF} \le \text{ADT}$ (tối đa 1 em bé / người lớn).
* **🏢 Hệ Thống Nguồn Vé Đa Kênh (Brand Badges Nổi Bật):**
  * *Hãng nội địa*: Vietnam Airlines (`VN`), Vietjet Air (`VJ`), Bamboo Airways (`QH`), Vietravel Airlines (`VU`), Sun Phu Quoc Airways (`9G`).
  * *Global GDS*: Amadeus (`1A`), Travelport / Galileo (`1G`), Sabre / Abacus (`1B` / `1S`).
  * *Direct NDC*: Scoot (`TR`), Turkish Airlines (`TK`), Philippine Airlines (`PR`), Singapore Airlines (`SQ`).
  * *LCC Quốc tế*: AirAsia (`AK`), Spring Airlines (`9C`).
  * *Aggregators / Wholesale Hub*: Scoot & Batik Hub (`TH`), SkyHub (`SH`), Flyone (`FO`).
* **🔄 Mô Hình Hóa Luồng Nghiệp Vụ (Token Chaining Visualizer):**
  * Chuỗi trạng thái mã hóa 6 bước khép kín: `Sign In` $\to$ `Search` $\to$ `Select` $\to$ `Price Quote` $\to$ `Book (PNR)` $\to$ `Issue Ticket`.
* **⚠️ Từ Điển Tra Cứu Mã Lỗi Thông Minh (Smart Error Dictionary):**
  * Tích hợp thanh tìm kiếm thông minh (hỗ trợ phím tắt `Ctrl + K`), lọc tức thì theo mã lỗi và giải pháp khắc phục.
* **🛡️ Báo Cáo Thẩm Định & Góp Ý Kỹ Thuật Độc Lập:**
  * Kèm file `flight-hub-team-feedback.html` dành riêng cho đội ngũ kỹ thuật Backend Flight Hub của Hồng Ngọc Hà Travel.

---

## 📂 3. Cấu Trúc Thư Mục Tối Giản

```text
API-HNH-Guide-EN-CN/
├── index.html                      # Cổng hướng dẫn tích hợp chính (SPA hoàn chỉnh, Đa ngữ, Sandbox Runner)
├── flight-hub-team-feedback.html   # Báo cáo thẩm định & đề xuất cải tiến gửi riêng Core Team Flight Hub
├── logo-hnh.png                    # Logo chính thức Hồng Ngọc Hà Travel
├── LOGO HNH_TV 1265x657.png        # Logo dự phòng độ phân giải cao
├── .gitignore                      # Cấu hình lọc git
└── README.md                       # Tài liệu hướng dẫn dự án (File này)
```

---

## 🚀 4. Hướng Dẫn Sử Dụng & Triển Khai

### Mở trực tiếp trên máy
Mở file `index.html` bằng bất kỳ trình duyệt hiện đại nào (Chrome, Edge, Safari, Firefox).
* Mở bản Tiếng Việt: `index.html?lang=vi`
* Mở bản Tiếng Anh: `index.html?lang=en`
* Mở bản Tiếng Trung: `index.html?lang=cn`

### Triển khai tự động lên Netlify
Toàn bộ dự án là Single Page Application tĩnh, hiệu năng tải tức thì (< 0.5s):
```bash
git add index.html flight-hub-team-feedback.html README.md logo-hnh.png "LOGO HNH_TV 1265x657.png" .gitignore
git commit -m "feat: release enterprise flight hub api integration portal"
git push origin master
```
Netlify tự động kích hoạt CI/CD build và xuất bản ra Production.

---

## 📞 5. Kênh Hỗ Trợ Kỹ Thuật & SLA

* **📧 Email Hỗ Trợ Kỹ Thuật API:** `api-support@tripota.com.vn`
* **📞 Hotline Nghiệp Vụ Vé (24/7):** `+84 (0) 28 3914 9999`
* **💬 Kênh Trao Đổi Kỹ Sư:** `@HNH_FlightHub_Support` (Zalo / Telegram)
* **⚡ Cam Kết Phản Hồi (SLA):** Dưới 15 phút đối với sự cố xuất vé khẩn cấp

---

<div align="center">
  <p><b>Hong Ngoc Hà Travel (HNH) © 2026</b></p>
  <p><i>Designed with ♥ by Trung Nguyễn - Platform Expert</i></p>
</div>
