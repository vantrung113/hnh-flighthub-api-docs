# -*- coding: utf-8 -*-
"""
elevate_site_visuals.py
Refines site-wide visual contrast and colors per /premium-ui-ux-protocol:
1. Vibrant section-num badges with gradient & soft shadow
2. High-contrast method badges (.method-post in crisp sky/azure, .method-get in emerald)
3. High-contrast required badges (.req-yes in crisp crimson, .req-no in clean slate)
4. Polished callout boxes with solid left border accents
5. Inline mini system badges in parameter tables
6. Table rows subtle hover interaction
"""

import re

def main():
    print("Reading index.html...")
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    extra_css = '''
/* ==========================================================================
   WHOLE-PAGE COLOR & CONTRAST ELEVATION (PREMIUM PROTOCOL)
   ========================================================================== */

/* HIGH-CONTRAST SECTION NUMBERS */
.section-num {
  font-family: 'JetBrains Mono', monospace !important;
  font-size: 13px !important;
  font-weight: 800 !important;
  background: linear-gradient(135deg, #0284c7, #0369a1) !important;
  color: #ffffff !important;
  border: 1px solid #0284c7 !important;
  padding: 4px 10px !important;
  border-radius: 8px !important;
  box-shadow: 0 2px 6px rgba(2, 132, 199, 0.25) !important;
  display: inline-flex !important;
  align-items: center !important;
  justify-content: center !important;
  min-width: 34px !important;
  line-height: 1 !important;
}
[data-theme="dark"] .section-num {
  background: linear-gradient(135deg, #0284c7, #075985) !important;
  color: #ffffff !important;
  border-color: #38bdf8 !important;
  box-shadow: 0 2px 8px rgba(56, 189, 248, 0.2) !important;
}

/* HIGH-CONTRAST METHOD BADGES (POST / GET) */
.method-post {
  background: #e0f2fe !important;
  color: #0284c7 !important;
  border: 1px solid #bae6fd !important;
  font-weight: 800 !important;
}
.method-get {
  background: #dcfce7 !important;
  color: #16a34a !important;
  border: 1px solid #bbf7d0 !important;
  font-weight: 800 !important;
}
[data-theme="dark"] .method-post {
  background: rgba(2, 132, 199, 0.25) !important;
  color: #38bdf8 !important;
  border-color: rgba(56, 189, 248, 0.35) !important;
}
[data-theme="dark"] .method-get {
  background: rgba(22, 163, 74, 0.25) !important;
  color: #4ade80 !important;
  border-color: rgba(74, 222, 128, 0.35) !important;
}

/* HIGH-CONTRAST REQUIRED / OPTIONAL BADGES */
.req-badge {
  font-size: 10.5px !important;
  font-weight: 700 !important;
  padding: 3px 8px !important;
  border-radius: 6px !important;
  letter-spacing: 0.4px !important;
  text-transform: uppercase !important;
  line-height: 1.2 !important;
}
.req-yes {
  background: #fee2e2 !important;
  color: #b91c1c !important;
  border: 1px solid #fecaca !important;
  box-shadow: 0 1px 2px rgba(185, 28, 28, 0.06) !important;
}
.req-no {
  background: #f1f5f9 !important;
  color: #475569 !important;
  border: 1px solid #e2e8f0 !important;
}
[data-theme="dark"] .req-yes {
  background: rgba(239, 68, 68, 0.2) !important;
  color: #fca5a5 !important;
  border-color: rgba(239, 68, 68, 0.35) !important;
}
[data-theme="dark"] .req-no {
  background: rgba(148, 163, 184, 0.12) !important;
  color: #94a3b8 !important;
  border-color: rgba(148, 163, 184, 0.2) !important;
}

/* POLISHED CALLOUT ACCENTS */
.callout-tip {
  border-left: 4px solid #10b981 !important;
}
.callout-warn {
  border-left: 4px solid #f59e0b !important;
}
.callout-info {
  border-left: 4px solid #0284c7 !important;
}

/* SMALL INLINE SYSTEM BADGE */
.sys-badge-sm {
  min-width: 32px !important;
  padding: 1px 6px !important;
  font-size: 11px !important;
  border-radius: 5px !important;
  vertical-align: middle !important;
  margin: 0 1px !important;
}

/* TABLE ROW HOVER */
.field-table tbody tr {
  transition: background-color 0.15s ease;
}
.field-table tbody tr:hover td {
  background-color: var(--bg-card-alt);
}
'''

    if '/* WHOLE-PAGE COLOR & CONTRAST ELEVATION (PREMIUM PROTOCOL) */' not in html:
        html = html.replace('</style>', extra_css + '\n</style>')
        print("Injected whole-page contrast styles!")

    # Replace inline list of systems in parameter table (Section 01 Search Flights)
    old_sys_param = r'\(<code>VN</code>, <code>VJ</code>, <code>QH</code>, <code>VU</code>, <code>1A</code>, <code>TR</code>, <code>AK</code>\)'
    new_sys_param = '(<span class="sys-badge sys-vn sys-badge-sm">VN</span>, <span class="sys-badge sys-vj sys-badge-sm">VJ</span>, <span class="sys-badge sys-qh sys-badge-sm">QH</span>, <span class="sys-badge sys-vu sys-badge-sm">VU</span>, <span class="sys-badge sys-1a sys-badge-sm">1A</span>, <span class="sys-badge sys-tr sys-badge-sm">TR</span>, <span class="sys-badge sys-ak sys-badge-sm">AK</span>)'
    html = re.sub(old_sys_param, new_sys_param, html)

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Done! File size:", len(html))

if __name__ == '__main__':
    main()
