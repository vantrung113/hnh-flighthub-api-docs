# -*- coding: utf-8 -*-
"""
apply_perfect_fixes.py
Applies all 6 critical fixes:
1. Fix header layout so Theme Toggle (Light/Dark) NEVER gets clipped or pushed off screen.
2. Fix Sandbox cURL terminal box: proper newlines (\n) and pre-wrap code wrapping (no horizontal scroll, wraps cleanly).
3. Add Round-Trip (Khứ hồi) vs One-Way (Một chiều) with dynamic return date and 2-leg payload.
4. Remove all internal "Tương lai" text from labels and subtitles.
5. Soften footer signature styling (muted, elegant, not bold/dark) and upgrade wording to Platform Solutions Architect.
6. Clean all 28 endpoint titles (ep-title) with pure trilingual data attributes and zero leftover trailing text.
"""

import re

EXACT_ENDPOINT_TITLES = {
    "/api/v1/sign-in": {
        "method": "POST",
        "vi": "Đăng nhập lấy Token",
        "en": "Sign In (Get Bearer Token)",
        "cn": "账号登录获取 Token"
    },
    "/api/v1/refresh-token": {
        "method": "POST",
        "vi": "Gia hạn Token",
        "en": "Refresh Access Token",
        "cn": "刷新访问令牌"
    },
    "/api/v1/system?isNDC=true": {
        "method": "GET",
        "vi": "Lấy danh sách hệ thống khả dụng",
        "en": "Get Available Airline Systems",
        "cn": "获取可用航司及系统列表"
    },
    "/api/v1/flight/search": {
        "method": "POST",
        "vi": "Tìm kiếm chuyến bay theo ngày",
        "en": "Search Flights by Date",
        "cn": "实时航班运价查询"
    },
    "/api/v1/flight/searchminfare": {
        "method": "POST",
        "vi": "Tìm giá vé rẻ nhất theo tháng (Lịch vé rẻ)",
        "en": "Search Lowest Fare Calendar",
        "cn": "月度低价日历检索"
    },
    "/api/v1/flight/select": {
        "method": "POST",
        "vi": "Xác nhận chọn chuyến bay & Khóa chỗ",
        "en": "Select Flight & Lock Price",
        "cn": "确认航班并锁定价格 (验舱)"
    },
    "/api/v1/flight/pricequote": {
        "method": "POST",
        "vi": "Tái thẩm định giá trước khi xuất vé",
        "en": "Reprice & Quote Verification",
        "cn": "出票前价格二次复核 (Price Quote)"
    },
    "/api/v1/flight/book": {
        "method": "POST",
        "vi": "Tạo đặt chỗ (Sinh mã PNR)",
        "en": "Create Booking (Acquire PNR)",
        "cn": "创建预订 (生成航司 PNR)"
    },
    "/api/v1/flight/facebooking": {
        "method": "POST",
        "vi": "Xem mặt vé (Kiểm tra lại PNR)",
        "en": "Face Booking (Verify PNR Data)",
        "cn": "查看票面信息 (校验 PNR 明细)"
    },
    "/api/v1/flight/issueticket": {
        "method": "POST",
        "vi": "Thực hiện xuất vé chính thức",
        "en": "Issue Official Airline Ticket",
        "cn": "确认支付并正式出票"
    },
    "/api/v1/flight/retrieve": {
        "method": "POST",
        "vi": "Tra cứu đơn đặt chỗ & Tình trạng vé",
        "en": "Retrieve Booking & Ticket Status",
        "cn": "检索订单详情及客票状态"
    },
    "/api/v1/flight/getbaggages": {
        "method": "POST",
        "vi": "Tra cứu các gói hành lý mua thêm",
        "en": "Query Baggage Allowance Packages",
        "cn": "查询付费行李额度包"
    },
    "/api/v1/flight/getseatmap": {
        "method": "POST",
        "vi": "Lấy sơ đồ chỗ ngồi trên máy bay",
        "en": "Get Aircraft Seat Map",
        "cn": "获取机舱座位布局图 (Seat Map)"
    },
    "/api/v1/flight/issueEMD": {
        "method": "POST",
        "vi": "Xuất chứng từ dịch vụ phụ trợ (EMD)",
        "en": "Issue EMD Miscellaneous Document",
        "cn": "出具杂项凭据 (Issue EMD)"
    },
    "/api/v1/flight/infant": {
        "method": "POST",
        "vi": "Thêm em bé vào booking",
        "en": "Add Infant to Booking",
        "cn": "向预订中挂载婴儿旅客"
    },
    "/api/v1/flight/adddocument": {
        "method": "POST",
        "vi": "Thêm giấy tờ tùy thân (Hộ chiếu/CCCD)",
        "en": "Update Travel Document (Passport/ID)",
        "cn": "更新旅客证件信息 (护照/身份证)"
    },
    "/api/v1/flight/addmembership": {
        "method": "POST",
        "vi": "Thêm thẻ khách hàng thân thiết",
        "en": "Update Frequent Flyer Membership",
        "cn": "添加常旅客会员卡号"
    },
    "/api/v1/flight/addosi": {
        "method": "POST",
        "vi": "Thêm chỉ thị hãng (OSI / SK / Remark)",
        "en": "Add Airline Remarks (OSI / SK)",
        "cn": "添加航司业务指令 (OSI / SK / Remark)"
    },
    "/api/v1/flight/updatecontact": {
        "method": "POST",
        "vi": "Cập nhật thông tin liên hệ & hành khách",
        "en": "Update Contact Info & Passenger Details",
        "cn": "更新订单联系人及旅客信息"
    },
    "/api/v1/flight/split": {
        "method": "POST",
        "vi": "Tách hành khách khỏi đoàn (Split PNR)",
        "en": "Split Passenger from PNR (Split PNR)",
        "cn": "拆分订单旅客 (Split PNR)"
    },
    "/api/v1/flight/changeflight": {
        "method": "POST",
        "vi": "Thay đổi hành trình khi chưa xuất vé",
        "en": "Change Itinerary (Pre-Ticketing)",
        "cn": "出票前修改航班航程"
    },
    "/api/v1/flight/cancelbooking": {
        "method": "POST",
        "vi": "Hủy giữ chỗ PNR (Chưa xuất vé)",
        "en": "Cancel Booking (Pre-Ticketing)",
        "cn": "取消预订占用座位 (未出票)"
    },
    "/api/v1/flight/refundticket": {
        "method": "POST",
        "vi": "Quy trình hoàn vé 2 bước",
        "en": "Two-Step Ticket Refund Workflow",
        "cn": "两步式退票流程 (询价与提交)"
    },
    "/api/v1/flight/voidticket": {
        "method": "POST",
        "vi": "Hủy vé trong ngày không mất phí (Void Ticket)",
        "en": "Same-Day Void Ticket (Zero Penalty)",
        "cn": "当日免费废票 (Void Ticket)"
    },
    "/api/v1/flight/exchange-search": {
        "method": "POST",
        "vi": "Đổi vé máy bay (Quy trình 3 bước)",
        "en": "Ticket Reissue & Exchange (3-Step)",
        "cn": "客票改期换开 (三步流程)"
    },
    "/api/v1/flight/farerule": {
        "method": "POST",
        "vi": "Tra cứu điều kiện vé (Fare Rule)",
        "en": "Query Detailed Fare Rules",
        "cn": "查询客票详细退改签规则 (Fare Rule)"
    },
    "/api/v1/flight/checkin-online": {
        "method": "POST",
        "vi": "Làm thủ tục chuyến bay trực tuyến",
        "en": "Online Flight Check-in",
        "cn": "在线值机与登机牌办理"
    },
    "/api/v1/flight/compute-emission": {
        "method": "POST",
        "vi": "Tính toán phát thải CO2 chuyến bay",
        "en": "Calculate Flight Carbon Emission",
        "cn": "计算航班碳排放指标 (CO2)"
    }
}

def run():
    print("Reading index.html...")
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. FIX HEADER & THEME TOGGLE OVERFLOW (Prevent cut off on the right)
    header_css_old = r'\.header\s*\{[^}]*\}'
    header_css_new = '''.header {
  position: fixed; top: 0; left: 0; right: 0; z-index: 100;
  height: var(--header-h);
  background: var(--glass-bg);
  -webkit-backdrop-filter: blur(14px);
  backdrop-filter: blur(14px);
  border-bottom: 1px solid var(--border);
  display: flex; align-items: center; padding: 0 16px;
  gap: 10px;
  box-sizing: border-box;
  transition: background-color 0.25s ease, border-color 0.25s ease;
}
.header-brand {
  display: flex; align-items: center; gap: 10px;
  text-decoration: none;
  flex-shrink: 0;
}
.header-brand-title {
  display: flex; flex-direction: column;
  white-space: nowrap;
}
.header-brand-title .title {
  font-size: 13.5px; font-weight: 700; color: var(--text-primary);
}
.header-brand-title .sub {
  font-size: 11px; color: var(--text-muted);
}
.header-resources {
  display: flex; align-items: center; gap: 5px;
  margin-left: 6px;
  flex-shrink: 1;
  min-width: 0;
}
.res-pill {
  display: inline-flex; align-items: center; gap: 5px;
  padding: 4px 8px; border-radius: 6px;
  font-size: 11.5px; font-weight: 500;
  text-decoration: none;
  border: 1px solid var(--border);
  background: var(--bg-card);
  color: var(--text-secondary);
  white-space: nowrap;
  transition: all 0.2s;
}
.res-pill:hover {
  border-color: var(--accent);
  color: var(--accent);
  background: var(--accent-dim);
}
.header-controls {
  margin-left: auto;
  display: flex; align-items: center; gap: 8px;
  flex-shrink: 0;
}
.nav-search {
  position: relative;
  width: 150px;
}
.nav-search input {
  width: 100%;
  padding: 6px 10px 6px 28px;
  border-radius: 8px;
  border: 1px solid var(--border);
  background: var(--bg-card-alt);
  color: var(--text-primary);
  font-size: 12px;
  outline: none;
  box-sizing: border-box;
  transition: all 0.2s;
}
.nav-search input:focus {
  border-color: var(--accent);
  background: var(--bg-card);
  width: 180px;
}
.theme-btn {
  background: var(--bg-card-alt);
  border: 1px solid var(--border);
  color: var(--text-secondary);
  padding: 6px 10px; border-radius: 8px; cursor: pointer;
  display: flex; align-items: center; gap: 6px;
  font-size: 12px; font-weight: 500;
  transition: all 0.2s;
  font-family: inherit;
  flex-shrink: 0;
  white-space: nowrap;
}
@media (max-width: 1260px) {
  .header-brand-title .sub { display: none; }
  .header-resources .res-pill.json { display: none; }
}
@media (max-width: 1100px) {
  .header-resources .res-pill.swagger { display: none; }
  .nav-search { width: 120px; }
}'''
    html = re.sub(header_css_old, header_css_new, html, count=1)

    # 2. FIX CODE BLOCK PRE WRAP (No horizontal flat line, wraps naturally and cleanly)
    code_css_old = r'pre\s*\{[^}]*\}'
    code_css_new = '''pre {
  margin: 0;
  font-family: 'JetBrains Mono', Consolas, Monaco, monospace;
  font-size: 12.5px;
  line-height: 1.6;
  color: var(--text-code);
  white-space: pre-wrap !important;
  word-break: break-word !important;
  overflow-wrap: break-word !important;
  tab-size: 2;
}
#pgCurlOutput {
  white-space: pre-wrap !important;
  word-break: break-word !important;
  overflow-wrap: break-word !important;
  display: block;
}'''
    html = re.sub(code_css_old, code_css_new, html, count=1)

    # 3. UPDATE PLAYGROUND: TRIP TYPE (ROUND-TRIP & ONE-WAY), RETURN DATE, AND PURGE "TƯƠNG LAI"
    # Header of section playground
    pg_head_old = r'<div class="section" id="playground">\s*<div class="section-header">.*?</div>\s*</div>'
    pg_head_new = '''<div class="section" id="playground">
    <div class="section-header">
      <div class="section-num">⚡</div>
      <div class="section-titles">
        <h2 data-vi="Interactive Sandbox cURL Generator — Tạo Lệnh Test Nhanh" data-en="Interactive Sandbox cURL Generator — Instant API Testing" data-cn="交互式沙箱 cURL 生成器 — 快速测试接口">Interactive Sandbox cURL Generator — Tạo Lệnh Test Nhanh</h2>
        <div class="subtitle" data-vi="Chọn loại hành trình, chặng bay và số lượng hành khách để tạo ngay lệnh cURL gọi vào Sandbox" data-en="Select trip type, route, and passengers to generate instant Sandbox cURL commands" data-cn="选择航程类型、航线与旅客人数，即时生成可直接调用的沙箱 cURL 测试命令">Chọn loại hành trình, chặng bay và số lượng hành khách để tạo ngay lệnh cURL gọi vào Sandbox</div>
      </div>
    </div>'''
    html = re.sub(pg_head_old, pg_head_new, html, count=1, flags=re.DOTALL)

    # Playground form and code block
    pg_form_old = r'<div class="playground-box">.*?</div>\s*</div>\s*<!-- SECTION: AUTHENTICATION'
    pg_form_new = '''<div class="playground-box">
      <div class="pg-form">
        <div class="pg-field">
          <label data-vi="LOẠI HÀNH TRÌNH (TRIP TYPE)" data-en="TRIP TYPE" data-cn="航程类型 (TRIP TYPE)">LOẠI HÀNH TRÌNH (TRIP TYPE)</label>
          <select id="pgTripType" class="pg-select">
            <option value="oneway" data-vi="Một chiều (One-Way)" data-en="One-Way" data-cn="单程 (One-Way)">Một chiều (One-Way)</option>
            <option value="roundtrip" data-vi="Khứ hồi (Round-Trip)" data-en="Round-Trip" data-cn="往返 (Round-Trip)">Khứ hồi (Round-Trip)</option>
          </select>
        </div>

        <div class="pg-field">
          <label data-vi="CHẶNG BAY (ROUTE)" data-en="FLIGHT ROUTE" data-cn="航线选择 (ROUTE)">CHẶNG BAY (ROUTE)</label>
          <select id="pgRoute" class="pg-select">
            <option value="SGN-HAN">SGN → HAN (TP.HCM - Hà Nội)</option>
            <option value="HAN-DAD">HAN → DAD (Hà Nội - Đà Nẵng)</option>
            <option value="SGN-DAD">SGN → DAD (TP.HCM - Đà Nẵng)</option>
            <option value="SGN-PQC">SGN → PQC (TP.HCM - Phú Quốc)</option>
            <option value="SGN-SIN">SGN → SIN (TP.HCM - Singapore)</option>
            <option value="HAN-BKK">HAN → BKK (Hà Nội - Bangkok)</option>
            <option value="HAN-CAN">HAN → CAN (Hà Nội - Quảng Châu)</option>
          </select>
        </div>

        <div class="pg-field">
          <label data-vi="HỆ THỐNG HÃNG (SYSTEM)" data-en="AIRLINE / SYSTEM" data-cn="航司/系统 (SYSTEM)">HỆ THỐNG HÃNG (SYSTEM)</label>
          <select id="pgSystem" class="pg-select">
            <option value="VN">VN — Vietnam Airlines</option>
            <option value="VJ">VJ — Vietjet Air</option>
            <option value="QH">QH — Bamboo Airways</option>
            <option value="VU">VU — Vietravel Airlines</option>
            <option value="1A">1A — Amadeus GDS</option>
            <option value="1S">1S — Sabre GDS</option>
            <option value="TR">TR — Scoot NDC</option>
            <option value="AK">AK — AirAsia LCC</option>
            <option value="9C">9C — Spring Airlines LCC</option>
          </select>
        </div>

        <div class="pg-field">
          <label data-vi="NGÀY ĐI (DEPART DATE)" data-en="DEPARTURE DATE" data-cn="出发日期 (DEPART DATE)">NGÀY ĐI (DEPART DATE)</label>
          <input type="date" id="pgDate" class="pg-input">
        </div>

        <div class="pg-field" id="pgReturnGroup" style="display: none;">
          <label data-vi="NGÀY VỀ (RETURN DATE)" data-en="RETURN DATE" data-cn="返回日期 (RETURN DATE)">NGÀY VỀ (RETURN DATE)</label>
          <input type="date" id="pgReturnDate" class="pg-input">
        </div>

        <div class="pg-field">
          <label data-vi="HÀNH KHÁCH (PASSENGERS)" data-en="PASSENGERS" data-cn="乘机人数 (PASSENGERS)">HÀNH KHÁCH (PASSENGERS)</label>
          <select id="pgPax" class="pg-select">
            <option value="1-0-0" data-vi="1 Người lớn (ADT)" data-en="1 Adult (ADT)" data-cn="1 位成人 (ADT)">1 Người lớn (ADT)</option>
            <option value="2-0-0" data-vi="2 Người lớn (2 ADT)" data-en="2 Adults (2 ADT)" data-cn="2 位成人 (2 ADT)">2 Người lớn (2 ADT)</option>
            <option value="2-1-0" data-vi="2 Người lớn + 1 Trẻ em (CHD)" data-en="2 Adults + 1 Child (CHD)" data-cn="2 成人 + 1 儿童 (CHD)">2 Người lớn + 1 Trẻ em (CHD)</option>
            <option value="1-0-1" data-vi="1 Người lớn + 1 Em bé (INF)" data-en="1 Adult + 1 Infant (INF)" data-cn="1 成人 + 1 婴儿 (INF)">1 Người lớn + 1 Em bé (INF)</option>
          </select>
        </div>
      </div>

      <div class="code-block" style="margin-bottom:0;">
        <div class="code-header">
          <span class="code-lang" data-vi="Lệnh Sandbox cURL (Chạy ngay trên Terminal)" data-en="Sandbox cURL Command (Run directly in Terminal)" data-cn="沙箱测试 cURL 命令 (可在终端直接执行)">Lệnh Sandbox cURL (Chạy ngay trên Terminal)</span>
          <button class="copy-btn" id="pgCopyBtn" data-vi="Sao chép cURL" data-en="Copy cURL" data-cn="复制 cURL">Copy cURL</button>
        </div>
        <pre id="pgCurlOutput"></pre>
      </div>
    </div>
  </div>

  <!-- SECTION: AUTHENTICATION'''
    html = re.sub(pg_form_old, pg_form_new, html, count=1, flags=re.DOTALL)

    # 4. CLEAN ALL 28 ENDPOINT HEADERS (Pure trilingual data attributes, zero duplicate trailing tags)
    for path, info in EXACT_ENDPOINT_TITLES.items():
        m_type = info['method']
        m_cls = 'ep-get' if m_type == 'GET' else 'ep-post'
        vi = info['vi']
        en = info['en']
        cn = info['cn']

        esc_path = re.escape(path)
        pat = rf'<div class="endpoint-header">\s*<span class="ep-method[^"]*">.*?</span>\s*<span class="ep-path">{esc_path}</span>.*?<span class="ep-toggle([^"]*)">.*?</span>\s*</div>'
        
        def make_clean_header(match, m_cls=m_cls, m_type=m_type, path=path, vi=vi, en=en, cn=cn):
            toggle_cls = match.group(1)
            return f'''<div class="endpoint-header">
        <span class="ep-method {m_cls}">{m_type}</span>
        <span class="ep-path">{path}</span>
        <span class="ep-title" data-vi="{vi}" data-en="{en}" data-cn="{cn}">{vi}</span>
        <span class="ep-toggle{toggle_cls}">▼</span>
      </div>'''

        html = re.sub(pat, make_clean_header, html)

    # 5. ELEGANT FOOTER SIGNATURE & SUBTLE STYLING
    footer_old = r'<footer class="site-footer">.*?</footer>'
    footer_new = '''<footer class="site-footer">
    <p class="footer-copy" data-vi="Hong Ngoc Ha Travel (HNH) &nbsp;·&nbsp; Cổng Tích Hợp API B2B &nbsp;·&nbsp; v1.0 &nbsp;·&nbsp; 2026" data-en="Hong Ngoc Ha Travel (HNH) &nbsp;·&nbsp; B2B Aviation Integration Portal &nbsp;·&nbsp; v1.0 &nbsp;·&nbsp; 2026" data-cn="Hong Ngoc Ha Travel (HNH) &nbsp;·&nbsp; B2B 航空分销 API 开发者门户 &nbsp;·&nbsp; v1.0 &nbsp;·&nbsp; 2026">Hong Ngoc Ha Travel (HNH) &nbsp;·&nbsp; B2B Aviation Integration Portal &nbsp;·&nbsp; v1.0 &nbsp;·&nbsp; 2026</p>
    <p class="signature">Crafted with <span class="heart">♥</span> by Trung Nguyễn · Platform Solutions Architect</p>
  </footer>'''
    html = re.sub(footer_old, footer_new, html, count=1, flags=re.DOTALL)

    css_sig_old = r'\.site-footer\s*\{.*?\.site-footer\s+\.signature\s*\{[^}]*\}'
    css_sig_new = '''.site-footer {
  margin-top: 60px;
  padding: 32px 0 24px 0;
  border-top: 1px solid var(--border);
  text-align: center;
}
.site-footer .footer-copy {
  font-size: 13px;
  color: var(--text-muted);
  opacity: 0.8;
}
.site-footer .signature {
  margin-top: 8px;
  font-size: 12px;
  font-weight: 400;
  color: var(--text-muted);
  opacity: 0.65;
  letter-spacing: 0.3px;
}
.site-footer .signature .heart {
  color: #f43f5e;
  opacity: 0.8;
  display: inline-block;
  margin: 0 2px;
}'''
    html = re.sub(css_sig_old, css_sig_new, html, count=1, flags=re.DOTALL)

    # 6. JAVASCRIPT: PROPER MULTI-LINE CURL GENERATION WITH CLEAN NEWLINES
    js_section7_old = r'// 7\. SANDBOX CURL PLAYGROUND GENERATOR.*?// 8\.'
    js_section7_new = '''// 7. SANDBOX CURL PLAYGROUND GENERATOR (ONE-WAY & ROUND-TRIP)
function initDynamicDates() {
  var today = new Date();
  var depart = new Date();
  depart.setDate(today.getDate() + 7);

  var ret = new Date();
  ret.setDate(today.getDate() + 11);

  function formatDate(d) {
    var yyyy = d.getFullYear();
    var mm = String(d.getMonth() + 1).padStart(2, '0');
    var dd = String(d.getDate()).padStart(2, '0');
    return yyyy + '-' + mm + '-' + dd;
  }

  var minStr = formatDate(today);
  var departStr = formatDate(depart);
  var returnStr = formatDate(ret);

  var dInput = document.getElementById('pgDate');
  var rInput = document.getElementById('pgReturnDate');
  if (dInput) {
    dInput.value = departStr;
    dInput.min = minStr;
  }
  if (rInput) {
    rInput.value = returnStr;
    rInput.min = departStr;
  }
}
initDynamicDates();

function updateSandboxCurl() {
  var tripTypeEl = document.getElementById('pgTripType');
  var tripType = tripTypeEl ? tripTypeEl.value : 'oneway';
  var returnGroup = document.getElementById('pgReturnGroup');
  
  if (returnGroup) {
    if (tripType === 'roundtrip') {
      returnGroup.style.display = 'flex';
      returnGroup.style.flexDirection = 'column';
    } else {
      returnGroup.style.display = 'none';
    }
  }

  var routeEl = document.getElementById('pgRoute');
  var route = (routeEl ? routeEl.value : 'SGN-HAN').split('-');
  var systemEl = document.getElementById('pgSystem');
  var system = systemEl ? systemEl.value : 'VN';
  var dInput = document.getElementById('pgDate');
  var departDate = dInput ? dInput.value : '';
  var returnDateEl = document.getElementById('pgReturnDate');
  var returnDate = returnDateEl ? returnDateEl.value : '';
  var paxEl = document.getElementById('pgPax');
  var pax = (paxEl ? paxEl.value : '1-0-0').split('-');

  // Keep return date >= depart date
  if (returnDateEl && departDate) {
    returnDateEl.min = departDate;
    if (returnDate && returnDate < departDate) {
      returnDateEl.value = departDate;
      returnDate = departDate;
    }
  }

  var flights = [
    {
      leg: 0,
      startPoint: route[0],
      endPoint: route[1],
      departDate: departDate
    }
  ];

  if (tripType === 'roundtrip') {
    flights.push({
      leg: 1,
      startPoint: route[1],
      endPoint: route[0],
      departDate: returnDate || departDate
    });
  }

  var payload = {
    system: system,
    adt: parseInt(pax[0]) || 1,
    chd: parseInt(pax[1]) || 0,
    inf: parseInt(pax[2]) || 0,
    flights: flights
  };

  var payloadJson = JSON.stringify(payload, null, 2);
  var curlLines = [
    'curl -X POST "https://sandbox-apihub.tripota.com.vn/api/v1/flight/search" \\\\',
    '  -H "Content-Type: application/json" \\\\',
    '  -H "Authorization: Bearer YOUR_SANDBOX_TOKEN" \\\\',
    '  -d \\'' + payloadJson + '\\''
  ];

  var outEl = document.getElementById('pgCurlOutput');
  if (outEl) {
    outEl.textContent = curlLines.join('\\n');
  }
}

['pgTripType', 'pgRoute', 'pgSystem', 'pgDate', 'pgReturnDate', 'pgPax'].forEach(function(id) {
  var el = document.getElementById(id);
  if (el) {
    el.addEventListener('change', updateSandboxCurl);
    el.addEventListener('input', updateSandboxCurl);
  }
});
updateSandboxCurl();

// 8.'''
    html = re.sub(js_section7_old, js_section7_new, html, count=1, flags=re.DOTALL)

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("All fixes applied successfully! File length:", len(html))

if __name__ == '__main__':
    run()
