# -*- coding: utf-8 -*-
"""
Full portal data definitions for Hong Ngoc Ha Travel — Flight Hub API
"""

NAV_DATA = [
    {
        "title": {
            "vi": "TỔNG QUAN",
            "en": "OVERVIEW",
            "cn": "概览导引"
        },
        "items": [
            {
                "id": "overview",
                "icon": "🌐",
                "title": {"vi": "Giới thiệu chung", "en": "Introduction & Overview", "cn": "平台概览"}
            },
            {
                "id": "systems",
                "icon": "🏢",
                "title": {"vi": "Hệ thống nguồn vé", "en": "Content Sources & Airlines", "cn": "航司与系统渠道"}
            },
            {
                "id": "playground",
                "icon": "⚡",
                "title": {"vi": "Trình tạo lệnh Sandbox cURL", "en": "Sandbox cURL Generator", "cn": "沙箱快速测试"}
            }
        ]
    },
    {
        "title": {
            "vi": "XÁC THỰC",
            "en": "AUTHENTICATION",
            "cn": "接口认证"
        },
        "items": [
            {
                "id": "auth",
                "method": "POST",
                "title": {"vi": "Đăng nhập tài khoản", "en": "Sign In", "cn": "账号登录"}
            },
            {
                "id": "refresh-token",
                "method": "POST",
                "title": {"vi": "Làm mới Token", "en": "Refresh Token", "cn": "刷新令牌"}
            },
            {
                "id": "system-list",
                "method": "GET",
                "title": {"vi": "Danh sách hệ thống", "en": "System List", "cn": "航司系统列表"}
            }
        ]
    },
    {
        "title": {
            "vi": "LUỒNG ĐẶT VÉ CHÍNH",
            "en": "CORE BOOKING FLOW",
            "cn": "核心出票流程"
        },
        "items": [
            {
                "id": "flow",
                "icon": "🔄",
                "title": {"vi": "Quy trình & Chaining Token", "en": "Flow & State Chaining", "cn": "业务流与令牌串联"}
            },
            {
                "id": "search",
                "method": "POST",
                "title": {"vi": "Tìm chuyến bay", "en": "Search Flights", "cn": "航班查询"}
            },
            {
                "id": "searchminfare",
                "method": "POST",
                "badge": {"vi": "Mới", "en": "New", "cn": "新"},
                "title": {"vi": "Lịch vé rẻ theo tháng", "en": "Min Fare Calendar", "cn": "低价日历"}
            },
            {
                "id": "select",
                "method": "POST",
                "title": {"vi": "Chọn giá & Khóa chỗ", "en": "Select & Price Lock", "cn": "验价选座"}
            },
            {
                "id": "pricequote",
                "method": "POST",
                "title": {"vi": "Kiểm tra lại giá", "en": "Price Quote", "cn": "价格确认"}
            },
            {
                "id": "book",
                "method": "POST",
                "title": {"vi": "Giữ chỗ (Tạo PNR)", "en": "Create Booking (PNR)", "cn": "创建预订 (生单)"}
            },
            {
                "id": "facebooking",
                "method": "POST",
                "title": {"vi": "Xem mặt vé", "en": "Face Booking", "cn": "票面信息"}
            },
            {
                "id": "issue",
                "method": "POST",
                "title": {"vi": "Xuất vé chính thức", "en": "Issue Ticket", "cn": "正式出票"}
            },
            {
                "id": "retrieve",
                "method": "POST",
                "title": {"vi": "Tra cứu đơn đặt chỗ", "en": "Retrieve Booking", "cn": "订单检索"}
            }
        ]
    },
    {
        "title": {
            "vi": "DỊCH VỤ BỔ TRỢ",
            "en": "ANCILLARY SERVICES",
            "cn": "附加服务 (Add-ons)"
        },
        "items": [
            {
                "id": "baggage",
                "method": "POST",
                "title": {"vi": "Mua hành lý ký gửi", "en": "Baggage Allowance", "cn": "行李额度"}
            },
            {
                "id": "seatmap",
                "method": "POST",
                "title": {"vi": "Sơ đồ & Chọn ghế", "en": "Seat Map", "cn": "机上选座"}
            },
            {
                "id": "ancillary",
                "method": "POST",
                "title": {"vi": "Dịch vụ bổ trợ khác", "en": "Ancillaries", "cn": "增值服务"}
            },
            {
                "id": "issue-emd",
                "method": "POST",
                "title": {"vi": "Xuất chứng từ phí phụ EMD", "en": "Issue EMD", "cn": "杂项凭证出票 (EMD)"}
            }
        ]
    },
    {
        "title": {
            "vi": "BỔ SUNG THÔNG TIN",
            "en": "SUPPLEMENTARY DATA",
            "cn": "信息补充与变更"
        },
        "items": [
            {
                "id": "infant",
                "method": "POST",
                "title": {"vi": "Thêm em bé (Infant)", "en": "Add Infant", "cn": "婴儿信息"}
            },
            {
                "id": "document",
                "method": "POST",
                "title": {"vi": "Hộ chiếu / CCCD", "en": "Passport & ID Document", "cn": "证件信息"}
            },
            {
                "id": "membership",
                "method": "POST",
                "title": {"vi": "Thẻ bay thường xuyên", "en": "Frequent Flyer Card", "cn": "常旅客会员"}
            },
            {
                "id": "osi-sk-remark",
                "method": "POST",
                "title": {"vi": "Chỉ thị hãng OSI / SK", "en": "Airline OSI / SK Remarks", "cn": "航司特殊指令"}
            },
            {
                "id": "update-contact",
                "method": "POST",
                "title": {"vi": "Cập nhật liên hệ & Hành khách", "en": "Update Contact & Pax", "cn": "联系人及旅客更新"}
            }
        ]
    },
    {
        "title": {
            "vi": "NGHIỆP VỤ HẬU MÃI",
            "en": "POST-SALE OPERATIONS",
            "cn": "售后与客票处理"
        },
        "items": [
            {
                "id": "split",
                "method": "POST",
                "title": {"vi": "Tách đoàn (Split PNR)", "en": "Split PNR", "cn": "订单拆单"}
            },
            {
                "id": "changeflight",
                "method": "POST",
                "title": {"vi": "Đổi chuyến bay", "en": "Change Flight", "cn": "改期换开"}
            },
            {
                "id": "cancel",
                "method": "POST",
                "title": {"vi": "Hủy chỗ đặt trước", "en": "Cancel Booking", "cn": "取消预订"}
            },
            {
                "id": "refund",
                "method": "POST",
                "title": {"vi": "Yêu cầu hoàn vé", "en": "Refund Ticket", "cn": "退票申请"}
            },
            {
                "id": "void",
                "method": "POST",
                "title": {"vi": "Hủy vé trong ngày (Void)", "en": "Void Ticket (Same-Day)", "cn": "当日废票 (Void)"}
            },
            {
                "id": "exchange",
                "method": "POST",
                "title": {"vi": "Đổi vé máy bay", "en": "Exchange Ticket", "cn": "客票换开"}
            },
            {
                "id": "farerule",
                "method": "POST",
                "title": {"vi": "Tra cứu điều kiện vé", "en": "Fare Rules", "cn": "客票退改规则"}
            },
            {
                "id": "checkin-online",
                "method": "POST",
                "title": {"vi": "Làm thủ tục trực tuyến", "en": "Online Check-in", "cn": "在线值机"}
            },
            {
                "id": "emission",
                "method": "POST",
                "title": {"vi": "Dữ liệu phát thải CO2", "en": "Carbon Emission", "cn": "碳排放数据"}
            }
        ]
    },
    {
        "title": {
            "vi": "TRA CỨU & HỖ TRỢ",
            "en": "REFERENCE & SUPPORT",
            "cn": "检索与技术支持"
        },
        "items": [
            {
                "id": "errors",
                "icon": "⚠️",
                "title": {"vi": "Từ điển mã lỗi thông minh", "en": "Smart Error Code Dictionary", "cn": "智能错误码字典"}
            },
            {
                "id": "example",
                "icon": "⚡",
                "title": {"vi": "Mã nguồn Python mẫu", "en": "Full Python Integration Script", "cn": "完整集成代码 (Python)"}
            },
            {
                "id": "support",
                "icon": "🎧",
                "title": {"vi": "Kênh hỗ trợ kỹ thuật", "en": "Developer Support & SLA", "cn": "技术支持与 SLA"}
            }
        ]
    }
]

HERO_DATA = {
    "badge": {
        "vi": "HỆ THỐNG KẾT NỐI API VÉ MÁY BAY B2B V1.0",
        "en": "HNH B2B AVIATION INTEGRATION PORTAL V1.0",
        "cn": "HNH 航空 B2B 开发者门户 V1.0"
    },
    "title_main": "Hong Ngoc Ha Travel — ",
    "title_span": "Flight Hub API",
    "subtitle": {
        "vi": "Cổng Tài Liệu & Hướng Dẫn Tích Hợp API Dành Cho Đại Lý & Đối Tác OTA (Việt Nam & Quốc Tế)",
        "en": "Partner Integration Guide | B2B Air Ticketing & GDS API Documentation",
        "cn": "合作伙伴集成指南 | 航司与 GDS 直连分销接口文档"
    },
    "desc": {
        "vi": "Hệ thống cổng kết nối API vé máy bay B2B tiêu chuẩn doanh nghiệp của <strong>Hồng Ngọc Hà Travel</strong>. Cung cấp kết nối trực tiếp đến toàn bộ các hãng hàng không nội địa Việt Nam (<strong>Vietnam Airlines</strong>, <strong>Vietjet Air</strong>, <strong>Bamboo Airways</strong>, <strong>Vietravel Airlines</strong>), các hệ thống phân phối toàn cầu <strong>GDS (Amadeus, Sabre, Galileo)</strong>, các kết nối chuẩn <strong>NDC (Scoot TR, Turkish TK, Singapore SQ, Philippine PR)</strong> và các hãng giá rẻ <strong>LCC (AirAsia AK, Spring Airlines 9C)</strong>.",
        "en": "Enterprise-grade flight booking API service provided by <strong>Hong Ngoc Ha Travel (HNH)</strong>. Delivering direct connectivity to all Vietnamese domestic airlines (<strong>Vietnam Airlines</strong>, <strong>Vietjet Air</strong>, <strong>Bamboo Airways</strong>, <strong>Vietravel Airlines</strong>), global distribution systems <strong>GDS (Amadeus, Sabre, Galileo)</strong>, direct <strong>NDC (Scoot TR, Turkish TK, Singapore SQ, Philippine PR)</strong>, and <strong>LCCs (AirAsia AK, Spring Airlines 9C)</strong>.",
        "cn": "本文档为中国及全球 OTA / 代理商提供越南航线及国际航班 API 完整集成指引。涵盖 <strong>Vietnam Airlines (VN)</strong>、<strong>Vietjet Air (VJ)</strong>、<strong>Bamboo Airways (QH)</strong>、<strong>Amadeus (1A)</strong>、<strong>Sabre (1S/1B)</strong>、<strong>Direct NDC (TR, TK, PR, SQ)</strong> 以及 <strong>LCC 廉航 (AirAsia AK, Spring Airlines 9C)</strong> 的认证、搜索、验价、预订、出票与售后全流程。"
    },
    "cards": [
        {
            "label": {"vi": "📘 Tài liệu chi tiết (Docs)", "en": "📘 Detailed Documentation (Docs)", "cn": "📘 详细技术文档 (Docs)"},
            "url": "https://flight-doc.tripota.com.vn/docs/intro/",
            "text": "flight-doc.tripota.com.vn"
        },
        {
            "label": {"vi": "🧪 Môi trường Sandbox Test", "en": "🧪 Sandbox Testing Environment", "cn": "🧪 沙箱测试环境 (Sandbox)"},
            "url": "https://sandbox-apihub.tripota.com.vn",
            "text": "sandbox-apihub.tripota.com.vn"
        },
        {
            "label": {"vi": "🛠️ Swagger UI Dev Console", "en": "🛠️ Swagger UI Dev Console", "cn": "🛠️ Swagger 交互控制台"},
            "url": "https://flight-api-hub-dev.tripota.com.vn/swagger/index.html",
            "text": "Swagger API Console v1.0"
        },
        {
            "label": {"vi": "📄 OpenAPI 3.0 Spec JSON", "en": "📄 OpenAPI 3.0 Spec JSON", "cn": "📄 OpenAPI 3.0 规范 JSON"},
            "url": "https://flight-api-hub-dev.tripota.com.vn/swagger/flight-hub/swagger.json",
            "text": "swagger.json (53 Endpoints)"
        }
    ]
}
