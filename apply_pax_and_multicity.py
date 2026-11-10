# -*- coding: utf-8 -*-
"""
apply_pax_and_multicity.py
Implements:
1. Passenger Selection: 3 independent controls for ADT, CHD, INF (no hardcoded bundles).
2. Journey Types: Một chiều (One-Way), Khứ hồi (Round-Trip), and Đa chặng (Multi-City).
3. Multi-segment flights builder for Multi-City generating sequential legs (0, 1, 2).
4. Strictly preserves user title: "Platform Expert" in subtle, muted footer signature.
"""

import re

def update_portal():
    print("Reading index.html...")
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. UPDATE CSS for Multicity and Clean Form Layout
    extra_css = '''
/* MULTI-CITY & EXPANDED PLAYGROUND CSS */
.pg-flight-row {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 14px;
  grid-column: 1 / -1;
}
.pg-multicity-box {
  grid-column: 1 / -1;
  background: var(--bg-card-alt);
  border: 1px dashed var(--border-bright);
  border-radius: 12px;
  padding: 16px;
  margin-top: 4px;
}
.multicity-title {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-bottom: 12px;
}
.mc-badge {
  background: var(--accent-dim);
  color: var(--accent);
  border: 1px solid var(--accent-border);
  font-size: 11px;
  font-weight: 700;
  padding: 3px 8px;
  border-radius: 6px;
  letter-spacing: 0.5px;
}
.mc-hint {
  font-size: 12px;
  color: var(--text-muted);
}
.multicity-legs {
  display: flex;
  flex-direction: column;
  gap: 10px;
}
.mc-leg-row {
  display: flex;
  align-items: center;
  gap: 10px;
  flex-wrap: wrap;
}
.mc-leg-num {
  font-size: 12px;
  font-weight: 600;
  color: var(--text-primary);
  min-width: 52px;
  background: var(--bg-card);
  border: 1px solid var(--border);
  padding: 6px 10px;
  border-radius: 8px;
  text-align: center;
}
.mc-leg-row select {
  flex: 2;
  min-width: 200px;
}
.mc-leg-row input {
  flex: 1;
  min-width: 140px;
}
'''
    if 'MULTI-CITY & EXPANDED PLAYGROUND CSS' not in html:
        html = html.replace('</style>', extra_css + '\n</style>')

    # 2. UPDATE PLAYGROUND BOX HTML (3 Pax Controls + 3 Trip Types: One-way, Round-trip, Multi-City)
    pg_box_old = r'<div class="playground-box">.*?</div>\s*</div>\s*<!-- SECTION: AUTHENTICATION'
    pg_box_new = '''<div class="playground-box">
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

        <!-- PASSENGERS: ADT (Adults) -->
        <div class="pg-field">
          <label data-vi="NGƯỜI LỚN (ADT ≥12T)" data-en="ADULTS (ADT ≥12Y)" data-cn="成人 (ADT ≥12岁)">NGƯỜI LỚN (ADT ≥12T)</label>
          <select id="pgAdt" class="pg-select">
            <option value="1" selected data-vi="1 Người lớn (1 ADT)" data-en="1 Adult (1 ADT)" data-cn="1 位成人 (1 ADT)">1 Người lớn (1 ADT)</option>
            <option value="2" data-vi="2 Người lớn (2 ADT)" data-en="2 Adults (2 ADT)" data-cn="2 位成人 (2 ADT)">2 Người lớn (2 ADT)</option>
            <option value="3" data-vi="3 Người lớn (3 ADT)" data-en="3 Adults (3 ADT)" data-cn="3 位成人 (3 ADT)">3 Người lớn (3 ADT)</option>
            <option value="4" data-vi="4 Người lớn (4 ADT)" data-en="4 Adults (4 ADT)" data-cn="4 位成人 (4 ADT)">4 Người lớn (4 ADT)</option>
            <option value="5" data-vi="5 Người lớn (5 ADT)" data-en="5 Adults (5 ADT)" data-cn="5 位成人 (5 ADT)">5 Người lớn (5 ADT)</option>
            <option value="6" data-vi="6 Người lớn (6 ADT)" data-en="6 Adults (6 ADT)" data-cn="6 位成人 (6 ADT)">6 Người lớn (6 ADT)</option>
            <option value="7" data-vi="7 Người lớn (7 ADT)" data-en="7 Adults (7 ADT)" data-cn="7 位成人 (7 ADT)">7 Người lớn (7 ADT)</option>
            <option value="8" data-vi="8 Người lớn (8 ADT)" data-en="8 Adults (8 ADT)" data-cn="8 位成人 (8 ADT)">8 Người lớn (8 ADT)</option>
            <option value="9" data-vi="9 Người lớn (9 ADT)" data-en="9 Adults (9 ADT)" data-cn="9 位成人 (9 ADT)">9 Người lớn (9 ADT)</option>
          </select>
        </div>

        <!-- PASSENGERS: CHD (Children) -->
        <div class="pg-field">
          <label data-vi="TRẺ EM (CHD 2-11T)" data-en="CHILDREN (CHD 2-11Y)" data-cn="儿童 (CHD 2-11岁)">TRẺ EM (CHD 2-11T)</label>
          <select id="pgChd" class="pg-select">
            <option value="0" selected data-vi="0 Trẻ em (0 CHD)" data-en="0 Children (0 CHD)" data-cn="0 儿童 (0 CHD)">0 Trẻ em (0 CHD)</option>
            <option value="1" data-vi="1 Trẻ em (1 CHD)" data-en="1 Child (1 CHD)" data-cn="1 位儿童 (1 CHD)">1 Trẻ em (1 CHD)</option>
            <option value="2" data-vi="2 Trẻ em (2 CHD)" data-en="2 Children (2 CHD)" data-cn="2 位儿童 (2 CHD)">2 Trẻ em (2 CHD)</option>
            <option value="3" data-vi="3 Trẻ em (3 CHD)" data-en="3 Children (3 CHD)" data-cn="3 位儿童 (3 CHD)">3 Trẻ em (3 CHD)</option>
            <option value="4" data-vi="4 Trẻ em (4 CHD)" data-en="4 Children (4 CHD)" data-cn="4 位儿童 (4 CHD)">4 Trẻ em (4 CHD)</option>
            <option value="5" data-vi="5 Trẻ em (5 CHD)" data-en="5 Children (5 CHD)" data-cn="5 位儿童 (5 CHD)">5 Trẻ em (5 CHD)</option>
            <option value="6" data-vi="6 Trẻ em (6 CHD)" data-en="6 Children (6 CHD)" data-cn="6 位儿童 (6 CHD)">6 Trẻ em (6 CHD)</option>
            <option value="7" data-vi="7 Trẻ em (7 CHD)" data-en="7 Children (7 CHD)" data-cn="7 位儿童 (7 CHD)">7 Trẻ em (7 CHD)</option>
            <option value="8" data-vi="8 Trẻ em (8 CHD)" data-en="8 Children (8 CHD)" data-cn="8 位儿童 (8 CHD)">8 Trẻ em (8 CHD)</option>
          </select>
        </div>

        <!-- PASSENGERS: INF (Infants) -->
        <div class="pg-field">
          <label data-vi="EM BÉ (INF <2T)" data-en="INFANTS (INF <2Y)" data-cn="婴儿 (INF <2岁)">EM BÉ (INF <2T)</label>
          <select id="pgInf" class="pg-select">
            <option value="0" selected data-vi="0 Em bé (0 INF)" data-en="0 Infants (0 INF)" data-cn="0 婴儿 (0 INF)">0 Em bé (0 INF)</option>
            <option value="1" data-vi="1 Em bé (1 INF)" data-en="1 Infant (1 INF)" data-cn="1 位婴儿 (1 INF)">1 Em bé (1 INF)</option>
            <option value="2" data-vi="2 Em bé (2 INF)" data-en="2 Infants (2 INF)" data-cn="2 位婴儿 (2 INF)">2 Em bé (2 INF)</option>
            <option value="3" data-vi="3 Em bé (3 INF)" data-en="3 Infants (3 INF)" data-cn="3 位婴儿 (3 INF)">3 Em bé (3 INF)</option>
            <option value="4" data-vi="4 Em bé (4 INF)" data-en="4 Infants (4 INF)" data-cn="4 位婴儿 (4 INF)">4 Em bé (4 INF)</option>
          </select>
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
    html = re.sub(pg_box_old, pg_box_new, html, count=1, flags=re.DOTALL)

    # 3. UPDATE FOOTER: KEEP STRICT TITLE "Platform Expert"
    footer_old = r'<footer class="site-footer">.*?</footer>'
    footer_new = '''<footer class="site-footer">
    <p class="footer-copy" data-vi="Hong Ngoc Ha Travel (HNH) &nbsp;·&nbsp; Cổng Tích Hợp API B2B &nbsp;·&nbsp; v1.0 &nbsp;·&nbsp; 2026" data-en="Hong Ngoc Ha Travel (HNH) &nbsp;·&nbsp; B2B Aviation Integration Portal &nbsp;·&nbsp; v1.0 &nbsp;·&nbsp; 2026" data-cn="Hong Ngoc Ha Travel (HNH) &nbsp;·&nbsp; B2B 航空分销 API 开发者门户 &nbsp;·&nbsp; v1.0 &nbsp;·&nbsp; 2026">Hong Ngoc Ha Travel (HNH) &nbsp;·&nbsp; B2B Aviation Integration Portal &nbsp;·&nbsp; v1.0 &nbsp;·&nbsp; 2026</p>
    <p class="signature">Crafted with <span class="heart">♥</span> by Trung Nguyễn · Platform Expert</p>
  </footer>'''
    html = re.sub(footer_old, footer_new, html, count=1, flags=re.DOTALL)

    # 4. UPDATE JAVASCRIPT: LOGIC FOR ADT, CHD, INF & ONE-WAY, ROUND-TRIP, MULTI-CITY
    js_section7_old = r'// 7\. SANDBOX CURL PLAYGROUND GENERATOR.*?// 8\.'
    js_section7_new = '''// 7. SANDBOX CURL PLAYGROUND GENERATOR (ONE-WAY, ROUND-TRIP, MULTI-CITY & FLEXIBLE PAX)
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

  var adtEl = document.getElementById('pgAdt');
  var chdEl = document.getElementById('pgChd');
  var infEl = document.getElementById('pgInf');

  var adt = parseInt(adtEl ? adtEl.value : 1) || 1;
  var chd = parseInt(chdEl ? chdEl.value : 0) || 0;
  var inf = parseInt(infEl ? infEl.value : 0) || 0;

  // IATA Rule: inf <= adt
  if (inf > adt && infEl) {
    inf = adt;
    infEl.value = String(adt);
  }

  var flights = [];

  if (tripType === 'multicity') {
    var r0 = (document.getElementById('mcRoute0') ? document.getElementById('mcRoute0').value : 'SGN-HAN').split('-');
    var d0 = document.getElementById('mcDate0') ? document.getElementById('mcDate0').value : '';
    var r1 = (document.getElementById('mcRoute1') ? document.getElementById('mcRoute1').value : 'HAN-DAD').split('-');
    var d1 = document.getElementById('mcDate1') ? document.getElementById('mcDate1').value : '';
    var r2 = (document.getElementById('mcRoute2') ? document.getElementById('mcRoute2').value : 'DAD-SGN').split('-');
    var d2 = document.getElementById('mcDate2') ? document.getElementById('mcDate2').value : '';

    // Keep dates sequential
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
    adt: adt,
    chd: chd,
    inf: inf,
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

['pgTripType', 'pgSystem', 'pgAdt', 'pgChd', 'pgInf', 'pgRoute', 'pgDate', 'pgReturnDate', 'mcRoute0', 'mcDate0', 'mcRoute1', 'mcDate1', 'mcRoute2', 'mcDate2'].forEach(function(id) {
  var el = document.getElementById(id);
  if (el) {
    el.addEventListener('change', updateSandboxCurl);
    el.addEventListener('input', updateSandboxCurl);
  }
});
updateSandboxCurl();

// 8.'''
    html = re.sub(js_section7_old, js_section7_new, html, count=1, flags=re.DOTALL)

    # 5. Fix any JS string escaping distortion on curlLines
    bad_curl_join = "outEl.textContent = curlLines.join('\n');"
    # Make sure curlLines.join('\n') has a real literal \n in index.html
    html = html.replace("outEl.textContent = curlLines.join('\n');", "outEl.textContent = curlLines.join('\\n');")

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Updates written to index.html successfully! Length:", len(html))

if __name__ == '__main__':
    update_portal()
