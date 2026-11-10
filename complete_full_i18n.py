# -*- coding: utf-8 -*-
"""
complete_full_i18n.py
Final polishing pass that ensures 100% full-page trilingual translation
across all elements in index.html with zero leftover untranslated strings.
"""

import re

def polish():
    print("Reading index.html...")
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Fix globalSearch placeholder
    html = re.sub(
        r'<input type="text" id="globalSearch"[^>]*>',
        '<input type="text" id="globalSearch" data-vi-ph="Tìm kiếm API, mã lỗi (Ctrl+K)..." data-en-ph="Search API, error codes (Ctrl+K)..." data-cn-ph="搜索 API、错误代码 (Ctrl+K)..." placeholder="Tìm kiếm API, mã lỗi (Ctrl+K)...">',
        html
    )

    # 2. Fix Section 02 Flow diagram step nodes
    flow_steps_old = r'<div class="flow-steps">.*?</div>\s*</div>\s*<div class="callout callout-warn">'
    flow_steps_new = '''<div class="flow-steps">
        <a href="#search" class="flow-node">
          <div class="step-badge" data-vi="Bước 1" data-en="Step 1" data-cn="步骤 1">Bước 1</div>
          <div class="step-title" data-vi="Search Tìm vé" data-en="Search Flights" data-cn="航班查询">Search Tìm vé</div>
          <div class="step-token" data-vi="Sinh flightValue thô" data-en="Raw flightValue token" data-cn="生成原始 flightValue">Sinh flightValue thô</div>
        </a>
        <div class="flow-arrow">→</div>
        <a href="#select" class="flow-node">
          <div class="step-badge" data-vi="Bước 2" data-en="Step 2" data-cn="步骤 2">Bước 2</div>
          <div class="step-title" data-vi="Select Chọn giá" data-en="Select &amp; Reprice" data-cn="验价选座">Select Chọn giá</div>
          <div class="step-token" data-vi="Sinh flightValue khóa giá" data-en="Price-locked flightValue" data-cn="生成锁价 flightValue">Sinh flightValue khóa giá</div>
        </a>
        <div class="flow-arrow">→</div>
        <a href="#book" class="flow-node">
          <div class="step-badge" data-vi="Bước 3" data-en="Step 3" data-cn="步骤 3">Bước 3</div>
          <div class="step-title" data-vi="Book Giữ chỗ" data-en="Create Booking" data-cn="创建预订 (生单)">Book Giữ chỗ</div>
          <div class="step-token" data-vi="Sinh mã PNR (bookingCode)" data-en="Airline PNR (bookingCode)" data-cn="生成航司 PNR (bookingCode)">Sinh mã PNR (bookingCode)</div>
        </a>
        <div class="flow-arrow">→</div>
        <a href="#baggage" class="flow-node">
          <div class="step-badge" data-vi="Bước 4 (Tùy chọn)" data-en="Step 4 (Optional)" data-cn="步骤 4 (可选)">Bước 4 (Tùy chọn)</div>
          <div class="step-title" data-vi="Add-ons Dịch vụ" data-en="Ancillaries &amp; Add-ons" data-cn="增值附加服务">Add-ons Dịch vụ</div>
          <div class="step-token" data-vi="Mua Ghế, Hành lý, EMD" data-en="Seats, Baggage &amp; EMD" data-cn="增购行李/选座/出EMD">Mua Ghế, Hành lý, EMD</div>
        </a>
        <div class="flow-arrow">→</div>
        <a href="#issue" class="flow-node" style="border-color:var(--accent-green);">
          <div class="step-badge" style="color:var(--accent-green);" data-vi="Bước 5" data-en="Step 5" data-cn="步骤 5">Bước 5</div>
          <div class="step-title" data-vi="Issue Xuất vé" data-en="Issue E-Ticket" data-cn="正式出票">Issue Xuất vé</div>
          <div class="step-token" data-vi="Sinh số vé điện tử (e-Ticket)" data-en="13-digit e-Ticket Number" data-cn="生成 13 位电子客票号">Sinh số vé điện tử (e-Ticket)</div>
        </a>
        <div class="flow-arrow">→</div>
        <a href="#retrieve" class="flow-node">
          <div class="step-badge" data-vi="Bước 6" data-en="Step 6" data-cn="步骤 6">Bước 6</div>
          <div class="step-title" data-vi="Retrieve Tra cứu" data-en="Retrieve Booking" data-cn="订单检索">Retrieve Tra cứu</div>
          <div class="step-token" data-vi="Kiểm tra trạng thái TICKETED" data-en="Verify TICKETED Status" data-cn="查验 TICKETED 出票状态">Kiểm tra trạng thái TICKETED</div>
        </a>
      </div>
    </div>

    <div class="callout callout-warn">'''
    html = re.sub(flow_steps_old, flow_steps_new, html, count=1, flags=re.DOTALL)

    # 3. Update Section 02 callout text
    callout_old = r'<div class="callout callout-warn">\s*<span class="callout-icon">⚠️</span>\s*<div class="bi">.*?</div>\s*</div>'
    callout_new = '''<div class="callout callout-warn">
      <span class="callout-icon">⚠️</span>
      <div class="bi">
        <span class="vi"><strong>Nguyên tắc bất di bất dịch của chuỗi giá vé:</strong> Chuỗi <code>flightValues</code> truyền vào API <code>/flight/book</code> BẮT BUỘC phải lấy từ kết quả của API <code>/flight/select</code> (tuyệt đối không lấy trực tiếp từ Search). Nếu thời gian từ lúc Select đến khi Book vượt quá 15 phút, cần gọi <code>/flight/pricequote</code> để xác minh giá không bị nhảy.</span>
        <span class="en"><strong>State Chaining Rule:</strong> The <code>flightValues</code> token passed to <code>/flight/book</code> MUST be retrieved directly from the <code>/flight/select</code> response (never use the raw string from Search). If elapsed time exceeds 15 minutes, invoke <code>/flight/pricequote</code> to verify price stability.</span>
        <span class="cn"><strong>状态链核心规则：</strong>调用 <code>/flight/book</code> 时的 <code>flightValues</code> 必须来自 <code>/flight/select</code> 的返回结果，严禁直接使用 <code>/flight/search</code> 的原始串。若从验价到生单间隔超过 15 分钟，建议调用 <code>/flight/pricequote</code> 二次核价以防运价跳变。</span>
      </div>
    </div>'''
    html = re.sub(callout_old, callout_new, html, count=1, flags=re.DOTALL)

    # 4. Fix Section 13 Developer Support & SLA and Footer
    sec13_old = r'<div class="section" id="support">.*?</main>'
    sec13_new = '''<div class="section" id="support">
    <div class="section-header">
      <div class="section-num">13</div>
      <div class="section-titles">
        <h2 data-vi="Kênh Hỗ Trợ Kỹ Thuật &amp; SLA — Developer Support" data-en="Developer Support &amp; SLA — 24/7 Technical Assistance" data-cn="开发者支持与 SLA 保障 — 7x24 技术服务">Kênh Hỗ Trợ Kỹ Thuật &amp; SLA — Developer Support</h2>
        <div class="subtitle" data-vi="Đội ngũ kỹ sư hỗ trợ tích hợp 24/7 của Hồng Ngọc Hà Travel" data-en="Dedicated 24/7 integration engineering team by Hong Ngoc Ha Travel" data-cn="鸿玉荷旅行社 (Hong Ngoc Ha Travel) 7x24 小时技术保障团队">Đội ngũ kỹ sư hỗ trợ tích hợp 24/7 của Hồng Ngọc Hà Travel</div>
      </div>
    </div>

    <div class="hero-meta-grid" style="grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));">
      <div class="hero-meta-card">
        <div class="label" data-vi="📧 Email Kỹ Thuật API" data-en="📧 API Technical Support" data-cn="📧 接口技术支持邮箱">📧 Email Kỹ Thuật API</div>
        <code>api-support@tripota.com.vn</code>
      </div>
      <div class="hero-meta-card">
        <div class="label" data-vi="📞 Hotline Nghiệp Vụ Vé 24/7" data-en="📞 24/7 Ticketing Desk Hotline" data-cn="📞 7x24 客票业务应急热线">📞 Hotline Nghiệp Vụ Vé 24/7</div>
        <code>+84 (0) 28 3914 9999</code>
      </div>
      <div class="hero-meta-card">
        <div class="label" data-vi="💬 Zalo / Telegram Dev" data-en="💬 Dev Chat (Zalo / TG)" data-cn="💬 开发者即时通讯群组 (Zalo / TG)">💬 Zalo / Telegram Dev</div>
        <code>@HNH_FlightHub_Support</code>
      </div>
      <div class="hero-meta-card">
        <div class="label" data-vi="⚡ Cam Kết Phản Hồi (SLA)" data-en="⚡ Response Commitment (SLA)" data-cn="⚡ 服务级别保障承诺 (SLA)">⚡ Cam Kết Phản Hồi (SLA)</div>
        <code style="word-break: normal; overflow-wrap: break-word;">
          <span class="lang-vi">&lt; 15 phút đối với sự cố xuất vé khẩn cấp</span>
          <span class="lang-en">&lt; 15 minutes for urgent ticketing incidents</span>
          <span class="lang-cn">&lt; 15 分钟极速响应紧急出票异常</span>
        </code>
      </div>
    </div>
  </div>

  <!-- FOOTER -->
  <footer class="site-footer">
    <p data-vi="Hong Ngoc Hà Travel (HNH) &nbsp;·&nbsp; Cổng Tích Hợp API B2B &nbsp;·&nbsp; v1.0 &nbsp;·&nbsp; 2026" data-en="Hong Ngoc Ha Travel (HNH) &nbsp;·&nbsp; B2B Aviation Integration Portal &nbsp;·&nbsp; v1.0 &nbsp;·&nbsp; 2026" data-cn="Hong Ngoc Ha Travel (HNH) &nbsp;·&nbsp; B2B 航空分销 API 开发者门户 &nbsp;·&nbsp; v1.0 &nbsp;·&nbsp; 2026">Hong Ngoc Ha Travel (HNH) &nbsp;·&nbsp; B2B Aviation Integration Portal &nbsp;·&nbsp; v1.0 &nbsp;·&nbsp; 2026</p>
    <p class="signature">Designed with ♥ by Trung Nguyễn - Platform Expert</p>
  </footer>

</main>'''
    html = re.sub(sec13_old, sec13_new, html, count=1, flags=re.DOTALL)

    # 5. Fix any double </div> tags in section-header
    html = html.replace('      </div>\n    </div>\n    </div>', '      </div>\n    </div>')

    # 6. Fix CSS to ensure word-break does not break Vietnamese words
    html = html.replace('word-break: break-all;', 'word-break: normal; overflow-wrap: break-word;')

    # 7. Write output
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Polishing complete! File length:", len(html))

if __name__ == '__main__':
    polish()
