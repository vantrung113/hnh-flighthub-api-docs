# -*- coding: utf-8 -*-
"""
portal_translations.py
Complete multilingual translation maps for Hong Ngoc Ha Travel — Flight Hub API
"""

SECTION_HEADERS = {
    "systems": {
        "num": "00",
        "title": {
            "vi": "Hệ Thống Nguồn Vé & Hãng Bay",
            "en": "Content Sources & Airline Systems",
            "cn": "航司与系统渠道"
        },
        "subtitle": {
            "vi": "Bảng mã kết nối chuẩn xác theo phân nhóm: Hãng nội địa, GDS, NDC, LCC và Kênh Aggregator",
            "en": "System codes categorized by type: Domestic carriers, GDS, NDC direct-connect, LCC, and Aggregators",
            "cn": "按系统类型分类的标准对接代码：越南本土航司、GDS 分销系统、NDC 直连、LCC 廉航及专业聚合渠道"
        }
    },
    "playground": {
        "num": "⚡",
        "title": {
            "vi": "Interactive Sandbox cURL Generator — Tạo Lệnh Test Nhanh",
            "en": "Interactive Sandbox cURL Generator — Instant API Testing",
            "cn": "交互式沙箱 cURL 生成器 — 快速测试接口"
        },
        "subtitle": {
            "vi": "Tự động lấy ngày tương lai (Hôm nay + 7 ngày), sinh lệnh cURL trỏ thẳng vào Sandbox",
            "en": "Automatically sets future departure date (Today + 7 days) and generates instant Sandbox cURL commands",
            "cn": "自动获取未来起飞日期（今天 + 7天），即时生成直连沙箱环境的 cURL 测试命令"
        }
    },
    "auth": {
        "num": "01",
        "title": {
            "vi": "Cơ Chế Xác Thực & Cấp Token — Đăng Nhập & Duy Trì Phiên Làm Việc",
            "en": "Authentication & Credentials — Sign In & Maintain Bearer Token",
            "cn": "接口认证与凭证 — 账号登录与 Bearer Token 维护"
        },
        "subtitle": {
            "vi": "Đăng nhập tài khoản B2B và duy trì JWT Bearer Token trong vòng 24 giờ",
            "en": "B2B partner authentication and 24-hour JWT Bearer token lifecycle",
            "cn": "B2B 合作伙伴登录认证及 24 小时 JWT Bearer 令牌生命周期"
        }
    },
    "flow": {
        "num": "02",
        "title": {
            "vi": "Luồng Đặt Vé Chuẩn & Chaining Token — Quy Trình 6 Bước Khép Kín",
            "en": "End-to-End Booking Flow & Token Chaining — Standard 6-Step Workflow",
            "cn": "完整预订业务流与令牌串联 — 标准六步闭环流程"
        },
        "subtitle": {
            "vi": "Quy trình bắt buộc: Search → Select → Book → (Add-ons) → Issue Ticket → Retrieve",
            "en": "Mandatory sequence: Search → Select → Book → (Add-ons) → Issue Ticket → Retrieve",
            "cn": "核心调用时序：查询 (Search) → 验价 (Select) → 生单 (Book) → (附加服务) → 出票 (Issue) → 检索 (Retrieve)"
        }
    },
    "search": {
        "num": "03",
        "title": {
            "vi": "Tìm Chuyến Bay & Lịch Vé Rẻ — Tìm Vé 1 Chiều, Khứ Hồi & Giá Rẻ Tháng",
            "en": "Flight Search & Low Fare Calendar — One-Way, Round-Trip & Monthly Matrix",
            "cn": "航班查询与低价日历 — 单程/往返搜索及月度低价矩阵"
        },
        "subtitle": {
            "vi": "Tìm kiếm thời gian thực chuyến bay 1 chiều, khứ hồi và ma trận vé rẻ theo tháng",
            "en": "Real-time availability search for one-way/round-trip flights and monthly lowest fare calendar",
            "cn": "实时查询单程、往返航班运价库存，以及按月低价日历推荐"
        }
    },
    "select": {
        "num": "04",
        "title": {
            "vi": "Chọn Giá Vé & Khóa Chỗ — Lấy Chuỗi flightValue Thẩm Định",
            "en": "Select & Price Lock — Real-Time Seat Validation & flightValue Chain",
            "cn": "验价选座与锁定价格 — 实时验舱与获取 flightValue 令牌"
        },
        "subtitle": {
            "vi": "Xác minh kho chỗ thời gian thực và lấy chuỗi flightValue để đặt chỗ",
            "en": "Verify real-time seat inventory, reprice fare basis, and acquire locked flightValue token",
            "cn": "向航司实时验舱核实座位可用性，获取用于后续生单的 flightValue 核心令牌"
        }
    },
    "book": {
        "num": "05",
        "title": {
            "vi": "Tạo Đơn Giữ Chỗ (PNR) — Đẩy Thông Tin Hành Khách Lên Hãng Bay",
            "en": "Create Booking — Submit Passenger Details & Acquire Airline PNR",
            "cn": "创建预订 — 提交旅客信息并生成航司 PNR (bookingCode)"
        },
        "subtitle": {
            "vi": "Đưa thông tin hành khách lên hệ thống hãng và nhận mã đặt chỗ (bookingCode)",
            "en": "Submit passenger name records to airline hosts and acquire reservation code (bookingCode / PNR)",
            "cn": "向航司系统提交旅客名单，生成订座编码 (bookingCode / PNR) 并进入待支付状态"
        }
    },
    "issue": {
        "num": "06",
        "title": {
            "vi": "Xuất Vé Máy Bay — Ký Quỹ B2B & Cấp Vé Điện Tử (13 Chữ Số)",
            "en": "Issue Ticket — Official Issuance & B2B Deposit Deduction (13-Digit e-Ticket)",
            "cn": "正式出票 — 确认支付并扣减 B2B 授信额度（生成 13 位电子客票号）"
        },
        "subtitle": {
            "vi": "Thao tác chính thức và không thể đảo ngược — Sinh số vé điện tử 13 chữ số",
            "en": "Irreversible commercial action — Deducts B2B balance and issues official 13-digit airline e-tickets",
            "cn": "不可逆商业扣款操作 — 扣减 B2B 预存款并生成航司官方 13 位电子客票凭单"
        }
    },
    "retrieve": {
        "num": "07",
        "title": {
            "vi": "Tra Cứu Tình Trạng Vé & Đơn Hàng — Đọc Lại PNR & Trạng Thái Vé",
            "en": "Retrieve Booking — Read Itinerary, Passenger List & e-Ticket Status",
            "cn": "订单检索 — 查验航程信息、旅客列表及电子客票出票状态"
        },
        "subtitle": {
            "vi": "Đọc lại dữ liệu hành trình, hành khách và trạng thái vé điện tử",
            "en": "Query booking status, airline ticket numbers, and itinerary details anytime",
            "cn": "随时查询最新订单状态、航司票号及完整行程单数据"
        }
    },
    "ancillary": {
        "num": "08",
        "title": {
            "vi": "Hành Lý, Ghế Ngồi & Xuất EMD — Dịch Vụ Gia Tăng Cho Chuyến Bay",
            "en": "Ancillary Services & EMD — Baggage, Seat Map & Electronic Miscellaneous Documents",
            "cn": "附加服务与 EMD — 行李额度、机上选座与杂项凭证出票"
        },
        "subtitle": {
            "vi": "Bán các dịch vụ gia tăng trước và sau khi vé đã xuất",
            "en": "Sell and issue extra baggage, advanced seat selection, and ancillary services before or after ticketing",
            "cn": "支持在出票前或出票后增购预付费行李、机上预选座位及出具 EMD 杂项凭单"
        }
    },
    "supplementary": {
        "num": "09",
        "title": {
            "vi": "Bổ Sung Thông Tin Đặt Chỗ — Em Bé, Hộ Chiếu, Bông Sen Vàng & OSI/SK",
            "en": "Supplementary Booking Data — Infant, Passport, Frequent Flyer & OSI/SK",
            "cn": "预订信息补充 — 婴儿挂载、护照证件、常客卡号及航司 OSI/SK 指令"
        },
        "subtitle": {
            "vi": "Thêm em bé, giấy tờ tùy thân, thẻ khách hàng thân thiết và chỉ thị hàng không (OSI/SK/Remark)",
            "en": "Add infant pax, passport/national ID, frequent flyer cards, and airline service remarks (OSI/SK)",
            "cn": "出票前后补充关联婴儿、护照证件、常旅客会员卡以及航司业务服务指令 (OSI/SK/Remark)"
        }
    },
    "post-sale": {
        "num": "10",
        "title": {
            "vi": "Nghiệp Vụ Hậu Mãi & Xử Lý Vé — Tách Đoàn, Đổi Chuyến, Hoàn Vé & Void Vé",
            "en": "Post-Sale Operations — Split PNR, Change Flight, Refund & Void Ticket",
            "cn": "售后客票管理 — 订单拆单、改期换开、退票申请与当日作废"
        },
        "subtitle": {
            "vi": "Tách đoàn (Split PNR), Đổi vé (Exchange), Hoàn vé (Refund) và Hủy vé trong ngày (Void)",
            "en": "Comprehensive post-booking workflow: Split PNR, flight schedule change, refund application, same-day void, and fare rule verification",
            "cn": "覆盖客票全生命周期售后服务：订单拆单 (Split PNR)、改期换开 (Exchange)、退票申请 (Refund)、当日作废 (Void) 及客票退改规则查询"
        }
    },
    "errors": {
        "num": "11",
        "title": {
            "vi": "Từ Điển Mã Lỗi Thông Minh — Smart Error Code Dictionary",
            "en": "Smart Error Code Dictionary — Instant Diagnostic Guide",
            "cn": "智能错误码字典 — 故障排查与解决方案速查"
        },
        "subtitle": {
            "vi": "Tra cứu nguyên nhân và giải pháp xử lý ngay lập tức",
            "en": "Quick reference for root cause analysis and instant recovery procedures",
            "cn": "快速检索错误原因并获取官方推荐解决方案"
        }
    },
    "example": {
        "num": "12",
        "title": {
            "vi": "Mã Nguồn Tích Hợp Hoàn Chỉnh — Full Python Integration Script",
            "en": "Full Python Integration Script — End-to-End Workflow",
            "cn": "完整集成代码 — Python 端到端出票流程"
        },
        "subtitle": {
            "vi": "Đoạn mã Python tích hợp hoàn chỉnh: Đăng nhập → Tìm vé → Chọn giá → Giữ chỗ → Xuất vé",
            "en": "Production-ready Python implementation: Sign In → Search → Select → Book PNR → Issue Ticket",
            "cn": "生产级 Python 集成代码：登录认证 → 航班查询 → 验价选座 → 创建预订 → 正式出票"
        }
    },
    "support": {
        "num": "13",
        "title": {
            "vi": "Kênh Hỗ Trợ Kỹ Thuật & SLA — Developer Support",
            "en": "Developer Support & SLA — 24/7 Technical Assistance",
            "cn": "开发者支持与 SLA 保障 — 7x24 技术服务"
        },
        "subtitle": {
            "vi": "Đội ngũ kỹ sư hỗ trợ tích hợp 24/7 của Hồng Ngọc Hà Travel",
            "en": "Dedicated 24/7 integration engineering team by Hong Ngoc Ha Travel",
            "cn": "鸿玉荷旅行社 (Hong Ngoc Ha Travel) 7x24 小时技术保障团队"
        }
    }
}

ENDPOINT_TITLES = {
    "/api/v1/sign-in": {
        "vi": "Đăng nhập lấy Token",
        "en": "Sign In (Get Bearer Token)",
        "cn": "账号登录获取 Token"
    },
    "/api/v1/refresh-token": {
        "vi": "Gia hạn Token",
        "en": "Refresh Access Token",
        "cn": "刷新访问令牌"
    },
    "/api/v1/system": {
        "vi": "Lấy danh sách hệ thống khả dụng",
        "en": "Get Available Systems",
        "cn": "获取可用航司及系统列表"
    },
    "/api/v1/flight/search": {
        "vi": "Tìm kiếm chuyến bay theo ngày",
        "en": "Search Flights by Date",
        "cn": "实时航班运价查询"
    },
    "/api/v1/flight/search-min-fare": {
        "vi": "Tìm giá vé rẻ nhất theo khoảng ngày (Lịch vé rẻ)",
        "en": "Search Lowest Fare Calendar",
        "cn": "月度低价日历检索"
    },
    "/api/v1/flight/select": {
        "vi": "Xác nhận chọn chuyến bay & Khóa chỗ",
        "en": "Select Flight & Lock Price",
        "cn": "确认航班并锁定价格 (验舱)"
    },
    "/api/v1/flight/price-quote": {
        "vi": "Tái thẩm định giá trước khi xuất vé",
        "en": "Reprice & Quote Verification",
        "cn": "出票前价格二次复核 (Price Quote)"
    },
    "/api/v1/flight/book": {
        "vi": "Tạo đặt chỗ (Sinh mã PNR)",
        "en": "Create Booking (Acquire PNR)",
        "cn": "创建预订 (生成航司 PNR)"
    },
    "/api/v1/flight/face-booking": {
        "vi": "Xem mặt vé (Kiểm tra lại PNR)",
        "en": "Face Booking (Verify PNR Data)",
        "cn": "查看票面信息 (校验 PNR 明细)"
    },
    "/api/v1/flight/issue-ticket": {
        "vi": "Thực hiện xuất vé chính thức",
        "en": "Issue Official Airline Ticket",
        "cn": "确认支付并正式出票"
    },
    "/api/v1/flight/retrieve-booking": {
        "vi": "Tra cứu đơn đặt chỗ & Tình trạng vé",
        "en": "Retrieve Booking & Ticket Status",
        "cn": "检索订单详情及客票状态"
    },
    "/api/v1/ancillary/baggage": {
        "vi": "Tra cứu các gói hành lý mua thêm",
        "en": "Query Baggage Allowance Packages",
        "cn": "查询付费行李额度包"
    },
    "/api/v1/ancillary/seatmap": {
        "vi": "Lấy sơ đồ chỗ ngồi trên máy bay",
        "en": "Get Aircraft Seat Map",
        "cn": "获取机舱座位布局图 (Seat Map)"
    },
    "/api/v1/ancillary/book-ancillary": {
        "vi": "Đặt mua dịch vụ bổ trợ",
        "en": "Book Ancillary Services",
        "cn": "预订增值服务 (行李/选座)"
    },
    "/api/v1/ancillary/issue-emd": {
        "vi": "Xuất chứng từ dịch vụ phụ trợ (EMD)",
        "en": "Issue EMD Miscellaneous Document",
        "cn": "出具杂项凭据 (Issue EMD)"
    },
    "/api/v1/booking/add-infant": {
        "vi": "Thêm em bé vào booking",
        "en": "Add Infant to Booking",
        "cn": "向预订中挂载婴儿旅客"
    },
    "/api/v1/booking/update-document": {
        "vi": "Thêm giấy tờ tùy thân (Hộ chiếu/CCCD)",
        "en": "Update Travel Document (Passport/ID)",
        "cn": "更新旅客证件信息 (护照/身份证)"
    },
    "/api/v1/booking/update-membership": {
        "vi": "Thêm thẻ khách hàng thân thiết",
        "en": "Update Frequent Flyer Membership",
        "cn": "添加常旅客会员卡号"
    },
    "/api/v1/booking/add-remark": {
        "vi": "Thêm chỉ thị hãng (OSI / SK / Remark)",
        "en": "Add Airline Remarks (OSI / SK)",
        "cn": "添加航司业务指令 (OSI / SK / Remark)"
    },
    "/api/v1/booking/update-contact": {
        "vi": "Cập nhật thông tin liên hệ & hành khách",
        "en": "Update Contact Info & Passenger Details",
        "cn": "更新订单联系人及旅客信息"
    },
    "/api/v1/booking/split-pnr": {
        "vi": "Tách hành khách khỏi đoàn (Split PNR)",
        "en": "Split Passenger from PNR (Split PNR)",
        "cn": "拆分订单旅客 (Split PNR)"
    },
    "/api/v1/booking/change-flight": {
        "vi": "Thay đổi hành trình khi chưa xuất vé",
        "en": "Change Itinerary (Pre-Ticketing)",
        "cn": "出票前修改航班航程"
    },
    "/api/v1/booking/cancel": {
        "vi": "Hủy giữ chỗ PNR (Chưa xuất vé)",
        "en": "Cancel Booking (Pre-Ticketing)",
        "cn": "取消预订占用座位 (未出票)"
    },
    "/api/v1/ticket/refund": {
        "vi": "Quy trình hoàn vé 2 bước",
        "en": "Two-Step Ticket Refund Workflow",
        "cn": "两步式退票流程 (询价与提交)"
    },
    "/api/v1/ticket/void": {
        "vi": "Hủy vé trong ngày không mất phí (Void Ticket)",
        "en": "Same-Day Void Ticket (Zero Penalty)",
        "cn": "当日免费废票 (Void Ticket)"
    },
    "/api/v1/ticket/exchange": {
        "vi": "Đổi vé máy bay (Quy trình 3 bước)",
        "en": "Ticket Reissue & Exchange (3-Step)",
        "cn": "客票改期换开 (三步流程)"
    },
    "/api/v1/ticket/fare-rule": {
        "vi": "Tra cứu điều kiện vé (Fare Rule)",
        "en": "Query Detailed Fare Rules",
        "cn": "查询客票详细退改签规则 (Fare Rule)"
    },
    "/api/v1/checkin/online": {
        "vi": "Làm thủ tục chuyến bay trực tuyến",
        "en": "Online Flight Check-in",
        "cn": "在线值机与登机牌办理"
    },
    "/api/v1/flight/carbon-emission": {
        "vi": "Tính toán phát thải CO2 chuyến bay",
        "en": "Calculate Flight Carbon Emission",
        "cn": "计算航班碳排放指标 (CO2)"
    }
}

ERROR_ROWS = [
    {
        "code": "00001",
        "name": "AuthenticationFailed",
        "cause": {
            "vi": "Tài khoản hoặc mật khẩu kết nối API không đúng",
            "en": "Invalid partnerCode, username, or password for API authentication",
            "cn": "API 认证账号、密码或 partnerCode 错误"
        },
        "solution": {
            "vi": "Kiểm tra lại partnerCode, userName và password được cấp",
            "en": "Verify partnerCode, userName, and password assigned by HNH",
            "cn": "请核对 HNH 官方分配的 partnerCode、userName 及密码"
        }
    },
    {
        "code": "00002",
        "name": "Unauthorized",
        "cause": {
            "vi": "Token chưa truyền hoặc đã hết hạn 24 giờ",
            "en": "Bearer token missing or expired (exceeded 24 hours)",
            "cn": "未携带 Bearer 令牌或令牌已过期（超过24小时）"
        },
        "solution": {
            "vi": "Gọi /api/v1/refresh-token hoặc đăng nhập lại",
            "en": "Call /api/v1/refresh-token or re-authenticate via /api/v1/sign-in",
            "cn": "调用 /api/v1/refresh-token 刷新或重新登录获取新令牌"
        }
    },
    {
        "code": "00004",
        "name": "EndpointNotFound",
        "cause": {
            "vi": "Sai URL endpoint hoặc sai phương thức GET/POST",
            "en": "Endpoint not found or incorrect HTTP method (GET vs POST)",
            "cn": "请求端点 URL 错误或 HTTP 方法不匹配 (GET/POST)"
        },
        "solution": {
            "vi": "Kiểm tra lại đường dẫn API trong tài liệu",
            "en": "Verify exact API URL path and HTTP verb against documentation",
            "cn": "请核对文档中该接口的标准路径及请求方法"
        }
    },
    {
        "code": "00010",
        "name": "ValidationNotEmpty",
        "cause": {
            "vi": "Thiếu trường dữ liệu bắt buộc trong request body",
            "en": "Missing mandatory field in JSON request payload",
            "cn": "JSON 请求体中缺少必填参数字段"
        },
        "solution": {
            "vi": "Xem kỹ bảng tham số các trường Required: YES",
            "en": "Inspect field specification table and ensure all REQUIRED fields are present",
            "cn": "对照参数说明表，补全所有标记为「必填」的字段"
        }
    },
    {
        "code": "00013",
        "name": "SystemNotFound",
        "cause": {
            "vi": "Mã hệ thống truyền vào không tồn tại hoặc chưa kích hoạt",
            "en": "Specified airline system code not found or inactive for account",
            "cn": "传入的航司或系统代码不存在或未为该账户开通权限"
        },
        "solution": {
            "vi": "Gọi /api/v1/system để lấy danh sách mã hợp lệ",
            "en": "Call /api/v1/system to list all enabled carrier system codes",
            "cn": "调用 /api/v1/system 接口获取已授权开通的系统代码列表"
        }
    },
    {
        "code": "ERR_SEAT",
        "name": "InventorySoldOut",
        "cause": {
            "vi": "Chỗ ngồi hoặc hạng vé giá rẻ đã bị bán hết",
            "en": "Selected booking class / seat inventory sold out in real-time",
            "cn": "所选舱位或低价配额已售罄（航司实时验舱失败）"
        },
        "solution": {
            "vi": "Yêu cầu khách hàng tìm kiếm lại chuyến bay mới",
            "en": "Prompt user to re-search flights and choose an available fare bucket",
            "cn": "引导用户重新发起航班查询并选择其他可用舱位"
        }
    },
    {
        "code": "ERR_DRIFT",
        "name": "PriceChanged",
        "cause": {
            "vi": "Giá vé của hãng đã biến động sau bước Select",
            "en": "Airline fare basis or taxes changed between select and booking",
            "cn": "从验价到生单期间航司基础运价或税费发生变动"
        },
        "solution": {
            "vi": "Hiển thị giá mới cho khách hàng xác nhận lại",
            "en": "Display updated price quote to traveler for re-confirmation",
            "cn": "向旅客展示最新价格复核结果，待确认后继续提交预订"
        }
    },
    {
        "code": "ERR_LIMIT",
        "name": "InsufficientCreditLimit",
        "cause": {
            "vi": "Hạn mức tài khoản ký quỹ B2B không đủ để xuất vé",
            "en": "Insufficient B2B deposit credit limit to issue ticket",
            "cn": "B2B 预存保证金账户或授信额度不足，无法完成出票扣款"
        },
        "solution": {
            "vi": "Liên hệ bộ phận kế toán HNH để nạp thêm hạn mức",
            "en": "Top up B2B account deposit balance via HNH finance desk",
            "cn": "请联系 HNH 财务或商务团队为账户充值授信额度"
        }
    }
]

SUPPORT_DATA = {
    "title": {
        "vi": "Developer Support & SLA — Kênh Hỗ Trợ Kỹ Thuật",
        "en": "Developer Support & SLA — 24/7 Technical Assistance",
        "cn": "开发者支持与 SLA 保障 — 7x24 技术服务"
    },
    "subtitle": {
        "vi": "Đội ngũ kỹ sư hỗ trợ tích hợp 24/7 của Hồng Ngọc Hà Travel",
        "en": "Dedicated 24/7 integration engineering team by Hong Ngoc Ha Travel",
        "cn": "鸿玉荷旅行社 (Hong Ngoc Ha Travel) 7x24 小时技术保障团队"
    },
    "cards": [
        {
            "label": {"vi": "EMAIL KỸ THUẬT API", "en": "API TECHNICAL SUPPORT", "cn": "接口技术支持邮箱"},
            "value": "api-support@tripota.com.vn"
        },
        {
            "label": {"vi": "HOTLINE NGHIỆP VỤ VÉ 24/7", "en": "24/7 TICKETING DESK HOTLINE", "cn": "7x24 客票业务应急热线"},
            "value": "+84 (0) 28 3914 9999"
        },
        {
            "label": {"vi": "ZALO / TELEGRAM DEV", "en": "DEV CHAT (ZALO / TELEGRAM)", "cn": "开发者通讯群组 (Zalo / TG)"},
            "value": "@HNH_FlightHub_Support"
        },
        {
            "label": {"vi": "CAM KẾT PHẢN HỒI (SLA)", "en": "RESPONSE COMMITMENT (SLA)", "cn": "服务级别保障承诺 (SLA)"},
            "sla": {
                "vi": "< 15 phút đối với sự cố xuất vé khẩn cấp",
                "en": "< 15 minutes for urgent ticketing incidents",
                "cn": "< 15 分钟极速响应紧急出票异常"
            }
        }
    ]
}
