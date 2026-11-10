# -*- coding: utf-8 -*-
"""
verify_i18n.py
Simulates language selection and checks for 100% translation completeness.
"""

from bs4 import BeautifulSoup
import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

print("--- 1. CHECK [data-vi] ELEMENTS ---")
data_vi_elements = soup.find_all(attrs={"data-vi": True})
print(f"Total elements with data-vi: {len(data_vi_elements)}")

missing_cn = []
missing_en = []
for el in data_vi_elements:
    if not el.get('data-cn'):
        missing_cn.append(el)
    if not el.get('data-en'):
        missing_en.append(el)

print(f"Elements missing data-cn: {len(missing_cn)}")
if missing_cn:
    for m in missing_cn[:5]:
        print("  Missing CN:", m)

print(f"Elements missing data-en: {len(missing_en)}")
if missing_en:
    for m in missing_en[:5]:
        print("  Missing EN:", m)

print("\n--- 2. CHECK SIDEBAR TARGETS ---")
sidebar_links = soup.find_all('a', class_='nav-link')
print(f"Total sidebar links: {len(sidebar_links)}")
missing_targets = []
for a in sidebar_links:
    target = a.get('data-target')
    if not target or not soup.find(id=target):
        missing_targets.append(target)

print(f"Missing targets in page: {missing_targets}")

print("\n--- 3. CHECK PLACEHOLDERS ---")
placeholders = soup.find_all(attrs={"data-vi-ph": True})
print(f"Total inputs with data-vi-ph: {len(placeholders)}")
for p in placeholders:
    print(f"  Input #{p.get('id')}: VI='{p.get('data-vi-ph')[:30]}...', EN='{p.get('data-en-ph')[:30]}...', CN='{p.get('data-cn-ph')[:30]}...'")

print("\n--- 4. CHECK ERROR CODE ROWS ---")
error_table = soup.find('table', id='errorTable')
if error_table:
    rows = error_table.find('tbody').find_all('tr')
    print(f"Total error code rows: {len(rows)}")
    for r in rows:
        code = r.find('code').text.strip()
        bi_spans = r.find_all('span', class_='cn')
        print(f"  Code {code}: CN spans count = {len(bi_spans)}")

print("\n--- 5. CHECK HERO RESOURCE CARDS ---")
meta_cards = soup.find_all('div', class_='hero-meta-card')
print(f"Total hero meta cards: {len(meta_cards)}")
for c in meta_cards:
    lbl = c.find('div', class_='label')
    if lbl:
        print(f"  Card: VI='{lbl.get('data-vi')}' | CN='{lbl.get('data-cn')}' | EN='{lbl.get('data-en')}'")

print("\n--- 6. CHECK SLA WORD CUT ---")
sla_text = soup.find(string=re.compile(r'khẩn cấp'))
print("SLA text found:", sla_text)
