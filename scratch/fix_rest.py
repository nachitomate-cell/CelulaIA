import re

# === SHARED LUXURY STYLE BLOCK ===
luxury_style_block = '''
    :root {
      --bg: #0a0a0a;
      --text: #f5f4f0;
      --muted: rgba(245, 244, 240, 0.6);
      --line: rgba(245, 244, 240, 0.15);
      --font-serif: 'Cormorant Garamond', serif;
      --font-sans: 'DM Sans', sans-serif;
      --safe-area-bottom: env(safe-area-inset-bottom, 20px);
    }
    body {
      background-color: var(--bg);
      background-image:
        linear-gradient(rgba(255,255,255,0.025) 1px, transparent 1px),
        linear-gradient(90deg, rgba(255,255,255,0.025) 1px, transparent 1px);
      background-size: 32px 32px;
      color: var(--text);
      -webkit-font-smoothing: antialiased;
      overscroll-behavior: none;
      -webkit-tap-highlight-color: transparent;
    }
    @keyframes fadeUp {
      from { opacity: 0; transform: translateY(16px); }
      to { opacity: 1; transform: translateY(0); }
    }
'''

luxury_fonts = '<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,600;0,700;1,400&family=DM+Sans:wght@300;400;500&display=swap" rel="stylesheet">'

# ============================================================
# 1. FIX registro.html
# ============================================================
with open(r'c:\Users\56983\OneDrive\Desktop\BARBERIA_ELEGANCE\registro.html', 'r', encoding='utf-8') as f:
    reg = f.read()

# Fix viewport
reg = reg.replace(
    'initial-scale=1.0, maximum-scale=1.0, user-scalable=no"',
    'initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover"'
)

# Fix theme-color
reg = reg.replace('content="#050505"', 'content="#0a0a0a"')

# Fix fonts
reg = reg.replace(
    '<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">',
    luxury_fonts
)

# Add Apple PWA metas
reg = reg.replace(
    '<link rel="manifest" href="/manifest.json">',
    '<link rel="manifest" href="/manifest.json">\n  <meta name="apple-mobile-web-app-capable" content="yes">\n  <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">'
)

# Replace inline style block
reg = reg.replace(
    '''  <style>
    body { background-color:#050505; color:#f8fafc; overscroll-behavior-y:none; -webkit-tap-highlight-color:transparent; }
    .text-neon { color:#fff; text-shadow:0 0 5px rgba(255,255,255,0.4),0 0 10px rgba(255,255,255,0.2); }
    .border-neon { border-color:#fff; box-shadow:0 0 6px rgba(255,255,255,0.2),inset 0 0 6px rgba(255,255,255,0.05); }
    input:-webkit-autofill { -webkit-box-shadow:0 0 0 100px #111115 inset !important; -webkit-text-fill-color:#f8fafc !important; }
    .tab-btn.active { color:#fff; border-color:rgba(255,255,255,0.6); }
  </style>''',
    '''  <style>''' + luxury_style_block + '''
    .text-neon { color: var(--text); }
    .border-neon { border-color: var(--text); box-shadow: none; }
    input:-webkit-autofill { -webkit-box-shadow:0 0 0 100px #0a0a0a inset !important; -webkit-text-fill-color: var(--text) !important; }
    .tab-btn.active { color: var(--text); border-color: var(--text); }
    .tab-btn { transition: color 0.2s ease; }
    h1.text-neon { font-family: var(--font-serif); font-weight: 700; letter-spacing: 2px; text-shadow: none; }
  </style>'''
)

with open(r'c:\Users\56983\OneDrive\Desktop\BARBERIA_ELEGANCE\registro.html', 'w', encoding='utf-8') as f:
    f.write(reg)
print("registro.html updated")

# ============================================================
# 2. FIX dashboard.html
# ============================================================
with open(r'c:\Users\56983\OneDrive\Desktop\BARBERIA_ELEGANCE\dashboard.html', 'r', encoding='utf-8') as f:
    dash = f.read()

# Fix viewport
dash = dash.replace(
    'initial-scale=1.0, maximum-scale=1.0, user-scalable=no"',
    'initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover"'
)

# Fix theme-color
dash = dash.replace('content="#050505"', 'content="#0a0a0a"')

# Fix fonts
dash = dash.replace(
    '<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">',
    luxury_fonts
)

# Add Apple PWA metas
dash = dash.replace(
    '<link rel="manifest" href="/manifest.json">',
    '<link rel="manifest" href="/manifest.json">\n  <meta name="apple-mobile-web-app-capable" content="yes">\n  <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">'
)

# Replace inline style block
dash = dash.replace(
    '''  <style>
    body { background-color:#050505; color:#f8fafc; overscroll-behavior-y:none; -webkit-tap-highlight-color:transparent; }
    .text-neon { color:#fff; text-shadow:0 0 5px rgba(255,255,255,0.4),0 0 10px rgba(255,255,255,0.2); }
    .border-neon { border-color:#fff; box-shadow:0 0 6px rgba(255,255,255,0.2),inset 0 0 6px rgba(255,255,255,0.05); }
    .no-scrollbar::-webkit-scrollbar { display:none; }
    .no-scrollbar { -ms-overflow-style:none; scrollbar-width:none; }
  </style>''',
    '''  <style>''' + luxury_style_block + '''
    .text-neon { color: var(--text); text-shadow: none; }
    .border-neon { border-color: var(--text); box-shadow: none; }
    .no-scrollbar::-webkit-scrollbar { display:none; }
    .no-scrollbar { -ms-overflow-style:none; scrollbar-width:none; }
    h1.text-neon, h2.text-neon { font-family: var(--font-serif); font-weight: 700; letter-spacing: 2px; text-shadow: none; }
  </style>'''
)

with open(r'c:\Users\56983\OneDrive\Desktop\BARBERIA_ELEGANCE\dashboard.html', 'w', encoding='utf-8') as f:
    f.write(dash)
print("dashboard.html updated")

# ============================================================
# 3. FIX gestion-interna.html
# ============================================================
with open(r'c:\Users\56983\OneDrive\Desktop\BARBERIA_ELEGANCE\gestion-interna.html', 'r', encoding='utf-8') as f:
    gi = f.read()

# Fix viewport
gi = gi.replace(
    'initial-scale=1.0, maximum-scale=1.0, user-scalable=no"',
    'initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover"'
)

# Fix theme-color
gi = gi.replace('content="#09090b"', 'content="#0a0a0a"')

# Fix fonts
gi = gi.replace(
    '<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">',
    luxury_fonts
)

# Fix body background in style
gi = gi.replace(
    'background-color: #09090b;',
    'background-color: #0a0a0a;\n      background-image: linear-gradient(rgba(255,255,255,0.025) 1px, transparent 1px), linear-gradient(90deg, rgba(255,255,255,0.025) 1px, transparent 1px);\n      background-size: 32px 32px;'
)

with open(r'c:\Users\56983\OneDrive\Desktop\BARBERIA_ELEGANCE\gestion-interna.html', 'w', encoding='utf-8') as f:
    f.write(gi)
print("gestion-interna.html updated")

# ============================================================
# 4. FIX manifest.json
# ============================================================
import json
manifest = {
    "name": "Elegance Barbershop | Reservas",
    "short_name": "ELEGANCE",
    "description": "Reserva tu hora en Elegance Barbershop",
    "start_url": "/index.html",
    "scope": "/",
    "display": "standalone",
    "background_color": "#0a0a0a",
    "theme_color": "#0a0a0a",
    "orientation": "portrait",
    "icons": [
        {
            "src": "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 512 512'%3E%3Crect width='512' height='512' fill='%230a0a0a'/%3E%3Ctext x='256' y='300' text-anchor='middle' font-family='serif' font-size='200' font-weight='700' fill='%23f5f4f0'%3EE%3C/text%3E%3C/svg%3E",
            "sizes": "512x512",
            "type": "image/svg+xml",
            "purpose": "any maskable"
        }
    ]
}

with open(r'c:\Users\56983\OneDrive\Desktop\BARBERIA_ELEGANCE\manifest.json', 'w', encoding='utf-8') as f:
    json.dump(manifest, f, indent=2, ensure_ascii=False)
print("manifest.json updated")

print("\n=== ALL FILES UPDATED SUCCESSFULLY ===")
