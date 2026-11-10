# -*- coding: utf-8 -*-
"""
patch_full_i18n.py
Comprehensive transformer that reads index.html and ensures 100% full-page i18n
for Vietnamese (VI), English (EN), and Simplified Chinese (CN).
"""

import re
from portal_data import NAV_DATA, HERO_DATA
from portal_translations import SECTION_HEADERS, ENDPOINT_TITLES, ERROR_ROWS, SUPPORT_DATA

def main():
    print("Reading index.html...")
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Update Brand in Header
    brand_old_pattern = r'<div class="brand-text">.*?</div>\s*</div>'
    brand_new = '''<div class="brand-text">
      <div class="brand-title" data-vi="Hong Ngoc Ha Travel — Cổng API Flight Hub" data-en="Hong Ngoc Ha Travel — Flight Hub API" data-cn="Hong Ngoc Ha Travel — 航空 Flight Hub API">Hong Ngoc Ha Travel — Flight Hub API</div>
      <div class="brand-sub" data-vi="Cổng Tích Hợp Đại Lý B2B" data-en="B2B Aviation Partner Integration Portal" data-cn="B2B 航空合作伙伴集成门户">B2B Aviation Partner Integration Portal</div>
    </div>
  </div>'''
    html = re.sub(brand_old_pattern, brand_new, html, count=1, flags=re.DOTALL)

    # 2. Update Header 4 Quick Links with i18n
    header_links_old = r'<div class="header-links">.*?</div>\s*<!-- SEARCH'
    header_links_new = '''<div class="header-links">
      <a href="https://flight-doc.tripota.com.vn/docs/intro/" target="_blank" class="header-link link-docs"><span class="dot"></span> <span data-vi="Tài liệu chi tiết" data-en="Docs" data-cn="开发文档">Docs</span></a>
      <a href="https://sandbox-apihub.tripota.com.vn" target="_blank" class="header-link link-sandbox"><span class="dot"></span> <span data-vi="Sandbox API" data-en="Sandbox API" data-cn="沙箱接口">Sandbox API</span></a>
      <a href="https://flight-api-hub-dev.tripota.com.vn/swagger/index.html" target="_blank" class="header-link link-swagger"><span class="dot"></span> <span data-vi="Swagger UI" data-en="Swagger UI" data-cn="Swagger 控制台">Swagger UI</span></a>
      <a href="https://flight-api-hub-dev.tripota.com.vn/swagger/flight-hub/swagger.json" target="_blank" class="header-link link-openapi"><span class="dot"></span> <span data-vi="OpenAPI JSON" data-en="OpenAPI JSON" data-cn="OpenAPI 规范">OpenAPI JSON</span></a>
    </div>
    <!-- SEARCH'''
    html = re.sub(header_links_old, header_links_new, html, count=1, flags=re.DOTALL)

    # 3. Update Global Search placeholder
    html = re.sub(
        r'<input type="text" class="search-input" id="globalSearch".*?>',
        '<input type="text" class="search-input" id="globalSearch" data-vi-ph="Tìm kiếm API, mã lỗi (Ctrl+K)..." data-en-ph="Search API, error codes (Ctrl+K)..." data-cn-ph="搜索 API、错误代码 (Ctrl+K)..." placeholder="Tìm kiếm API, mã lỗi (Ctrl+K)...">',
        html
    )

    # 4. Generate Complete Sidebar from NAV_DATA
    sidebar_lines = ['<nav class="sidebar" id="sidebarNav">']
    for group in NAV_DATA:
        g_vi = group['title']['vi']
        g_en = group['title']['en']
        g_cn = group['title']['cn']
        sidebar_lines.append(f'  <div class="nav-section">')
        sidebar_lines.append(f'    <div class="nav-section-title" data-vi="{g_vi}" data-en="{g_en}" data-cn="{g_cn}">{g_vi}</div>')
        for item in group['items']:
            iid = item['id']
            i_vi = item['title']['vi']
            i_en = item['title']['en']
            i_cn = item['title']['cn']
            prefix = ''
            if 'icon' in item:
                prefix = f'<span>{item["icon"]}</span> '
            elif 'method' in item:
                m = item['method']
                m_class = 'method-get' if m == 'GET' else 'method-post'
                prefix = f'<span class="nav-method {m_class}">{m}</span> '
            badge_html = ''
            if 'badge' in item:
                b_vi = item['badge']['vi']
                b_en = item['badge']['en']
                b_cn = item['badge']['cn']
                badge_html = f' <span class="nav-badge badge-new" data-vi="{b_vi}" data-en="{b_en}" data-cn="{b_cn}">{b_vi}</span>'
            active_class = ' active' if iid == 'overview' else ''
            sidebar_lines.append(f'    <a class="nav-link{active_class}" data-target="{iid}">{prefix}<span class="nav-text" data-vi="{i_vi}" data-en="{i_en}" data-cn="{i_cn}">{i_vi}</span>{badge_html}</a>')
        sidebar_lines.append('  </div>\n')
    sidebar_lines.append('</nav>')
    sidebar_full_html = '\n'.join(sidebar_lines)

    html = re.sub(r'<nav class="sidebar" id="sidebarNav">.*?</nav>', sidebar_full_html, html, count=1, flags=re.DOTALL)

    # 5. Update Hero 4 Meta Cards
    hero_cards_old = r'<div class="hero-meta-grid">.*?</div>\s*</div>\s*<!-- SECTION: CONTENT SOURCES'
    hero_cards_new = '''<div class="hero-meta-grid">
      <div class="hero-meta-card">
        <div class="label" data-vi="📘 Tài liệu chi tiết (Docs)" data-en="📘 Detailed Documentation (Docs)" data-cn="📘 详细技术文档 (Docs)">📘 Tài liệu chi tiết (Docs)</div>
        <code><a href="https://flight-doc.tripota.com.vn/docs/intro/" target="_blank" style="color:inherit;text-decoration:none;">flight-doc.tripota.com.vn</a></code>
      </div>
      <div class="hero-meta-card">
        <div class="label" data-vi="🧪 Môi trường Sandbox Test" data-en="🧪 Sandbox Testing Environment" data-cn="🧪 沙箱测试环境 (Sandbox)">🧪 Môi trường Sandbox Test</div>
        <code><a href="https://sandbox-apihub.tripota.com.vn" target="_blank" style="color:inherit;text-decoration:none;">sandbox-apihub.tripota.com.vn</a></code>
      </div>
      <div class="hero-meta-card">
        <div class="label" data-vi="🛠️ Swagger UI Dev Console" data-en="🛠️ Swagger UI Dev Console" data-cn="🛠️ Swagger 交互控制台">🛠️ Swagger UI Dev Console</div>
        <code><a href="https://flight-api-hub-dev.tripota.com.vn/swagger/index.html" target="_blank" style="color:inherit;text-decoration:none;">Swagger API Console v1.0</a></code>
      </div>
      <div class="hero-meta-card">
        <div class="label" data-vi="📄 OpenAPI 3.0 Spec JSON" data-en="📄 OpenAPI 3.0 Spec JSON" data-cn="📄 OpenAPI 3.0 规范 JSON">📄 OpenAPI 3.0 Spec JSON</div>
        <code><a href="https://flight-api-hub-dev.tripota.com.vn/swagger/flight-hub/swagger.json" target="_blank" style="color:inherit;text-decoration:none;">swagger.json (53 Endpoints)</a></code>
      </div>
    </div>
  </div>

  <!-- SECTION: CONTENT SOURCES'''
    html = re.sub(hero_cards_old, hero_cards_new, html, count=1, flags=re.DOTALL)

    # 6. Update all Section Headers with data-vi, data-en, data-cn
    for sec_id, info in SECTION_HEADERS.items():
        s_num = info['num']
        t_vi = info['title']['vi']
        t_en = info['title']['en']
        t_cn = info['title']['cn']
        sub_vi = info['subtitle']['vi']
        sub_en = info['subtitle']['en']
        sub_cn = info['subtitle']['cn']

        pattern = rf'(id=["\']{sec_id}["\'].*?<div class="section-header">).*?(</div>\s*</div>)'
        replacement = rf'''\1
      <div class="section-num">{s_num}</div>
      <div class="section-titles">
        <h2 data-vi="{t_vi}" data-en="{t_en}" data-cn="{t_cn}">{t_vi}</h2>
        <div class="subtitle" data-vi="{sub_vi}" data-en="{sub_en}" data-cn="{sub_cn}">{sub_vi}</div>
      </div>
    </div>'''
        html = re.sub(pattern, replacement, html, count=1, flags=re.DOTALL)

    # 7. Update Interactive Playground Form Labels & Options
    pg_form_old = r'<div class="playground-body">.*?<div class="curl-output-wrap">'
    pg_form_new = '''<div class="playground-body">
      <div class="playground-form">
        <div class="pg-form-group">
          <label data-vi="CHẶNG BAY (ROUTE)" data-en="FLIGHT ROUTE" data-cn="航线选择 (ROUTE)">CHẶNG BAY (ROUTE)</label>
          <select class="pg-select" id="pgRoute">
            <option value="SGN-HAN">SGN → HAN (TP.HCM - Hà Nội)</option>
            <option value="HAN-DAD">HAN → DAD (Hà Nội - Đà Nẵng)</option>
            <option value="SGN-PQC">SGN → PQC (TP.HCM - Phú Quốc)</option>
            <option value="SGN-BKK">SGN → BKK (TP.HCM - Bangkok)</option>
            <option value="HAN-SIN">HAN → SIN (Hà Nội - Singapore)</option>
            <option value="HAN-CAN">HAN → CAN (Hà Nội - Quảng Châu)</option>
          </select>
        </div>

        <div class="pg-form-group">
          <label data-vi="HỆ THỐNG HÃNG (SYSTEM)" data-en="AIRLINE / SYSTEM" data-cn="航司/系统 (SYSTEM)">HỆ THỐNG HÃNG (SYSTEM)</label>
          <select class="pg-select" id="pgSystem">
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

        <div class="pg-form-group">
          <label data-vi="NGÀY BAY (DEPART DATE)" data-en="DEPARTURE DATE" data-cn="出发日期 (DEPART DATE)">NGÀY BAY (DEPART DATE)</label>
          <input type="date" class="pg-input" id="pgDate">
        </div>

        <div class="pg-form-group">
          <label data-vi="HÀNH KHÁCH (PASSENGERS)" data-en="PASSENGERS" data-cn="乘机人数 (PASSENGERS)">HÀNH KHÁCH (PASSENGERS)</label>
          <select class="pg-select" id="pgPax">
            <option value="1-0-0" data-vi="1 Người lớn (ADT)" data-en="1 Adult (ADT)" data-cn="1 位成人 (ADT)">1 Người lớn (ADT)</option>
            <option value="2-0-0" data-vi="2 Người lớn (2 ADT)" data-en="2 Adults (2 ADT)" data-cn="2 位成人 (2 ADT)">2 Người lớn (2 ADT)</option>
            <option value="1-1-0" data-vi="1 Người lớn + 1 Trẻ em (1 ADT + 1 CHD)" data-en="1 Adult + 1 Child (1 ADT + 1 CHD)" data-cn="1 成人 + 1 儿童 (1 ADT + 1 CHD)">1 Người lớn + 1 Trẻ em (1 ADT + 1 CHD)</option>
            <option value="1-0-1" data-vi="1 Người lớn + 1 Em bé (1 ADT + 1 INF)" data-en="1 Adult + 1 Infant (1 ADT + 1 INF)" data-cn="1 成人 + 1 婴儿 (1 ADT + 1 INF)">1 Người lớn + 1 Em bé (1 ADT + 1 INF)</option>
          </select>
        </div>
      </div>

      <div class="curl-output-wrap">'''
    html = re.sub(pg_form_old, pg_form_new, html, count=1, flags=re.DOTALL)

    # Playground terminal header
    html = re.sub(
        r'<div class="curl-head">.*?</div>',
        '''<div class="curl-head">
          <span class="curl-title" data-vi="Lệnh Sandbox cURL (Chạy ngay trên Terminal)" data-en="Sandbox cURL Command (Run directly in Terminal)" data-cn="沙箱测试 cURL 命令 (可在终端直接执行)">Lệnh Sandbox cURL (Chạy ngay trên Terminal)</span>
          <button class="copy-btn" id="pgCopyBtn" data-vi="Sao chép" data-en="Copy" data-cn="复制">Sao chép</button>
        </div>''',
        html,
        count=1,
        flags=re.DOTALL
    )

    # 8. Update all 28 Endpoint Headers (ep-title)
    for path, ep_dict in ENDPOINT_TITLES.items():
        vi_t = ep_dict['vi']
        en_t = ep_dict['en']
        cn_t = ep_dict['cn']
        
        # Regex to find the endpoint header for this path
        # <span class="ep-path">/api/v1/sign-in</span>\s*<span class="ep-title">.*?</span>
        pat = rf'(<span class="ep-path">{re.escape(path)}</span>\s*)<span class="ep-title">.*?</span>'
        rep = rf'\1<span class="ep-title" data-vi="{vi_t}" data-en="{en_t}" data-cn="{cn_t}">{vi_t}</span>'
        html = re.sub(pat, rep, html)

    # 9. Update Table 0 Headers (Content Sources)
    tbl0_head_old = r'<table class="field-table">\s*<thead>\s*<tr>\s*<th style="width: 25%;">.*?</tr>\s*</thead>'
    tbl0_head_new = '''<table class="field-table">
      <thead>
        <tr>
          <th style="width: 25%;" data-vi="Phân nhóm (Category)" data-en="Category" data-cn="系统分类">Phân nhóm (Category)</th>
          <th style="width: 15%;" data-vi="Mã hệ thống (System Code)" data-en="System Code" data-cn="系统代码">Mã hệ thống (System Code)</th>
          <th style="width: 35%;" data-vi="Tên Hãng / Nhà cung cấp" data-en="Airline / Provider Name" data-cn="航司 / 渠道名称">Tên Hãng / Nhà cung cấp</th>
          <th style="width: 25%;" data-vi="Phương thức kết nối" data-en="Connection Type" data-cn="对接类型">Phương thức kết nối</th>
        </tr>
      </thead>'''
    html = re.sub(tbl0_head_old, tbl0_head_new, html, count=1, flags=re.DOTALL)

    # 10. Update Request / Response Table Headers
    html = re.sub(
        r'<thead><tr><th>Trường \(Field\)</th><th>Kiểu</th><th>Bắt buộc</th><th>Ý nghĩa &amp; Chú thích</th></tr></thead>',
        '<thead><tr><th data-vi="Trường (Field)" data-en="Field" data-cn="参数名称">Trường (Field)</th><th data-vi="Kiểu" data-en="Type" data-cn="数据类型">Kiểu</th><th data-vi="Bắt buộc" data-en="Required" data-cn="必填">Bắt buộc</th><th data-vi="Ý nghĩa &amp; Chú thích" data-en="Description" data-cn="说明与注释">Ý nghĩa &amp; Chú thích</th></tr></thead>',
        html
    )
    html = re.sub(
        r'<thead><tr><th>Tham số</th><th>Kiểu</th><th>Bắt buộc</th><th>Ý nghĩa &amp; Ràng buộc nghiệp vụ</th></tr></thead>',
        '<thead><tr><th data-vi="Tham số" data-en="Parameter" data-cn="参数名称">Tham số</th><th data-vi="Kiểu" data-en="Type" data-cn="数据类型">Kiểu</th><th data-vi="Bắt buộc" data-en="Required" data-cn="必填">Bắt buộc</th><th data-vi="Ý nghĩa &amp; Ràng buộc nghiệp vụ" data-en="Business Rules &amp; Meaning" data-cn="业务规则与说明">Ý nghĩa &amp; Ràng buộc nghiệp vụ</th></tr></thead>',
        html
    )
    html = re.sub(
        r'<thead><tr><th>Trường</th><th>Kiểu</th><th>Bắt buộc</th><th>Ý nghĩa</th></tr></thead>',
        '<thead><tr><th data-vi="Trường (Field)" data-en="Field" data-cn="参数名称">Trường</th><th data-vi="Kiểu" data-en="Type" data-cn="数据类型">Kiểu</th><th data-vi="Bắt buộc" data-en="Required" data-cn="必填">Bắt buộc</th><th data-vi="Ý nghĩa" data-en="Description" data-cn="说明">Ý nghĩa</th></tr></thead>',
        html
    )

    # Update Required badges
    html = re.sub(
        r'<span class="req-badge req-yes">BẮT BUỘC</span>',
        '<span class="req-badge req-yes" data-vi="BẮT BUỘC" data-en="REQUIRED" data-cn="必填">BẮT BUỘC</span>',
        html
    )

    # 11. Replace Error Code Search & Table
    err_rows_html = []
    for r in ERROR_ROWS:
        code = r['code']
        name = r['name']
        c_vi = r['cause']['vi']
        c_en = r['cause']['en']
        c_cn = r['cause']['cn']
        s_vi = r['solution']['vi']
        s_en = r['solution']['en']
        s_cn = r['solution']['cn']

        row_str = f'''          <tr>
            <td><code class="req-badge req-yes">{code}</code></td>
            <td><strong>{name}</strong></td>
            <td>
              <div class="bi">
                <span class="vi">{c_vi}</span>
                <span class="en">{c_en}</span>
                <span class="cn">{c_cn}</span>
              </div>
            </td>
            <td>
              <div class="bi">
                <span class="vi">{s_vi}</span>
                <span class="en">{s_en}</span>
                <span class="cn">{s_cn}</span>
              </div>
            </td>
          </tr>'''
        err_rows_html.append(row_str)

    error_section_new = f'''    <div class="error-lookup-wrap">
      <input type="text" class="error-search-input" id="errorSearch" data-vi-ph="Gõ mã lỗi (00004, 00001, token, name, seat, limit...) để tra cứu ngay..." data-en-ph="Type error code (00004, 00001, token, name, seat, limit...) to search..." data-cn-ph="输入错误代码 (00004, 00001, token, name, seat, limit...) 立即检索..." placeholder="Gõ mã lỗi (00004, 00001, token, name, seat, limit...) để tra cứu ngay...">
      
      <table class="field-table" id="errorTable">
        <thead>
          <tr>
            <th style="width: 15%;" data-vi="Mã lỗi" data-en="Error Code" data-cn="错误代码">Mã lỗi</th>
            <th style="width: 25%;" data-vi="Tên lỗi kỹ thuật" data-en="Technical Name" data-cn="技术标识">Tên lỗi kỹ thuật</th>
            <th style="width: 35%;" data-vi="Nguyên nhân &amp; Ý nghĩa" data-en="Root Cause &amp; Meaning" data-cn="故障原因与含义">Nguyên nhân &amp; Ý nghĩa</th>
            <th style="width: 25%;" data-vi="Hướng xử lý" data-en="Resolution &amp; Workaround" data-cn="排查与解决方案">Hướng xử lý</th>
          </tr>
        </thead>
        <tbody>
{chr(10).join(err_rows_html)}
        </tbody>
      </table>
    </div>'''

    html = re.sub(r'<div class="error-lookup-wrap">.*?</table>\s*</div>', error_section_new, html, count=1, flags=re.DOTALL)

    # 12. Remove any "thực chiến" / "实战" from headings and comments
    html = html.replace('Python thực chiến', 'Python hoàn chỉnh')
    html = html.replace('thực chiến', 'hoàn chỉnh')
    html = html.replace('实战', '端到端')

    # 13. Update Developer Support & SLA Section
    support_new = '''  <!-- SECTION: DEVELOPER SUPPORT & SLA -->
  <div class="section" id="support">
    <div class="section-header">
      <div class="section-num">13</div>
      <div class="section-titles">
        <h2 data-vi="Kênh Hỗ Trợ Kỹ Thuật &amp; SLA — Developer Support" data-en="Developer Support &amp; SLA — 24/7 Technical Assistance" data-cn="开发者支持与 SLA 保障 — 7x24 技术服务">Kênh Hỗ Trợ Kỹ Thuật &amp; SLA — Developer Support</h2>
        <div class="subtitle" data-vi="Đội ngũ kỹ sư hỗ trợ tích hợp 24/7 của Hồng Ngọc Hà Travel" data-en="Dedicated 24/7 integration engineering team by Hong Ngoc Ha Travel" data-cn="鸿玉荷旅行社 (Hong Ngoc Ha Travel) 7x24 小时技术保障团队">Đội ngũ kỹ sư hỗ trợ tích hợp 24/7 của Hồng Ngọc Hà Travel</div>
      </div>
    </div>

    <div class="hero-meta-grid" style="grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));">
      <div class="hero-meta-card">
        <div class="label" data-vi="EMAIL KỸ THUẬT API" data-en="API TECHNICAL SUPPORT" data-cn="接口技术支持邮箱">EMAIL KỸ THUẬT API</div>
        <code>api-support@tripota.com.vn</code>
      </div>
      <div class="hero-meta-card">
        <div class="label" data-vi="HOTLINE NGHIỆP VỤ VÉ 24/7" data-en="24/7 TICKETING DESK HOTLINE" data-cn="7x24 客票业务应急热线">HOTLINE NGHIỆP VỤ VÉ 24/7</div>
        <code>+84 (0) 28 3914 9999</code>
      </div>
      <div class="hero-meta-card">
        <div class="label" data-vi="ZALO / TELEGRAM DEV" data-en="DEV CHAT (ZALO / TELEGRAM)" data-cn="开发者通讯群组 (Zalo / TG)">ZALO / TELEGRAM DEV</div>
        <code>@HNH_FlightHub_Support</code>
      </div>
      <div class="hero-meta-card">
        <div class="label" data-vi="CAM KẾT PHẢN HỒI (SLA)" data-en="RESPONSE COMMITMENT (SLA)" data-cn="服务级别保障承诺 (SLA)">CAM KẾT PHẢN HỒI (SLA)</div>
        <code style="word-break: normal; overflow-wrap: break-word;">
          <span class="lang-vi">&lt; 15 phút đối với sự cố xuất vé khẩn cấp</span>
          <span class="lang-en">&lt; 15 minutes for urgent ticketing incidents</span>
          <span class="lang-cn">&lt; 15 分钟极速响应紧急出票异常</span>
        </code>
      </div>
    </div>
  </div>'''

    html = re.sub(r'<!-- SECTION: DEVELOPER SUPPORT.*?</div>\s*</div>\s*</main>', support_new + '\n  </main>', html, count=1, flags=re.DOTALL)

    # 14. Update Footer
    footer_new = '''<footer class="footer">
  <div data-vi="Hong Ngoc Ha Travel (HNH) · Cổng Tích Hợp API B2B · v1.0 · 2026" data-en="Hong Ngoc Ha Travel (HNH) · B2B Aviation Integration Portal · v1.0 · 2026" data-cn="Hong Ngoc Ha Travel (HNH) · B2B 航空分销 API 开发者门户 · v1.0 · 2026">Hong Ngoc Ha Travel (HNH) · Cổng Tích Hợp API B2B · v1.0 · 2026</div>
  <div class="designer-sig">Designed with ♥ by Trung Nguyễn - Platform Expert</div>
</footer>'''
    html = re.sub(r'<footer class="footer">.*?</footer>', footer_new, html, count=1, flags=re.DOTALL)

    # 15. Update CSS with Complete Language Rules
    css_extra = '''
/* MULTI-LANGUAGE DISPLAY RULES */
[data-lang="vi"] .lang-cn, [data-lang="vi"] .lang-en,
[data-lang="vi"] .bi .cn, [data-lang="vi"] .bi .en {
  display: none !important;
}
[data-lang="vi"] .lang-vi, [data-lang="vi"] .bi .vi {
  display: block !important;
}
[data-lang="vi"] span.lang-vi, [data-lang="vi"] .bi span.vi {
  display: inline !important;
}

[data-lang="cn"] .lang-vi, [data-lang="cn"] .lang-en,
[data-lang="cn"] .bi .vi, [data-lang="cn"] .bi .en {
  display: none !important;
}
[data-lang="cn"] .lang-cn, [data-lang="cn"] .bi .cn {
  display: block !important;
}
[data-lang="cn"] span.lang-cn, [data-lang="cn"] .bi span.cn {
  display: inline !important;
}

[data-lang="en"] .lang-vi, [data-lang="en"] .lang-cn,
[data-lang="en"] .bi .vi, [data-lang="en"] .bi .cn {
  display: none !important;
}
[data-lang="en"] .lang-en, [data-lang="en"] .bi .en {
  display: block !important;
}
[data-lang="en"] span.lang-en, [data-lang="en"] .bi span.en {
  display: inline !important;
}

[data-lang="all"] .lang-vi, [data-lang="all"] .lang-cn, [data-lang="all"] .lang-en,
[data-lang="all"] .bi .vi, [data-lang="all"] .bi .cn, [data-lang="all"] .bi .en {
  display: block !important;
}
[data-lang="all"] span.lang-vi, [data-lang="all"] span.lang-cn, [data-lang="all"] span.lang-en,
[data-lang="all"] .bi span.vi, [data-lang="all"] .bi span.cn, [data-lang="all"] .bi span.en {
  display: inline !important;
}
'''
    if 'MULTI-LANGUAGE DISPLAY RULES' not in html:
        html = html.replace('</style>', css_extra + '\n</style>')

    # 16. Update JavaScript applyLanguage(lang)
    js_apply_lang_new = '''function applyLanguage(lang) {
  if (!lang) lang = 'vi';
  document.documentElement.setAttribute('lang', lang);
  document.body.setAttribute('data-lang', lang);
  localStorage.setItem('hnh_lang', lang);

  document.querySelectorAll('.lang-option').forEach(function(opt) {
    if (opt.getAttribute('data-lang') === lang) opt.classList.add('active');
    else opt.classList.remove('active');
  });

  if (lang === 'vi') {
    langCurFlag.textContent = '🇻🇳';
    langCurLabel.textContent = 'Tiếng Việt';
  } else if (lang === 'cn') {
    langCurFlag.textContent = '🇨🇳';
    langCurLabel.textContent = '中文 (CN)';
  } else if (lang === 'en') {
    langCurFlag.textContent = '🇬🇧';
    langCurLabel.textContent = 'English';
  } else {
    langCurFlag.textContent = '🌐';
    langCurLabel.textContent = 'Tất cả / All';
  }

  // Update all elements with data-vi
  document.querySelectorAll('[data-vi]').forEach(function(el) {
    var txt = '';
    if (lang === 'all') {
      var vi = el.getAttribute('data-vi') || '';
      var en = el.getAttribute('data-en') || '';
      txt = vi + (en && en !== vi ? ' / ' + en : '');
    } else {
      txt = el.getAttribute('data-' + lang) || el.getAttribute('data-vi');
    }
    if (txt) {
      el.innerHTML = txt;
    }
  });

  // Update all inputs with placeholders
  document.querySelectorAll('[data-vi-ph]').forEach(function(el) {
    var ph = el.getAttribute('data-' + (lang === 'all' ? 'en' : lang) + '-ph') || el.getAttribute('data-vi-ph');
    if (ph) {
      el.placeholder = ph;
    }
  });
}'''

    html = re.sub(r'function applyLanguage\(lang\)\s*\{.*?\n\}', js_apply_lang_new, html, count=1, flags=re.DOTALL)

    # 17. Write the transformed html to index.html
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Successfully patched index.html! File length:", len(html))

if __name__ == '__main__':
    main()
