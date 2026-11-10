# -*- coding: utf-8 -*-
"""
simulate_lang_switch.py
Simulates the client-side language switch to CN and EN and inspects the output.
"""

from bs4 import BeautifulSoup

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

def simulate(lang):
    soup = BeautifulSoup(html, 'html.parser')
    
    # 1. Update [data-vi]
    for el in soup.find_all(attrs={"data-vi": True}):
        txt = el.get(f'data-{lang}') or el.get('data-vi')
        el.string = txt
        
    # 2. Inspect Sidebar links
    sidebar_texts = [a.get_text().strip() for a in soup.find('nav', class_='sidebar').find_all('a', class_='nav-link')]
    print(f"\n[{lang.upper()}] Sample Sidebar Links (first 8):")
    for st in sidebar_texts[:8]:
        print("  ", st)
        
    # 3. Inspect Hero meta cards
    cards = soup.find('div', class_='hero-meta-grid').find_all('div', class_='hero-meta-card')
    print(f"\n[{lang.upper()}] Hero 4 Cards:")
    for c in cards:
        print("  ", c.find('div', class_='label').get_text().strip())

    # 4. Inspect Section headers
    headers = [h2.get_text().strip() for h2 in soup.find_all('h2')]
    print(f"\n[{lang.upper()}] Section Headers (first 5):")
    for h in headers[:5]:
        print("  ", h)

simulate('cn')
simulate('en')
simulate('vi')
