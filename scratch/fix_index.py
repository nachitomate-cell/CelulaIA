file_path = r'c:\Users\56983\OneDrive\Desktop\BARBERIA_ELEGANCE\index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Fix theme-color + add viewport-fit=cover
content = content.replace(
    'content="#050505"',
    'content="#0a0a0a"'
)
content = content.replace(
    'initial-scale=1.0, maximum-scale=1.0, user-scalable=no"',
    'initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover"'
)

# 2. Add Apple PWA metas after manifest link
content = content.replace(
    '<link rel="manifest" href="/manifest.json">',
    '''<link rel="manifest" href="/manifest.json">
  <meta name="apple-mobile-web-app-capable" content="yes">
  <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">'''
)

# 3. Translate Step 1 title
content = content.replace(
    'Choose your service',
    'Elige tu servicio'
)

# 4. Fix back button tap target
content = content.replace(
    '''    .back-btn {
      position: absolute;
      left: 0;
      top: 24px;
      width: 40px;
      height: 40px;''',
    '''    .back-btn {
      position: absolute;
      left: 0;
      top: 24px;
      width: 44px;
      height: 44px;'''
)

# 5. Fix nav-tab tap targets
content = content.replace(
    '''        padding: 8px 4px;
        transition: color 0.3s ease;
        position: relative;
        white-space: nowrap;''',
    '''        padding: 12px 8px;
        transition: color 0.3s ease;
        position: relative;
        white-space: nowrap;
        min-height: 44px;'''
)

# 6. Add step transition animation
content = content.replace(
    '    .step { display: none; padding-top: 22px; }\r\n    .step.active { display: block; }',
    '''    .step { display: none; padding-top: 22px; opacity: 0; }
    .step.active { display: block; animation: fadeUp 300ms ease-out forwards; }'''
)

# 7. Fix barber cards to luxury style
content = content.replace(
    '''    .barber-card {
      display: flex;
      align-items: center;
      gap: 14px;
      padding: 14px 13px;
      border-radius: 16px;
      border: 1px solid var(--line);
      background: var(--card);
      transition: 180ms ease;
    }
    .barber-card.dimmed { opacity: 0.42; }
    .barber-card.active {
      border-color: rgba(255,255,255,0.88);
      box-shadow: 0 0 16px rgba(255,255,255,0.12);
      background: rgba(255,255,255,0.04);
    }
    .barber-avatar {
      width: 46px;
      height: 46px;
      border-radius: 999px;
      background: #27272a;
      border: 1px solid rgba(255,255,255,0.12);
      flex-shrink: 0;
    }''',
    '''    .barber-card {
      display: flex;
      align-items: center;
      gap: 16px;
      padding: 16px;
      border-radius: 0;
      border: 0.5px solid var(--line);
      background: transparent;
      transition: all var(--transition-speed) cubic-bezier(0.4, 0, 0.2, 1);
      cursor: pointer;
      position: relative;
      overflow: hidden;
      min-height: 44px;
    }
    .barber-card.dimmed { opacity: 0.55; }
    .barber-card.active {
      border: 1.5px solid var(--text);
      background-color: rgba(245, 244, 240, 0.02);
    }
    .barber-card.active::after {
      content: '';
      position: absolute;
      left: 0; top: 0; bottom: 0;
      width: 3px;
      background-color: var(--text);
    }
    .barber-avatar {
      width: 44px;
      height: 44px;
      border-radius: 999px;
      background: transparent;
      border: 0.5px solid var(--line);
      flex-shrink: 0;
    }'''
)

# 8. Fix section-subtitle
content = content.replace(
    '''    .section-subtitle {
      font-size: 0.96rem;
      font-weight: 700;
      margin: 18px 0 10px;
    }''',
    '''    .section-subtitle {
      font-family: var(--font-sans);
      font-size: 10px;
      font-weight: 400;
      letter-spacing: 2px;
      text-transform: uppercase;
      color: var(--muted);
      margin: 24px 0 12px;
    }'''
)

# 9. Fix calendar/hours pills
content = content.replace(
    '''    .day-pill, .hour-pill {
      border-radius: 14px;
      border: 1px solid var(--line);
      background: #0b0b0f;
      color: #fff;
      padding: 11px 12px;
      min-width: 80px;
      text-align: center;
      font-weight: 700;
    }
    .hour-pill {
      min-width: 86px;
      padding: 11px 10px;
    }
    .day-pill.active, .hour-pill.active {
      border-color: rgba(255,255,255,0.88);
      box-shadow: 0 0 14px rgba(255,255,255,0.14);
      background: rgba(255,255,255,0.05);
    }
    .hour-pill.disabled {
      opacity: 0.3;
      pointer-events: none;
    }''',
    '''    .day-pill, .hour-pill {
      border-radius: 0;
      border: 0.5px solid var(--line);
      background: transparent;
      color: var(--text);
      padding: 12px 14px;
      min-width: 80px;
      text-align: center;
      font-family: var(--font-sans);
      font-weight: 400;
      font-size: 13px;
      transition: all var(--transition-speed) cubic-bezier(0.4, 0, 0.2, 1);
      min-height: 44px;
    }
    .hour-pill {
      min-width: 86px;
      padding: 12px 10px;
    }
    .day-pill.active, .hour-pill.active {
      border: 1.5px solid var(--text);
      background: rgba(245, 244, 240, 0.02);
    }
    .hour-pill.disabled {
      opacity: 0.2;
      pointer-events: none;
    }'''
)

# 10. Fix form fields
content = content.replace(
    '''    .form-field label {
      display: block;
      margin-bottom: 8px;
      font-size: 0.83rem;
      font-weight: 800;
      letter-spacing: 0.12em;
      text-transform: uppercase;
      color: #f4f4f5;
    }
    .form-input {
      width: 100%;
      border-radius: 16px;
      border: 1px solid rgba(255,255,255,0.14);
      background: #0c0c10;
      color: #fff;
      padding: 15px 16px;
      font-size: 1rem;
      outline: none;
    }''',
    '''    .form-field label {
      display: block;
      margin-bottom: 8px;
      font-family: var(--font-sans);
      font-size: 10px;
      font-weight: 400;
      letter-spacing: 2px;
      text-transform: uppercase;
      color: var(--muted);
    }
    .form-input {
      width: 100%;
      border-radius: 0;
      border: 0.5px solid var(--line);
      background: transparent;
      color: var(--text);
      padding: 16px;
      font-family: var(--font-sans);
      font-size: 14px;
      font-weight: 300;
      outline: none;
      transition: border-color 0.2s ease;
      min-height: 44px;
    }
    .form-input:focus {
      border-color: var(--text);
    }
    .form-input::placeholder {
      color: rgba(245, 244, 240, 0.25);
    }'''
)

# 11. Fix summary card
content = content.replace(
    '''    .summary-card {
      margin-top: 22px;
      padding: 18px;
      border-radius: 16px;
      background: #0b0b0f;
      border: 1px solid rgba(255,255,255,0.18);
      box-shadow: 0 0 16px rgba(255,255,255,0.06);
    }
    .summary-card h4 {
      margin: 0 0 12px;
      font-size: 0.72rem;
      text-transform: uppercase;
      letter-spacing: 0.18em;
      color: rgba(255,255,255,0.75);
    }
    .summary-row {
      display: flex;
      justify-content: space-between;
      gap: 10px;
      margin-top: 7px;
      color: #d4d4d8;
      font-size: 0.95rem;
    }''',
    '''    .summary-card {
      margin-top: 32px;
      padding: 24px;
      border-radius: 0;
      background: transparent;
      border: 0.5px solid var(--line);
    }
    .summary-card h4 {
      margin: 0 0 16px;
      font-family: var(--font-sans);
      font-size: 10px;
      font-weight: 400;
      text-transform: uppercase;
      letter-spacing: 2px;
      color: var(--muted);
    }
    .summary-row {
      display: flex;
      justify-content: space-between;
      gap: 10px;
      margin-top: 8px;
      padding: 8px 0;
      border-bottom: 0.5px solid rgba(245, 244, 240, 0.06);
      color: var(--muted);
      font-family: var(--font-sans);
      font-size: 13px;
      font-weight: 300;
    }
    .summary-row:last-child { border-bottom: none; }
    .summary-row strong {
      color: var(--text);
      font-weight: 400;
    }'''
)

# 12. Fix success state
content = content.replace(
    '''    .success-icon {
      width: 92px;
      height: 92px;
      margin: 0 auto 18px;
      border-radius: 999px;
      border: 1px solid rgba(255,255,255,0.5);
      display: grid;
      place-items: center;
      font-size: 2.8rem;
      box-shadow: 0 0 24px rgba(255,255,255,0.12);
    }''',
    '''    .success-icon {
      width: 72px;
      height: 72px;
      margin: 0 auto 24px;
      border-radius: 999px;
      border: 0.5px solid var(--line);
      display: grid;
      place-items: center;
      font-size: 2rem;
    }'''
)

# 13. Fix club banner
content = content.replace(
    '''    .club-banner {
      margin-top: 24px;
      padding: 16px;
      border-radius: 18px;
      border: 1px solid rgba(255,255,255,0.14);
      background: #0b0b0f;
    }
    .club-banner .tiny {
      font-size: 0.7rem;
      letter-spacing: 0.18em;
      text-transform: uppercase;
      color: rgba(255,255,255,0.55);
      font-weight: 800;
    }''',
    '''    .club-banner {
      margin-top: 32px;
      padding: 24px;
      border-radius: 0;
      border: 0.5px solid var(--line);
      background: transparent;
    }
    .club-banner .tiny {
      font-family: var(--font-sans);
      font-size: 10px;
      letter-spacing: 2px;
      text-transform: uppercase;
      color: var(--muted);
      font-weight: 400;
    }'''
)

# 14. Fix footer - replace emojis
content = content.replace(
    '''        <div>𝐄𝐥𝐞𝐠𝐚𝐧𝐜𝐞 𝐛𝐚𝐫𝐛𝐞𝐫𝐬𝐡𝐨𝐩 | Cortes premium.</div>\r\n        <div>📍 Ecuador 243 | Viña del Mar</div>\r\n        <div>🕒 Lunes-Sáb: 10-20h | Dom: 12-20h. ¡Reserva ya! #EleganceBarbershop</div>''',
    '''        <div style="font-family:var(--font-serif);font-weight:700;letter-spacing:2px;text-transform:uppercase;margin-bottom:8px;">Elegance Barbershop</div>\r\n        <div>Ecuador 243 · Viña del Mar</div>\r\n        <div>Lunes–Sáb: 10–20h · Dom: 12–20h</div>'''
)

# 15. Fix footer style
content = content.replace(
    '''    .footer {
      margin-top: 26px;
      padding-top: 22px;
      border-top: 1px solid rgba(255,255,255,0.08);
      text-align: center;
      color: var(--muted);
      font-size: 0.92rem;
      line-height: 1.6;
    }''',
    '''    .footer {
      margin-top: 40px;
      padding-top: 24px;
      border-top: 0.5px solid var(--line);
      text-align: center;
      color: var(--muted);
      font-family: var(--font-sans);
      font-size: 11px;
      font-weight: 300;
      letter-spacing: 1px;
      line-height: 2;
    }'''
)

# 16. Fix barber name/subtitle inline styles in JS
content = content.replace(
    'font-weight:800; font-size:1rem;',
    'font-family:var(--font-serif); font-weight:600; font-size:14px; letter-spacing:0.5px;'
)
content = content.replace(
    'color:#9ca3af; margin-top:4px; font-size:0.9rem;',
    'color:var(--muted); margin-top:4px; font-family:var(--font-sans); font-size:11px; font-weight:300; letter-spacing:1px;'
)

# 17. Fix calendar inline styles
content = content.replace(
    'font-size:0.75rem; text-transform:uppercase; color:#9ca3af;',
    'font-family:var(--font-sans); font-size:10px; text-transform:uppercase; color:var(--muted); letter-spacing:1px; font-weight:300;'
)

# 18. Fix step 4 inline p color
content = content.replace(
    'color:#9ca3af; margin:-6px 0 22px;',
    'color:var(--muted); margin:0 0 32px; font-size:13px; font-weight:300; text-align:center;'
)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("index.html updated successfully")
