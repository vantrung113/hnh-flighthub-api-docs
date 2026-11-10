# -*- coding: utf-8 -*-
"""
apply_premium_upgrade.py
Implements complete /premium-ui-ux-protocol overhaul:
1. Vibrant, iconic brand badges for all System Codes (VN, VJ, QH, VU, 9G, 1A, 1G, 1B/1S, TR, TK, PR, SQ, AK, 9C, TH, SH, FO)
2. Category pills and connection type status badges with glowing indicators
3. Compact single passenger picker popup matching user reference image (media_1794300209477_6719843e.png)
   with strict IATA rules: ADT + CHD <= 9, INF <= ADT, ADT min 1
4. Multi-city (Đa chặng), Round-trip (Khứ hồi), and One-way (Một chiều) cURL playground
5. Fix layout overlap bug (media_1794300132463_573d7735.jpg) via overflow-x constraints and window.scrollTo
6. Fix theme switcher clipping bug (media_1794297697019_098ea3ef.png)
7. Fix SLA box word-breaking bug on 'khẩn cấp' (media_1794294961756_8b20a5ac.png)
8. Strictly preserve user title 'Platform Expert' with muted, subtle signature
"""

import re
import subprocess

def main():
    print("Reading index.html...")
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # ==========================================
    # 1. PREMIUM UI / UX CSS STYLES
    # ==========================================
    premium_css = '''
/* ==========================================================================
   PREMIUM UI/UX PROTOCOL UPGRADE - AIRLINE BRANDING, BADGES & INTERACTION
   ========================================================================== */

/* FIX LAYOUT & PREVENT SIDEBAR OVERLAP BUG */
html, body {
  overflow-x: hidden !important;
  max-width: 100% !important;
  width: 100% !important;
  box-sizing: border-box;
}
*, *::before, *::after {
  box-sizing: border-box;
}
.header {
  width: 100% !important;
  max-width: 100% !important;
  padding: 0 20px !important;
  box-sizing: border-box;
}
.header-controls {
  margin-left: auto;
  display: flex;
  align-items: center;
  gap: 10px;
  flex-shrink: 0;
  padding-right: 4px;
}
.theme-btn {
  white-space: nowrap !important;
  flex-shrink: 0 !important;
}
.layout {
  display: flex;
  padding-top: var(--header-h);
  min-height: 100vh;
  width: 100% !important;
  max-width: 100% !important;
  overflow-x: hidden !important;
  box-sizing: border-box;
}
.main {
  margin-left: var(--sidebar-w);
  flex: 1;
  min-width: 0;
  width: calc(100% - var(--sidebar-w)) !important;
  max-width: calc(100% - var(--sidebar-w)) !important;
  padding: 32px 36px 80px 36px;
  box-sizing: border-box;
  overflow-x: hidden !important;
}
.endpoint {
  width: 100% !important;
  max-width: 100% !important;
  overflow: hidden;
  box-sizing: border-box;
  border-radius: 14px;
  transition: box-shadow 0.25s ease, border-color 0.25s ease;
}
.endpoint:hover {
  border-color: var(--border-bright);
}
.endpoint-body {
  padding: 24px;
  overflow-x: auto;
  max-width: 100%;
}

/* HERO META CARDS (PREMIUM GLOSS & ACCENTS) */
.hero-meta-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(230px, 1fr));
  gap: 14px;
  margin: 20px 0;
}
.hero-meta-card {
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: 14px;
  padding: 16px 18px;
  box-shadow: var(--shadow-sm);
  transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
  position: relative;
  overflow: hidden;
}
.hero-meta-card:hover {
  transform: translateY(-2px);
  box-shadow: var(--shadow-md);
  border-color: var(--border-bright);
}
.hero-meta-card.card-docs { border-left: 4px solid #0284c7; }
.hero-meta-card.card-sandbox { border-left: 4px solid #10b981; }
.hero-meta-card.card-swagger { border-left: 4px solid #8b5cf6; }
.hero-meta-card.card-json { border-left: 4px solid #f59e0b; }
.hero-meta-card.card-sla { border-left: 4px solid #f97316; }

.hero-meta-card .label {
  font-size: 11.5px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  color: var(--text-muted);
  margin-bottom: 6px;
}
.hero-meta-card a {
  color: var(--accent);
  text-decoration: none;
  font-weight: 600;
  font-size: 13px;
  transition: color 0.2s;
}
.hero-meta-card a:hover {
  color: var(--accent-hover);
  text-decoration: underline;
}

/* SLA BOX TEXT - NEVER WRAP MID-WORD */
.sla-badge-text {
  font-size: 13px;
  font-weight: 600;
  color: var(--text-primary);
  line-height: 1.5;
  word-break: normal;
  overflow-wrap: normal;
  white-space: normal;
}

/* ==========================================================================
   SYSTEM CODES - VIBRANT BRAND-COLORED BADGES (PREMIUM PROTOCOL)
   ========================================================================== */
.sys-badge {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-width: 44px;
  padding: 4px 10px;
  border-radius: 8px;
  font-family: 'JetBrains Mono', monospace;
  font-size: 12.5px;
  font-weight: 800;
  letter-spacing: 0.5px;
  line-height: 1.2;
  box-shadow: 0 2px 5px rgba(0,0,0,0.08);
  transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
  text-decoration: none;
  cursor: default;
  white-space: nowrap;
}
.sys-badge:hover {
  transform: translateY(-1px) scale(1.05);
  box-shadow: 0 4px 10px rgba(0,0,0,0.15);
}
.sys-sep {
  color: var(--text-muted);
  font-weight: 400;
  margin: 0 4px;
}

/* Domestic Airlines */
.sys-vn { background: linear-gradient(135deg, #004b87, #002d56); color: #fde047; border: 1px solid #0284c7; }
.sys-vj { background: linear-gradient(135deg, #e11d48, #be123c); color: #ffffff; border: 1px solid #f43f5e; text-shadow: 0 1px 2px rgba(0,0,0,0.25); }
.sys-qh { background: linear-gradient(135deg, #059669, #047857); color: #ffffff; border: 1px solid #10b981; }
.sys-vu { background: linear-gradient(135deg, #0284c7, #0369a1); color: #fef08a; border: 1px solid #38bdf8; }
.sys-9g { background: linear-gradient(135deg, #ea580c, #c2410c); color: #ffffff; border: 1px solid #fb923c; }

/* Global GDS */
.sys-1a { background: linear-gradient(135deg, #2563eb, #1d4ed8); color: #ffffff; border: 1px solid #60a5fa; }
.sys-1g { background: linear-gradient(135deg, #6366f1, #4f46e5); color: #ffffff; border: 1px solid #818cf8; }
.sys-1b, .sys-1s { background: linear-gradient(135deg, #dc2626, #991b1b); color: #ffffff; border: 1px solid #ef4444; }

/* Direct NDC */
.sys-tr { background: linear-gradient(135deg, #facc15, #eab308); color: #111827; border: 1px solid #ca8a04; font-weight: 900; }
.sys-tk { background: linear-gradient(135deg, #b91c1c, #7f1d1d); color: #ffffff; border: 1px solid #dc2626; }
.sys-pr { background: linear-gradient(135deg, #0284c7, #1e3a8a); color: #ffffff; border: 1px solid #38bdf8; }
.sys-sq { background: linear-gradient(135deg, #0f172a, #1e293b); color: #fbbf24; border: 1px solid #f59e0b; }

/* LCC & Aggregators */
.sys-ak { background: linear-gradient(135deg, #ef4444, #dc2626); color: #ffffff; border: 1px solid #f87171; }
.sys-9c { background: linear-gradient(135deg, #16a34a, #15803d); color: #ffffff; border: 1px solid #22c55e; }
.sys-th { background: linear-gradient(135deg, #8b5cf6, #6d28d9); color: #ffffff; border: 1px solid #a78bfa; }
.sys-sh { background: linear-gradient(135deg, #0d9488, #0f766e); color: #ffffff; border: 1px solid #14b8a6; }
.sys-fo { background: linear-gradient(135deg, #d97706, #b45309); color: #ffffff; border: 1px solid #f59e0b; }
.sys-w2 { background: linear-gradient(135deg, #0e7490, #155e75); color: #ffffff; border: 1px solid #06b6d4; }

/* Small inline pill for API doc parameters */
.sys-pill-sm {
  display: inline-block;
  padding: 1px 6px;
  border-radius: 5px;
  font-family: 'JetBrains Mono', monospace;
  font-size: 11px;
  font-weight: 700;
  margin: 1px 3px 1px 0;
}

/* ==========================================================================
   CATEGORY PILLS (COLUMN 1)
   ========================================================================== */
.cat-pill {
  display: inline-block;
  padding: 3px 10px;
  border-radius: 9999px;
  font-size: 11.5px;
  font-weight: 700;
  letter-spacing: 0.3px;
  text-transform: uppercase;
  margin-bottom: 3px;
}
.cat-domestic { background: #e0f2fe; color: #0369a1; border: 1px solid #bae6fd; }
.cat-gds { background: #e0e7ff; color: #4338ca; border: 1px solid #c7d2fe; }
.cat-ndc { background: #dcfce7; color: #15803d; border: 1px solid #bbf7d0; }
.cat-lcc { background: #ffedd5; color: #c2410c; border: 1px solid #fed7aa; }
.cat-hub { background: #f3e8ff; color: #7e22ce; border: 1px solid #e9d5ff; }

[data-theme="dark"] .cat-domestic { background: rgba(3, 105, 161, 0.25); color: #38bdf8; border-color: rgba(56, 189, 248, 0.3); }
[data-theme="dark"] .cat-gds { background: rgba(67, 56, 202, 0.25); color: #818cf8; border-color: rgba(129, 140, 248, 0.3); }
[data-theme="dark"] .cat-ndc { background: rgba(21, 128, 61, 0.25); color: #4ade80; border-color: rgba(74, 222, 128, 0.3); }
[data-theme="dark"] .cat-lcc { background: rgba(194, 65, 12, 0.25); color: #fb923c; border-color: rgba(251, 146, 60, 0.3); }
[data-theme="dark"] .cat-hub { background: rgba(126, 34, 206, 0.25); color: #c084fc; border-color: rgba(192, 132, 252, 0.3); }

/* ==========================================================================
   CONNECTION TYPE BADGES (COLUMN 4)
   ========================================================================== */
.conn-badge {
  display: inline-flex;
  align-items: center;
  gap: 7px;
  padding: 4px 10px;
  border-radius: 6px;
  font-size: 11.5px;
  font-weight: 600;
  line-height: 1.2;
}
.badge-dot {
  width: 7px;
  height: 7px;
  border-radius: 50%;
  display: inline-block;
  flex-shrink: 0;
}
.conn-ndc { background: #ecfdf5; color: #047857; border: 1px solid #a7f3d0; }
.conn-ndc .badge-dot { background: #10b981; box-shadow: 0 0 6px #10b981; }

.conn-gds { background: #eff6ff; color: #1d4ed8; border: 1px solid #bfdbfe; }
.conn-gds .badge-dot { background: #3b82f6; box-shadow: 0 0 6px #3b82f6; }

.conn-navitaire { background: #fff7ed; color: #c2410c; border: 1px solid #ffedd5; }
.conn-navitaire .badge-dot { background: #f97316; }

.conn-altea { background: #eef2ff; color: #4338ca; border: 1px solid #e0e7ff; }
.conn-altea .badge-dot { background: #6366f1; }

.conn-lcc { background: #fef2f2; color: #b91c1c; border: 1px solid #fee2e2; }
.conn-lcc .badge-dot { background: #ef4444; }

.conn-hub { background: #faf5ff; color: #7e22ce; border: 1px solid #f3e8ff; }
.conn-hub .badge-dot { background: #a855f7; }

[data-theme="dark"] .conn-ndc { background: rgba(16, 185, 129, 0.15); color: #6ee7b7; border-color: rgba(16, 185, 129, 0.3); }
[data-theme="dark"] .conn-gds { background: rgba(59, 130, 246, 0.15); color: #93c5fd; border-color: rgba(59, 130, 246, 0.3); }
[data-theme="dark"] .conn-navitaire { background: rgba(249, 115, 22, 0.15); color: #fdba74; border-color: rgba(249, 115, 22, 0.3); }
[data-theme="dark"] .conn-altea { background: rgba(99, 102, 241, 0.15); color: #a5b4fc; border-color: rgba(99, 102, 241, 0.3); }
[data-theme="dark"] .conn-lcc { background: rgba(239, 68, 68, 0.15); color: #fca5a5; border-color: rgba(239, 68, 68, 0.3); }
[data-theme="dark"] .conn-hub { background: rgba(168, 85, 247, 0.15); color: #d8b4fe; border-color: rgba(168, 85, 247, 0.3); }

/* ==========================================================================
   PASSENGER PICKER POPUP (MATCHING REFERENCE IMAGE EXACTLY)
   ========================================================================== */
.pax-dropdown-wrap {
  position: relative;
  width: 100%;
}
.pax-summary-btn {
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 8px;
  background: var(--bg-card-alt);
  border: 1px solid var(--border);
  border-radius: 8px;
  padding: 8px 12px;
  font-size: 13px;
  color: var(--text-primary);
  cursor: pointer;
  transition: all 0.2s;
  font-family: inherit;
  box-sizing: border-box;
  text-align: left;
}
.pax-summary-btn:hover, .pax-summary-btn.open {
  border-color: var(--accent);
  background: var(--bg-card);
}
.pax-summary-content {
  display: flex;
  align-items: center;
  gap: 8px;
  flex: 1;
  min-width: 0;
}
.pax-icon {
  font-size: 14px;
  color: var(--text-muted);
}
#pgPaxSummaryText {
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  font-weight: 600;
  color: var(--text-primary);
}
.pax-popup {
  display: none;
  position: absolute;
  top: calc(100% + 6px);
  left: 0;
  width: 290px;
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: 16px;
  box-shadow: 0 10px 30px -5px rgba(0,0,0,0.18), 0 0 0 1px var(--border);
  padding: 16px;
  z-index: 250;
  box-sizing: border-box;
}
.pax-popup.show {
  display: block;
  animation: paxFadeIn 0.18s cubic-bezier(0.16, 1, 0.3, 1);
}
@keyframes paxFadeIn {
  from { opacity: 0; transform: translateY(-4px); }
  to { opacity: 1; transform: translateY(0); }
}
.pax-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 10px 0;
  border-bottom: 1px solid var(--border);
}
.pax-row:last-of-type {
  border-bottom: none;
}
.pax-title {
  font-size: 14px;
  font-weight: 600;
  color: var(--text-primary);
}
.pax-sub {
  font-size: 12px;
  color: var(--text-muted);
  margin-top: 2px;
}
.pax-stepper {
  display: flex;
  align-items: center;
  gap: 12px;
}
.stepper-btn {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  border: 1.5px solid var(--border-bright);
  background: var(--bg-card-alt);
  color: #2563eb;
  font-size: 18px;
  font-weight: 700;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.15s;
  padding: 0;
  line-height: 1;
}
.stepper-btn:hover:not(:disabled) {
  background: #2563eb;
  color: #fff;
  border-color: #2563eb;
  transform: scale(1.08);
}
.stepper-btn:disabled {
  opacity: 0.3;
  cursor: not-allowed;
  border-color: var(--border);
  color: var(--text-muted);
  background: transparent;
}
.stepper-val {
  font-size: 15px;
  font-weight: 700;
  color: var(--text-primary);
  min-width: 20px;
  text-align: center;
}
.pax-popup-footer {
  margin-top: 10px;
  padding-top: 10px;
  border-top: 1px solid var(--border);
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 10px;
}
.pax-note {
  font-size: 11px;
  color: var(--text-muted);
  line-height: 1.35;
  flex: 1;
}
.pax-done-btn {
  background: var(--accent);
  color: #fff;
  border: none;
  border-radius: 6px;
  padding: 4px 12px;
  font-size: 12px;
  font-weight: 600;
  cursor: pointer;
  transition: background 0.2s;
}
.pax-done-btn:hover {
  background: var(--accent-hover);
}

/* ==========================================================================
   MULTI-CITY ITINERARY BUILDER
   ========================================================================== */
.pg-flight-row {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 12px;
}
.pg-multicity-box {
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: 10px;
  padding: 12px 14px;
  margin-top: 8px;
}
.multicity-title {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 10px;
}
.mc-badge {
  background: #f3e8ff;
  color: #7e22ce;
  border: 1px solid #e9d5ff;
  border-radius: 4px;
  font-size: 11px;
  font-weight: 700;
  padding: 2px 6px;
}
[data-theme="dark"] .mc-badge {
  background: rgba(126, 34, 206, 0.25);
  color: #c084fc;
  border-color: rgba(192, 132, 252, 0.3);
}
.mc-hint {
  font-size: 12px;
  color: var(--text-muted);
}
.multicity-legs {
  display: flex;
  flex-direction: column;
  gap: 8px;
}
.mc-leg-row {
  display: flex;
  align-items: center;
  gap: 8px;
}
.mc-leg-num {
  font-size: 11px;
  font-weight: 700;
  color: var(--text-muted);
  width: 40px;
  flex-shrink: 0;
}
.mc-leg-row .pg-select {
  flex: 1.5;
}
.mc-leg-row .pg-input {
  flex: 1;
}

/* ==========================================================================
   MUTED FOOTER SIGNATURE
   ========================================================================== */
.site-footer .signature {
  font-size: 12px;
  font-weight: 400;
  color: var(--text-muted);
  opacity: 0.65;
  margin-top: 6px;
  letter-spacing: 0.3px;
}
.site-footer .heart {
  color: #ef4444;
  display: inline-block;
  font-size: 12px;
}
'''

    if '/* ==========================================================================\n   PREMIUM UI/UX PROTOCOL UPGRADE' not in html:
        html = html.replace('</style>', premium_css + '\n</style>')
        print("Injected Premium CSS styles successfully!")

    # ==========================================
    # 2. HERO META CARDS IN SECTION 00 INTRO
    # ==========================================
    old_hero_grid = r'<div class="hero-meta-grid">.*?</div>\s*</div>\s*<!-- SECTION: CONTENT SOURCES'
    new_hero_grid = '''<div class="hero-meta-grid">
      <div class="hero-meta-card card-docs">
        <div class="label" data-vi="📘 Tài liệu chi tiết (Docs)" data-en="📘 Detailed Documentation (Docs)" data-cn="📘 详细技术文档 (Docs)">📘 Tài liệu chi tiết (Docs)</div>
        <a href="https://flight-doc.tripota.com.vn/docs/intro/" target="_blank">flight-doc.tripota.com.vn</a>
      </div>
      <div class="hero-meta-card card-sandbox">
        <div class="label" data-vi="🧪 Môi trường Sandbox Test" data-en="🧪 Sandbox Testing Environment" data-cn="🧪 沙箱测试环境 (Sandbox)">🧪 Môi trường Sandbox Test</div>
        <a href="https://sandbox-apihub.tripota.com.vn" target="_blank">sandbox-apihub.tripota.com.vn</a>
      </div>
      <div class="hero-meta-card card-swagger">
        <div class="label" data-vi="🛠️ Swagger UI Dev Console" data-en="🛠️ Swagger UI Dev Console" data-cn="🛠️ Swagger 交互控制台">🛠️ Swagger UI Dev Console</div>
        <a href="https://flight-api-hub-dev.tripota.com.vn/swagger/index.html" target="_blank">Swagger API Console v1.0</a>
      </div>
      <div class="hero-meta-card card-json">
        <div class="label" data-vi="📄 OpenAPI 3.0 Spec JSON" data-en="📄 OpenAPI 3.0 Spec JSON" data-cn="📄 OpenAPI 3.0 规范 JSON">📄 OpenAPI 3.0 Spec JSON</div>
        <a href="https://flight-api-hub-dev.tripota.com.vn/swagger/flight-hub/swagger.json" target="_blank">swagger.json (53 Endpoints)</a>
      </div>
    </div>
  </div>

  <!-- SECTION: CONTENT SOURCES'''
    html = re.sub(old_hero_grid, new_hero_grid, html, count=1, flags=re.DOTALL)

    # ==========================================
    # 3. REVISE SECTION 00 TABLE WITH VIBRANT SYSTEM BADGES & CATEGORY PILLS
    # ==========================================
    old_table_pattern = r'<table class="field-table">\s*<thead>\s*<tr>\s*<th style="width: 25%;"[^>]*>.*?</table>'
    new_table = '''<table class="field-table">
      <thead>
        <tr>
          <th style="width: 22%;" data-vi="Phân nhóm (Category)" data-en="Category" data-cn="系统分类">Phân nhóm (Category)</th>
          <th style="width: 15%; text-align: center;" data-vi="Mã hệ thống (System Code)" data-en="System Code" data-cn="系统代码">Mã hệ thống (System Code)</th>
          <th style="width: 38%;" data-vi="Tên Hãng / Nhà cung cấp" data-en="Airline / Provider Name" data-cn="航司 / 渠道名称">Tên Hãng / Nhà cung cấp</th>
          <th style="width: 25%;" data-vi="Phương thức kết nối" data-en="Connection Type" data-cn="对接类型">Phương thức kết nối</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><span class="cat-pill cat-domestic" data-vi="Domestic Airlines" data-en="Domestic Airlines" data-cn="越南国内航司">Domestic Airlines</span><br><span class="cn">越南国内航司</span></td>
          <td style="text-align: center;"><span class="sys-badge sys-vn" title="Vietnam Airlines (Hãng Hàng Không Quốc Gia VN)">VN</span></td>
          <td>Vietnam Airlines (Hãng Hàng Không Quốc Gia VN)</td>
          <td><span class="conn-badge conn-gds"><span class="badge-dot"></span>Direct Sabre / GDS</span></td>
        </tr>
        <tr>
          <td><span class="cat-pill cat-domestic" data-vi="Domestic Airlines" data-en="Domestic Airlines" data-cn="越南国内航司">Domestic Airlines</span><br><span class="cn">越南国内航司</span></td>
          <td style="text-align: center;"><span class="sys-badge sys-vj" title="Vietjet Air (Công ty CP Hàng không Vietjet)">VJ</span></td>
          <td>Vietjet Air (Công ty CP Hàng không Vietjet)</td>
          <td><span class="conn-badge conn-navitaire"><span class="badge-dot"></span>Navitaire API</span></td>
        </tr>
        <tr>
          <td><span class="cat-pill cat-domestic" data-vi="Domestic Airlines" data-en="Domestic Airlines" data-cn="越南国内航司">Domestic Airlines</span><br><span class="cn">越南国内航司</span></td>
          <td style="text-align: center;"><span class="sys-badge sys-qh" title="Bamboo Airways (Hãng Hàng không Tre Việt)">QH</span></td>
          <td>Bamboo Airways (Hãng Hàng không Tre Việt)</td>
          <td><span class="conn-badge conn-altea"><span class="badge-dot"></span>Amadeus Altea API</span></td>
        </tr>
        <tr>
          <td><span class="cat-pill cat-domestic" data-vi="Domestic Airlines" data-en="Domestic Airlines" data-cn="越南国内航司">Domestic Airlines</span><br><span class="cn">越南国内航司</span></td>
          <td style="text-align: center;"><span class="sys-badge sys-vu" title="Vietravel Airlines (Hàng không Lữ hành VN)">VU</span></td>
          <td>Vietravel Airlines (Hàng không Lữ hành VN)</td>
          <td><span class="conn-badge conn-lcc"><span class="badge-dot"></span>Direct LCC API</span></td>
        </tr>
        <tr>
          <td><span class="cat-pill cat-domestic" data-vi="Domestic Airlines" data-en="Domestic Airlines" data-cn="越南国内航司">Domestic Airlines</span><br><span class="cn">越南国内航司</span></td>
          <td style="text-align: center;"><span class="sys-badge sys-9g" title="Sun Phu Quoc Airways (Chuyến bay Phú Quốc)">9G</span></td>
          <td>Sun Phu Quoc Airways (Chuyến bay Phú Quốc)</td>
          <td><span class="conn-badge conn-hub"><span class="badge-dot"></span>Charter Hub</span></td>
        </tr>
        <tr>
          <td><span class="cat-pill cat-gds" data-vi="Global GDS" data-en="Global GDS" data-cn="全球分销系统">Global GDS</span><br><span class="cn">全球分销系统</span></td>
          <td style="text-align: center;"><span class="sys-badge sys-1a" title="Amadeus Global GDS">1A</span></td>
          <td>Amadeus (GDS Châu Âu / Toàn cầu)</td>
          <td><span class="conn-badge conn-ndc"><span class="badge-dot"></span>NDC &amp; Edifact</span></td>
        </tr>
        <tr>
          <td><span class="cat-pill cat-gds" data-vi="Global GDS" data-en="Global GDS" data-cn="全球分销系统">Global GDS</span><br><span class="cn">全球分销系统</span></td>
          <td style="text-align: center;"><span class="sys-badge sys-1g" title="Travelport Galileo GDS">1G</span></td>
          <td>Travelport / Galileo (GDS Galileo)</td>
          <td><span class="conn-badge conn-gds"><span class="badge-dot"></span>Galileo XML</span></td>
        </tr>
        <tr>
          <td><span class="cat-pill cat-gds" data-vi="Global GDS" data-en="Global GDS" data-cn="全球分销系统">Global GDS</span><br><span class="cn">全球分销系统</span></td>
          <td style="text-align: center;"><span class="sys-badge sys-1b" title="Sabre GDS">1B</span> <span class="sys-sep">/</span> <span class="sys-badge sys-1s" title="Sabre GDS">1S</span></td>
          <td>Sabre / Abacus (GDS Sabre Châu Á)</td>
          <td><span class="conn-badge conn-gds"><span class="badge-dot"></span>Sabre Web Services</span></td>
        </tr>
        <tr>
          <td><span class="cat-pill cat-ndc" data-vi="Direct NDC" data-en="Direct NDC" data-cn="航司直连 NDC">Direct NDC</span><br><span class="cn">航司直连 NDC</span></td>
          <td style="text-align: center;"><span class="sys-badge sys-tr" title="Scoot NDC (Singapore)">TR</span></td>
          <td>Scoot Air NDC (Hãng Scoot Singapore trực tiếp)</td>
          <td><span class="conn-badge conn-ndc"><span class="badge-dot"></span>IATA NDC Direct</span></td>
        </tr>
        <tr>
          <td><span class="cat-pill cat-ndc" data-vi="Direct NDC" data-en="Direct NDC" data-cn="航司直连 NDC">Direct NDC</span><br><span class="cn">航司直连 NDC</span></td>
          <td style="text-align: center;"><span class="sys-badge sys-tk" title="Turkish Airlines NDC">TK</span></td>
          <td>Turkish Airlines (Hãng Hàng không Thổ Nhĩ Kỳ)</td>
          <td><span class="conn-badge conn-ndc"><span class="badge-dot"></span>IATA NDC Direct</span></td>
        </tr>
        <tr>
          <td><span class="cat-pill cat-ndc" data-vi="Direct NDC" data-en="Direct NDC" data-cn="航司直连 NDC">Direct NDC</span><br><span class="cn">航司直连 NDC</span></td>
          <td style="text-align: center;"><span class="sys-badge sys-pr" title="Philippine Airlines NDC">PR</span></td>
          <td>Philippine Airlines (Hãng Hàng không Philippines)</td>
          <td><span class="conn-badge conn-ndc"><span class="badge-dot"></span>IATA NDC Direct</span></td>
        </tr>
        <tr>
          <td><span class="cat-pill cat-ndc" data-vi="Direct NDC" data-en="Direct NDC" data-cn="航司直连 NDC">Direct NDC</span><br><span class="cn">航司直连 NDC</span></td>
          <td style="text-align: center;"><span class="sys-badge sys-sq" title="Singapore Airlines NDC">SQ</span></td>
          <td>Singapore Airlines (Hãng Singapore Airlines)</td>
          <td><span class="conn-badge conn-ndc"><span class="badge-dot"></span>IATA NDC Direct</span></td>
        </tr>
        <tr>
          <td><span class="cat-pill cat-lcc" data-vi="LCC (Low-Cost)" data-en="LCC (Low-Cost)" data-cn="国际低成本航空">LCC (Low-Cost)</span><br><span class="cn">国际低成本航空</span></td>
          <td style="text-align: center;"><span class="sys-badge sys-ak" title="AirAsia LCC">AK</span></td>
          <td>AirAsia (Tập đoàn Hàng không Giá rẻ Châu Á)</td>
          <td><span class="conn-badge conn-navitaire"><span class="badge-dot"></span>Newskies Direct API</span></td>
        </tr>
        <tr>
          <td><span class="cat-pill cat-lcc" data-vi="LCC (Low-Cost)" data-en="LCC (Low-Cost)" data-cn="国际低成本航空">LCC (Low-Cost)</span><br><span class="cn">国际低成本航空</span></td>
          <td style="text-align: center;"><span class="sys-badge sys-9c" title="Spring Airlines (Xuân Thu - TQ)">9C</span></td>
          <td>Spring Airlines (Hãng Hàng không Xuân Thu - TQ)</td>
          <td><span class="conn-badge conn-lcc"><span class="badge-dot"></span>LCC Direct Connect</span></td>
        </tr>
        <tr>
          <td><span class="cat-pill cat-hub" data-vi="Aggregators" data-en="Aggregators" data-cn="专业聚合/批发渠道">Aggregators</span><br><span class="cn">专业聚合/批发渠道</span></td>
          <td style="text-align: center;"><span class="sys-badge sys-th" title="Scoot &amp; Batik Consolidator">TH</span></td>
          <td>Scoot &amp; Batik Consolidator (Tổng hợp Scoot + Batik)</td>
          <td><span class="conn-badge conn-hub"><span class="badge-dot"></span>Specialized Hub</span></td>
        </tr>
        <tr>
          <td><span class="cat-pill cat-hub" data-vi="Aggregators" data-en="Aggregators" data-cn="专业聚合/批发渠道">Aggregators</span><br><span class="cn">专业聚合/批发渠道</span></td>
          <td style="text-align: center;"><span class="sys-badge sys-sh" title="SkyHub Aggregator">SH</span></td>
          <td>SkyHub Aggregator (Kênh vé sỉ SkyHub)</td>
          <td><span class="conn-badge conn-hub"><span class="badge-dot"></span>B2B Consolidator</span></td>
        </tr>
        <tr>
          <td><span class="cat-pill cat-hub" data-vi="Aggregators" data-en="Aggregators" data-cn="专业聚合/批发渠道">Aggregators</span><br><span class="cn">专业聚合/批发渠道</span></td>
          <td style="text-align: center;"><span class="sys-badge sys-fo" title="Flyone Hub">FO</span></td>
          <td>Flyone Hub (Kênh vé liên tuyến Flyone)</td>
          <td><span class="conn-badge conn-hub"><span class="badge-dot"></span>B2B Wholesale</span></td>
        </tr>
      </tbody>
    </table>'''
    html = re.sub(old_table_pattern, new_table, html, count=1, flags=re.DOTALL)
    print("Updated Section 00 table with vibrant badges and category pills!")

    # ==========================================
    # 4. REVISE PLAYGROUND BOX (COMPACT PASSENGER PICKER + MULTI-CITY)
    # ==========================================
    old_pg_box = r'<div class="playground-box">.*?</div>\s*</div>\s*<!-- SECTION: AUTHENTICATION'
    new_pg_box = '''<div class="playground-box">
      <div class="pg-form">
        <!-- TRIP TYPE -->
        <div class="pg-field">
          <label data-vi="LOẠI HÀNH TRÌNH (TRIP TYPE)" data-en="TRIP TYPE" data-cn="航程类型 (TRIP TYPE)">LOẠI HÀNH TRÌNH (TRIP TYPE)</label>
          <select id="pgTripType" class="pg-select">
            <option value="oneway" data-vi="Một chiều (One-Way)" data-en="One-Way" data-cn="单程 (One-Way)">Một chiều (One-Way)</option>
            <option value="roundtrip" data-vi="Khứ hồi (Round-Trip)" data-en="Round-Trip" data-cn="往返 (Round-Trip)">Khứ hồi (Round-Trip)</option>
            <option value="multicity" data-vi="Đa chặng (Multi-City)" data-en="Multi-City" data-cn="多段航程 (Multi-City)">Đa chặng (Multi-City)</option>
          </select>
        </div>

        <!-- SYSTEM CODE -->
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

        <!-- COMPACT SINGLE PASSENGER PICKER (MATCHING REFERENCE IMAGE) -->
        <div class="pg-field pax-picker-field">
          <label data-vi="HÀNH KHÁCH" data-en="PASSENGERS" data-cn="乘机人数">HÀNH KHÁCH</label>
          <div class="pax-dropdown-wrap">
            <button type="button" class="pax-summary-btn" id="pgPaxBtn" aria-haspopup="true" aria-expanded="false">
              <span class="pax-summary-content">
                <span class="pax-icon">👥</span>
                <span id="pgPaxSummaryText">1 Người lớn</span>
              </span>
              <span class="dropdown-chevron">▼</span>
            </button>

            <!-- DROPDOWN POPUP CARD -->
            <div class="pax-popup" id="pgPaxPopup">
              <!-- Row 1: ADT -->
              <div class="pax-row">
                <div class="pax-info">
                  <div class="pax-title" data-vi="Người lớn" data-en="Adults" data-cn="成人">Người lớn</div>
                  <div class="pax-sub" data-vi="Từ 12 tuổi" data-en="Ages 12+" data-cn="12周岁及以上">Từ 12 tuổi</div>
                </div>
                <div class="pax-stepper">
                  <button type="button" class="stepper-btn" id="btnAdtMinus" disabled aria-label="Decrease Adults">−</button>
                  <span class="stepper-val" id="valAdt">1</span>
                  <button type="button" class="stepper-btn" id="btnAdtPlus" aria-label="Increase Adults">+</button>
                </div>
              </div>

              <!-- Row 2: CHD -->
              <div class="pax-row">
                <div class="pax-info">
                  <div class="pax-title" data-vi="Trẻ em" data-en="Children" data-cn="儿童">Trẻ em</div>
                  <div class="pax-sub" data-vi="Từ 2 - dưới 12 tuổi" data-en="Ages 2-11" data-cn="2-11周岁">Từ 2 - dưới 12 tuổi</div>
                </div>
                <div class="pax-stepper">
                  <button type="button" class="stepper-btn" id="btnChdMinus" disabled aria-label="Decrease Children">−</button>
                  <span class="stepper-val" id="valChd">0</span>
                  <button type="button" class="stepper-btn" id="btnChdPlus" aria-label="Increase Children">+</button>
                </div>
              </div>

              <!-- Row 3: INF -->
              <div class="pax-row">
                <div class="pax-info">
                  <div class="pax-title" data-vi="Trẻ sơ sinh" data-en="Infants" data-cn="婴儿">Trẻ sơ sinh</div>
                  <div class="pax-sub" data-vi="Dưới 2 tuổi" data-en="Under 2 yrs" data-cn="未满2周岁 (不占座)">Dưới 2 tuổi</div>
                </div>
                <div class="pax-stepper">
                  <button type="button" class="stepper-btn" id="btnInfMinus" disabled aria-label="Decrease Infants">−</button>
                  <span class="stepper-val" id="valInf">0</span>
                  <button type="button" class="stepper-btn" id="btnInfPlus" aria-label="Increase Infants">+</button>
                </div>
              </div>

              <!-- Rule notice footer -->
              <div class="pax-popup-footer">
                <div class="pax-note" data-vi="Tối đa 9 khách có ghế (ADT + CHD). Em bé ≤ Người lớn." data-en="Max 9 seated passengers (ADT + CHD). Infants ≤ Adults." data-cn="最多9名占座旅客 (ADT + CHD)。婴儿数 ≤ 成人数。">Tối đa 9 khách có ghế (ADT + CHD). Em bé ≤ Người lớn.</div>
                <button type="button" class="pax-done-btn" id="btnPaxDone" data-vi="Xong" data-en="Done" data-cn="完成">Xong</button>
              </div>
            </div>
          </div>
        </div>

        <!-- STANDARD FLIGHT ROW (ONE-WAY & ROUND-TRIP) -->
        <div id="pgStandardFlights" class="pg-flight-row">
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
            <label data-vi="NGÀY ĐI (DEPART DATE)" data-en="DEPARTURE DATE" data-cn="出发日期 (DEPART DATE)">NGÀY ĐI (DEPART DATE)</label>
            <input type="date" id="pgDate" class="pg-input">
          </div>

          <div class="pg-field" id="pgReturnGroup" style="display: none;">
            <label data-vi="NGÀY VỀ (RETURN DATE)" data-en="RETURN DATE" data-cn="返回日期 (RETURN DATE)">NGÀY VỀ (RETURN DATE)</label>
            <input type="date" id="pgReturnDate" class="pg-input">
          </div>
        </div>

        <!-- MULTI-CITY FLIGHT BUILDER (ĐA CHẶNG) -->
        <div id="pgMultiCityGroup" class="pg-multicity-box" style="display: none;">
          <div class="multicity-title">
            <span class="mc-badge" data-vi="ĐA CHẶNG BAY" data-en="MULTI-CITY ITINERARY" data-cn="多段航程">ĐA CHẶNG BAY</span>
            <span class="mc-hint" data-vi="Hành trình đa điểm dừng (Sequential Legs 0, 1, 2)" data-en="Multi-segment flight criteria (Sequential Legs 0, 1, 2)" data-cn="多段中转联程航段配置 (Sequential Legs 0, 1, 2)">Hành trình đa điểm dừng (Sequential Legs 0, 1, 2)</span>
          </div>
          <div class="multicity-legs">
            <div class="mc-leg-row">
              <span class="mc-leg-num">Leg 0</span>
              <select id="mcRoute0" class="pg-select">
                <option value="SGN-HAN" selected>SGN → HAN (TP.HCM - Hà Nội)</option>
                <option value="HAN-DAD">HAN → DAD (Hà Nội - Đà Nẵng)</option>
                <option value="SGN-DAD">SGN → DAD (TP.HCM - Đà Nẵng)</option>
                <option value="SGN-SIN">SGN → SIN (TP.HCM - Singapore)</option>
                <option value="SIN-BKK">SIN → BKK (Singapore - Bangkok)</option>
              </select>
              <input type="date" id="mcDate0" class="pg-input">
            </div>
            <div class="mc-leg-row">
              <span class="mc-leg-num">Leg 1</span>
              <select id="mcRoute1" class="pg-select">
                <option value="HAN-DAD" selected>HAN → DAD (Hà Nội - Đà Nẵng)</option>
                <option value="HAN-SGN">HAN → SGN (Hà Nội - TP.HCM)</option>
                <option value="DAD-SGN">DAD → SGN (Đà Nẵng - TP.HCM)</option>
                <option value="SIN-BKK">SIN → BKK (Singapore - Bangkok)</option>
                <option value="BKK-SGN">BKK → SGN (Bangkok - TP.HCM)</option>
              </select>
              <input type="date" id="mcDate1" class="pg-input">
            </div>
            <div class="mc-leg-row">
              <span class="mc-leg-num">Leg 2</span>
              <select id="mcRoute2" class="pg-select">
                <option value="DAD-SGN" selected>DAD → SGN (Đà Nẵng - TP.HCM)</option>
                <option value="DAD-HAN">DAD → HAN (Đà Nẵng - Hà Nội)</option>
                <option value="BKK-SGN">BKK → SGN (Bangkok - TP.HCM)</option>
                <option value="PQC-SGN">PQC → SGN (Phú Quốc - TP.HCM)</option>
              </select>
              <input type="date" id="mcDate2" class="pg-input">
            </div>
          </div>
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
    html = re.sub(old_pg_box, new_pg_box, html, count=1, flags=re.DOTALL)
    print("Updated Playground box with compact passenger picker & multi-city!")

    # ==========================================
    # 5. FIX SECTION 13 SLA TEXT (PREVENT MID-WORD BREAK)
    # ==========================================
    old_sla = r'<div class="label" data-vi="⚡ Cam Kết Phản Hồi \(SLA\)"[^>]*>.*?</div>\s*<code[^>]*>.*?</code>'
    new_sla = '''<div class="label" data-vi="⚡ Cam Kết Phản Hồi (SLA)" data-en="⚡ Response Commitment (SLA)" data-cn="⚡ 服务级别保障承诺 (SLA)">⚡ Cam Kết Phản Hồi (SLA)</div>
        <div class="sla-badge-text">
          <span class="lang-vi">&lt; 15 phút đối với sự cố xuất vé khẩn&nbsp;cấp</span>
          <span class="lang-en">&lt; 15 minutes for urgent ticketing incidents</span>
          <span class="lang-cn">&lt; 15 分钟极速响应紧急出票异常</span>
        </div>'''
    html = re.sub(old_sla, new_sla, html, count=1, flags=re.DOTALL)
    print("Fixed SLA box word-breaking bug!")

    # ==========================================
    # 6. FIX FOOTER SIGNATURE TO STRICT PROTOCOL WITH MUTED STYLING
    # ==========================================
    old_footer_sig = r'<p class="signature">.*?</p>'
    new_footer_sig = '<p class="signature">Designed with <span class="heart">♥</span> by Trung Nguyễn - Platform Expert</p>'
    html = re.sub(old_footer_sig, new_footer_sig, html, count=1, flags=re.DOTALL)
    print("Ensured signature strictly reads 'Designed with ♥ by Trung Nguyễn - Platform Expert'!")

    # ==========================================
    # 7. FIX NAV CLICK HANDLER (ELIMINATE HORIZONTAL SCROLL OVERLAP)
    # ==========================================
    nav_click_old = r'// 6\. SIDEBAR NAV CLICK SCROLL.*?// 7\.'
    nav_click_new = '''// 6. SIDEBAR NAV CLICK SCROLL (PREVENTS HORIZONTAL SCROLL UNDER SIDEBAR)
document.querySelectorAll('.nav-link[data-target]').forEach(function(link) {
  link.addEventListener('click', function(e) {
    e.preventDefault();
    var id = this.getAttribute('data-target');
    var el = document.getElementById(id);
    if (el) {
      if (el.classList.contains('endpoint')) {
        var body = el.querySelector('.endpoint-body');
        var toggle = el.querySelector('.ep-toggle');
        if (body && body.classList.contains('collapsed')) {
          body.classList.remove('collapsed');
          if (toggle) toggle.classList.add('open');
        }
      }
      var headerH = 76;
      var rect = el.getBoundingClientRect();
      var targetY = rect.top + (window.pageYOffset || document.documentElement.scrollTop) - headerH;
      window.scrollTo({
        top: targetY,
        left: 0,
        behavior: 'smooth'
      });
      document.querySelectorAll('.nav-link').forEach(function(l) { l.classList.remove('active'); });
      this.classList.add('active');
    }
  });
});

// Guard against unwanted horizontal window scroll
window.addEventListener('scroll', function() {
  if (window.scrollX !== 0) {
    window.scrollTo(0, window.scrollY);
  }
});

// 7.'''
    html = re.sub(nav_click_old, nav_click_new, html, count=1, flags=re.DOTALL)

    # ==========================================
    # 8. UPDATE SECTION 7 JS: IATA PAX STEPPERS + MULTI-CITY LOGIC
    # ==========================================
    js_section7_new = r'''// 7. SANDBOX CURL PLAYGROUND GENERATOR (IATA PAX RULES + ONE-WAY / ROUND-TRIP / MULTI-CITY)
var paxState = { adt: 1, chd: 0, inf: 0 };

function initDynamicDates() {
  var today = new Date();
  
  function addDays(d, days) {
    var res = new Date(d);
    res.setDate(res.getDate() + days);
    return res;
  }

  function formatDate(d) {
    var yyyy = d.getFullYear();
    var mm = String(d.getMonth() + 1).padStart(2, '0');
    var dd = String(d.getDate()).padStart(2, '0');
    return yyyy + '-' + mm + '-' + dd;
  }

  var minStr = formatDate(today);
  var d0Str = formatDate(addDays(today, 7));
  var d1Str = formatDate(addDays(today, 10));
  var d2Str = formatDate(addDays(today, 14));

  var dInput = document.getElementById('pgDate');
  var rInput = document.getElementById('pgReturnDate');
  if (dInput) { dInput.value = d0Str; dInput.min = minStr; }
  if (rInput) { rInput.value = d1Str; rInput.min = d0Str; }

  var mc0 = document.getElementById('mcDate0');
  var mc1 = document.getElementById('mcDate1');
  var mc2 = document.getElementById('mcDate2');
  if (mc0) { mc0.value = d0Str; mc0.min = minStr; }
  if (mc1) { mc1.value = d1Str; mc1.min = d0Str; }
  if (mc2) { mc2.value = d2Str; mc2.min = d1Str; }
}
initDynamicDates();

function updatePaxUI() {
  // Strict Aviation Rules:
  // 1. adt + chd <= 9 (Max 9 seated passengers)
  // 2. inf <= adt (Lap infants cannot exceed adult count)
  // 3. adt >= 1
  var totalSeats = paxState.adt + paxState.chd;

  var bAdtMinus = document.getElementById('btnAdtMinus');
  var bAdtPlus = document.getElementById('btnAdtPlus');
  var bChdMinus = document.getElementById('btnChdMinus');
  var bChdPlus = document.getElementById('btnChdPlus');
  var bInfMinus = document.getElementById('btnInfMinus');
  var bInfPlus = document.getElementById('btnInfPlus');

  if (bAdtMinus) bAdtMinus.disabled = (paxState.adt <= 1);
  if (bAdtPlus) bAdtPlus.disabled = (totalSeats >= 9);

  if (bChdMinus) bChdMinus.disabled = (paxState.chd <= 0);
  if (bChdPlus) bChdPlus.disabled = (totalSeats >= 9);

  if (bInfMinus) bInfMinus.disabled = (paxState.inf <= 0);
  if (bInfPlus) bInfPlus.disabled = (paxState.inf >= paxState.adt);

  var vAdt = document.getElementById('valAdt');
  var vChd = document.getElementById('valChd');
  var vInf = document.getElementById('valInf');
  if (vAdt) vAdt.textContent = paxState.adt;
  if (vChd) vChd.textContent = paxState.chd;
  if (vInf) vInf.textContent = paxState.inf;

  var lang = document.documentElement.getAttribute('lang') || 'vi';
  var parts = [];
  if (lang === 'cn') {
    parts.push(paxState.adt + ' 成人');
    if (paxState.chd > 0) parts.push(paxState.chd + ' 儿童');
    if (paxState.inf > 0) parts.push(paxState.inf + ' 婴儿');
  } else if (lang === 'en') {
    parts.push(paxState.adt + ' Adult' + (paxState.adt > 1 ? 's' : ''));
    if (paxState.chd > 0) parts.push(paxState.chd + ' Child' + (paxState.chd > 1 ? 'ren' : ''));
    if (paxState.inf > 0) parts.push(paxState.inf + ' Infant' + (paxState.inf > 1 ? 's' : ''));
  } else {
    parts.push(paxState.adt + ' Người lớn');
    if (paxState.chd > 0) parts.push(paxState.chd + ' Trẻ em');
    if (paxState.inf > 0) parts.push(paxState.inf + ' Em bé');
  }
  var summaryTextEl = document.getElementById('pgPaxSummaryText');
  if (summaryTextEl) summaryTextEl.textContent = parts.join(', ');

  updateSandboxCurl();
}

function initPaxEvents() {
  var bAdtPlus = document.getElementById('btnAdtPlus');
  var bAdtMinus = document.getElementById('btnAdtMinus');
  var bChdPlus = document.getElementById('btnChdPlus');
  var bChdMinus = document.getElementById('btnChdMinus');
  var bInfPlus = document.getElementById('btnInfPlus');
  var bInfMinus = document.getElementById('btnInfMinus');

  if (bAdtPlus) {
    bAdtPlus.addEventListener('click', function(e) {
      e.stopPropagation();
      if (paxState.adt + paxState.chd < 9) {
        paxState.adt++;
        updatePaxUI();
      }
    });
  }
  if (bAdtMinus) {
    bAdtMinus.addEventListener('click', function(e) {
      e.stopPropagation();
      if (paxState.adt > 1) {
        paxState.adt--;
        if (paxState.inf > paxState.adt) paxState.inf = paxState.adt;
        updatePaxUI();
      }
    });
  }
  if (bChdPlus) {
    bChdPlus.addEventListener('click', function(e) {
      e.stopPropagation();
      if (paxState.adt + paxState.chd < 9) {
        paxState.chd++;
        updatePaxUI();
      }
    });
  }
  if (bChdMinus) {
    bChdMinus.addEventListener('click', function(e) {
      e.stopPropagation();
      if (paxState.chd > 0) {
        paxState.chd--;
        updatePaxUI();
      }
    });
  }
  if (bInfPlus) {
    bInfPlus.addEventListener('click', function(e) {
      e.stopPropagation();
      if (paxState.inf < paxState.adt) {
        paxState.inf++;
        updatePaxUI();
      }
    });
  }
  if (bInfMinus) {
    bInfMinus.addEventListener('click', function(e) {
      e.stopPropagation();
      if (paxState.inf > 0) {
        paxState.inf--;
        updatePaxUI();
      }
    });
  }

  var paxBtn = document.getElementById('pgPaxBtn');
  var paxPopup = document.getElementById('pgPaxPopup');
  if (paxBtn && paxPopup) {
    paxBtn.addEventListener('click', function(e) {
      e.stopPropagation();
      paxPopup.classList.toggle('show');
      paxBtn.classList.toggle('open');
    });
    var btnDone = document.getElementById('btnPaxDone');
    if (btnDone) {
      btnDone.addEventListener('click', function(e) {
        e.stopPropagation();
        paxPopup.classList.remove('show');
        paxBtn.classList.remove('open');
      });
    }
    document.addEventListener('click', function(e) {
      if (!paxBtn.contains(e.target) && !paxPopup.contains(e.target)) {
        paxPopup.classList.remove('show');
        paxBtn.classList.remove('open');
      }
    });
  }
}
initPaxEvents();

function updateSandboxCurl() {
  var tripTypeEl = document.getElementById('pgTripType');
  var tripType = tripTypeEl ? tripTypeEl.value : 'oneway';

  var stdBox = document.getElementById('pgStandardFlights');
  var retGroup = document.getElementById('pgReturnGroup');
  var mcBox = document.getElementById('pgMultiCityGroup');

  if (tripType === 'oneway') {
    if (stdBox) stdBox.style.display = 'grid';
    if (retGroup) retGroup.style.display = 'none';
    if (mcBox) mcBox.style.display = 'none';
  } else if (tripType === 'roundtrip') {
    if (stdBox) stdBox.style.display = 'grid';
    if (retGroup) retGroup.style.display = 'flex';
    if (mcBox) mcBox.style.display = 'none';
  } else if (tripType === 'multicity') {
    if (stdBox) stdBox.style.display = 'none';
    if (mcBox) mcBox.style.display = 'block';
  }

  var systemEl = document.getElementById('pgSystem');
  var system = systemEl ? systemEl.value : 'VN';

  var flights = [];

  if (tripType === 'multicity') {
    var r0 = (document.getElementById('mcRoute0') ? document.getElementById('mcRoute0').value : 'SGN-HAN').split('-');
    var d0 = document.getElementById('mcDate0') ? document.getElementById('mcDate0').value : '';
    var r1 = (document.getElementById('mcRoute1') ? document.getElementById('mcRoute1').value : 'HAN-DAD').split('-');
    var d1 = document.getElementById('mcDate1') ? document.getElementById('mcDate1').value : '';
    var r2 = (document.getElementById('mcRoute2') ? document.getElementById('mcRoute2').value : 'DAD-SGN').split('-');
    var d2 = document.getElementById('mcDate2') ? document.getElementById('mcDate2').value : '';

    var mc1El = document.getElementById('mcDate1');
    if (mc1El && d0) {
      mc1El.min = d0;
      if (d1 && d1 < d0) { mc1El.value = d0; d1 = d0; }
    }
    var mc2El = document.getElementById('mcDate2');
    if (mc2El && d1) {
      mc2El.min = d1;
      if (d2 && d2 < d1) { mc2El.value = d1; d2 = d1; }
    }

    flights.push({ leg: 0, startPoint: r0[0], endPoint: r0[1], departDate: d0 });
    flights.push({ leg: 1, startPoint: r1[0], endPoint: r1[1], departDate: d1 || d0 });
    flights.push({ leg: 2, startPoint: r2[0], endPoint: r2[1], departDate: d2 || d1 || d0 });
  } else {
    var routeEl = document.getElementById('pgRoute');
    var route = (routeEl ? routeEl.value : 'SGN-HAN').split('-');
    var dInput = document.getElementById('pgDate');
    var departDate = dInput ? dInput.value : '';
    var rInput = document.getElementById('pgReturnDate');
    var returnDate = rInput ? rInput.value : '';

    if (rInput && departDate) {
      rInput.min = departDate;
      if (returnDate && returnDate < departDate) {
        rInput.value = departDate;
        returnDate = departDate;
      }
    }

    flights.push({ leg: 0, startPoint: route[0], endPoint: route[1], departDate: departDate });
    if (tripType === 'roundtrip') {
      flights.push({ leg: 1, startPoint: route[1], endPoint: route[0], departDate: returnDate || departDate });
    }
  }

  var payload = {
    system: system,
    adt: paxState.adt,
    chd: paxState.chd,
    inf: paxState.inf,
    flights: flights
  };

  var payloadJson = JSON.stringify(payload, null, 2);
  var curlLines = [
    'curl -X POST "https://sandbox-apihub.tripota.com.vn/api/v1/flight/search" \\',
    '  -H "Content-Type: application/json" \\',
    '  -H "Authorization: Bearer YOUR_SANDBOX_TOKEN" \\',
    '  -d \'' + payloadJson + '\''
  ];

  var outEl = document.getElementById('pgCurlOutput');
  if (outEl) {
    outEl.textContent = curlLines.join('\n');
  }
}

['pgTripType', 'pgSystem', 'pgRoute', 'pgDate', 'pgReturnDate', 'mcRoute0', 'mcDate0', 'mcRoute1', 'mcDate1', 'mcRoute2', 'mcDate2'].forEach(function(id) {
  var el = document.getElementById(id);
  if (el) {
    el.addEventListener('change', updateSandboxCurl);
    el.addEventListener('input', updateSandboxCurl);
  }
});
updatePaxUI();

// 8.'''

    s_marker = "// 7. SANDBOX CURL PLAYGROUND GENERATOR"
    e_marker = "// 8."
    s_idx = html.find(s_marker)
    e_idx = html.find(e_marker, s_idx)
    if s_idx != -1 and e_idx != -1:
        html = html[:s_idx] + js_section7_new + "\n\n" + html[e_idx:]
        print("Replaced Section 7 JS cleanly via slice!")
    else:
        print("Warning: Section 7 JS markers not found:", s_idx, e_idx)

    # ==========================================
    # 9. HOOK updatePaxUI() INTO applyLanguage()
    # ==========================================
    if 'if (typeof updatePaxUI === "function") updatePaxUI();' not in html:
        html = html.replace('el.placeholder = ph;\n    }\n  });\n}',
                            'el.placeholder = ph;\n    }\n  });\n  if (typeof updatePaxUI === "function") updatePaxUI();\n}')
        print("Hooked updatePaxUI() into applyLanguage()!")

    # Write output
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Done writing index.html! File size:", len(html))

if __name__ == '__main__':
    main()
