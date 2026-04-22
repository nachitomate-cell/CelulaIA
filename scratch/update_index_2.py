import re

file_path = r'c:\Users\56983\OneDrive\Desktop\BARBERIA_ELEGANCE\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Background Grid (2.5% opacity)
old_body = """    body {
      margin: 0;
      background: var(--bg);
      color: var(--text);"""
new_body = """    body {
      margin: 0;
      background-color: var(--bg);
      background-image: 
        linear-gradient(rgba(255, 255, 255, 0.025) 1px, transparent 1px),
        linear-gradient(90deg, rgba(255, 255, 255, 0.025) 1px, transparent 1px);
      background-size: 32px 32px;
      color: var(--text);"""
content = content.replace(old_body, new_body)

# 2. Service Card Border (1.5px)
old_card_active = """    .service-card.active {
        border-color: var(--text);
        background-color: rgba(245, 244, 240, 0.02);
    }"""
new_card_active = """    .service-card.active {
        border: 1.5px solid var(--text);
        background-color: rgba(245, 244, 240, 0.02);
    }"""
content = content.replace(old_card_active, new_card_active)

# 3. Typography & SVG Size
old_css_icons_text = """    .service-icon {
        margin-bottom: 24px;
        width: 36px;
        height: 36px;
        display: flex;
        justify-content: center;
        align-items: center;
    }
    .service-icon svg {
        width: 100%;
        height: 100%;
        stroke: var(--text);
        stroke-width: 1px;
        fill: none;
        stroke-linecap: square;
        stroke-linejoin: miter;
    }
    .service-name {
        font-family: var(--font-serif);
        font-size: 16px;
        margin-bottom: 8px;
        font-weight: 600;
        letter-spacing: 0.5px;
    }
    .service-price {
        font-family: var(--font-sans);
        font-weight: 300;
        font-size: 13px;
        color: var(--muted);
        margin-top: auto;
    }"""

new_css_icons_text = """    .service-icon {
        margin-bottom: 16px;
        width: 28px;
        height: 28px;
        display: flex;
        justify-content: center;
        align-items: center;
    }
    .service-icon svg {
        width: 100%;
        height: 100%;
        stroke: var(--text);
        stroke-width: 1.2px;
        fill: none;
        stroke-linecap: square;
        stroke-linejoin: miter;
    }
    .service-name {
        font-family: var(--font-serif);
        font-size: 13px;
        margin-bottom: 6px;
        font-weight: 600;
        letter-spacing: 0.5px;
    }
    .service-price {
        font-family: var(--font-sans);
        font-weight: 300;
        font-size: 11px;
        color: rgba(245, 244, 240, 0.4);
        margin-top: auto;
    }"""
content = content.replace(old_css_icons_text, new_css_icons_text)

# 4. CTA JS Format
old_cta_js = """              btn.innerHTML = 'CONTINUAR • ' + formatCurrency(selectedService.precio);"""
new_cta_js = """              btn.innerHTML = 'CONTINUAR <span style="opacity:0.25; margin:0 12px; font-weight:300;">|</span> ' + formatCurrency(selectedService.precio);"""
content = content.replace(old_cta_js, new_cta_js)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated refinements successfully")
