import re
import os

file_path = r'c:\Users\56983\OneDrive\Desktop\BARBERIA_ELEGANCE\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update fonts
content = content.replace(
    '<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">',
    '<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,600;0,700;1,400&family=DM+Sans:wght@300;400;500&display=swap" rel="stylesheet">'
)

# 2. Update CSS variables & body
old_css_root = """    :root {
      --bg: #050505;
      --panel: #0b0b0f;
      --card: #101014;
      --line: rgba(255,255,255,0.14);
      --line-strong: rgba(255,255,255,0.5);
      --text: #f7f7f8;
      --muted: #9ca3af;
    }
    * { box-sizing: border-box; }
    body {
      margin: 0;
      background: var(--bg);
      color: var(--text);
      font-family: "Inter", sans-serif;
      -webkit-tap-highlight-color: transparent;
    }"""

new_css_root = """    :root {
      --bg: #0a0a0a;
      --panel: #0a0a0a;
      --card: transparent;
      --line: rgba(245, 244, 240, 0.15);
      --line-strong: rgba(245, 244, 240, 0.5);
      --text: #f5f4f0;
      --muted: rgba(245, 244, 240, 0.6);
      --border-hover: rgba(245, 244, 240, 0.5);
      --font-serif: 'Cormorant Garamond', serif;
      --font-sans: 'DM Sans', sans-serif;
      --transition-speed: 0.3s;
      --safe-area-bottom: env(safe-area-inset-bottom, 20px);
      --safe-area-top: env(safe-area-inset-top, 20px);
    }
    * { box-sizing: border-box; }
    body {
      margin: 0;
      background: var(--bg);
      color: var(--text);
      font-family: var(--font-sans);
      line-height: 1.5;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      overflow-x: hidden;
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
      -webkit-tap-highlight-color: transparent;
      overscroll-behavior: none;
    }
    @keyframes fadeUp {
      from { opacity: 0; transform: translateY(20px); }
      to { opacity: 1; transform: translateY(0); }
    }
    
    /* Ripple Effect */
    .ripple {
        position: absolute;
        border-radius: 50%;
        transform: scale(0);
        animation: ripple 600ms linear;
        background-color: rgba(245, 244, 240, 0.1);
        pointer-events: none;
    }
    @keyframes ripple {
        to { transform: scale(4); opacity: 0; }
    }"""

content = content.replace(old_css_root, new_css_root)

# 3. Update app and header
old_css_app = """    .app {
      width: 100%;
      max-width: 390px;
      margin: 0 auto;
      min-height: 100vh;
      padding: 0 16px 120px;
      position: relative;
    }
    .header {
      position: sticky;
      top: 0;
      z-index: 20;
      background: rgba(5,5,5,0.96);
      backdrop-filter: blur(14px);
      padding: 14px 0 12px;
      text-align: center;
      border-bottom: 1px solid rgba(255,255,255,0.05);
    }
    .back-btn {
      position: absolute;
      left: 0;
      top: 14px;
      width: 40px;
      height: 40px;
      border-radius: 999px;
      border: 1px solid rgba(255,255,255,0.18);
      background: #0b0b0f;
      color: #fff;
      display: flex;
      align-items: center;
      justify-content: center;
      box-shadow: 0 0 12px rgba(255,255,255,0.12);
    }
    .logo-placeholder {
      width: 84px;
      height: 84px;
      margin: 4px auto 12px;
      border-radius: 999px;
      border: 2px solid rgba(255,255,255,0.65);
      background:
        linear-gradient(180deg, rgba(255,255,255,0.12), rgba(255,255,255,0.02)),
        #101014;
      display: grid;
      place-items: center;
      box-shadow: 0 0 24px rgba(255,255,255,0.16);
      position: relative;
      overflow: hidden;
    }
    .logo-placeholder::before {
      content: "";
      width: 38px;
      height: 38px;
      border: 2px solid white;
      transform: rotate(45deg);
      opacity: 0.92;
    }
    .brand-name {
      font-size: 1.9rem;
      font-weight: 800;
      letter-spacing: 0.02em;
      margin: 0 0 2px;
    }
    .brand-sub {
      margin: 0;
      font-size: 0.72rem;
      font-weight: 700;
      letter-spacing: 0.28em;
      text-transform: uppercase;
      color: rgba(255,255,255,0.82);
    }"""

new_css_app = """    .app {
      width: 100%;
      max-width: 600px;
      margin: 0 auto;
      min-height: 100vh;
      padding: var(--safe-area-top) 16px calc(var(--safe-area-bottom) + 120px);
      position: relative;
      animation: fadeUp 300ms ease-out forwards;
    }
    .header {
      text-align: center;
      padding: 32px 0 16px;
      position: relative;
    }
    .back-btn {
      position: absolute;
      left: 0;
      top: 24px;
      width: 40px;
      height: 40px;
      border-radius: 999px;
      border: 1px solid var(--line);
      background: transparent;
      color: var(--text);
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      z-index: 10;
    }
    .logo-placeholder { display: none; }
    .brand-name {
      font-family: var(--font-serif);
      font-weight: 700;
      font-size: 20px;
      letter-spacing: 2px;
      text-transform: uppercase;
      margin-bottom: 40px;
    }
    .brand-sub { display: none; }"""

content = content.replace(old_css_app, new_css_app)

# 4. Update Progress Bar CSS
old_css_progress = """    .progress-wrap { margin-top: 18px; }
    .progress-top {
      display: flex;
      justify-content: space-between;
      margin-bottom: 8px;
      font-size: 0.72rem;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.12em;
    }
    .progress-bar {
      width: 100%;
      height: 6px;
      border-radius: 999px;
      background: #18181b;
      border: 1px solid rgba(255,255,255,0.06);
      overflow: hidden;
    }
    .progress-fill {
      height: 100%;
      width: 25%;
      border-radius: 999px;
      background: #ffffff;
      box-shadow: 0 0 12px rgba(255,255,255,0.45);
      transition: width 220ms ease;
    }"""

new_css_progress = """    .progress-wrap {
      margin: 0 0 48px;
      display: flex;
      flex-direction: column;
      align-items: center;
    }
    .progress-top { display: none; }
    .progress-bar {
      display: flex;
      gap: 4px;
      width: 100%;
      margin-bottom: 16px;
      background: transparent;
      border: none;
      height: 1px;
      border-radius: 0;
      overflow: visible;
    }
    .progress-segment {
      height: 1px;
      flex: 1;
      background-color: var(--line);
      position: relative;
      transition: background-color 0.3s ease;
    }
    .progress-segment.active { background-color: var(--text); }
    .progress-label {
      font-family: var(--font-sans);
      font-size: 10px;
      letter-spacing: 2px;
      text-transform: uppercase;
      font-weight: 400;
    }"""

content = content.replace(old_css_progress, new_css_progress)

# 5. Update Step CSS & Titles
old_css_title = """    .title {
      margin: 0 0 16px;
      font-size: 2rem;
      font-weight: 800;
      line-height: 1.1;
    }"""

new_css_title = """    .title {
      font-family: var(--font-serif);
      font-style: italic;
      font-weight: 400;
      font-size: 36px;
      text-align: center;
      margin: 0 0 40px;
      line-height: 1.1;
    }"""
content = content.replace(old_css_title, new_css_title)

# 6. Update Pills to Tabs
old_css_pills = """    .pills {
      display: flex;
      gap: 8px;
      overflow-x: auto;
      padding-bottom: 12px;
      scrollbar-width: none;
    }
    .pills::-webkit-scrollbar { display: none; }
    .pill {
      white-space: nowrap;
      border-radius: 999px;
      border: 1px solid rgba(255,255,255,0.18);
      background: #0b0b0f;
      color: #d4d4d8;
      padding: 9px 15px;
      font-weight: 700;
      font-size: 0.86rem;
    }
    .pill.active {
      border-color: rgba(255,255,255,0.85);
      box-shadow: 0 0 16px rgba(255,255,255,0.18);
      color: #fff;
    }"""

new_css_pills = """    .nav-tabs {
        display: flex;
        justify-content: center;
        gap: 32px;
        margin-bottom: 40px;
        position: relative;
        overflow-x: auto;
        scrollbar-width: none;
    }
    .nav-tabs::-webkit-scrollbar { display: none; }
    .nav-tab {
        font-family: var(--font-sans);
        font-size: 13px;
        letter-spacing: 2px;
        text-transform: uppercase;
        color: var(--muted);
        cursor: pointer;
        padding: 8px 4px;
        transition: color 0.3s ease;
        position: relative;
        white-space: nowrap;
        background: transparent;
        border: none;
    }
    .nav-tab.active {
        color: var(--text);
    }
    .nav-underline {
        position: absolute;
        bottom: 0;
        left: 0;
        height: 1px;
        background-color: var(--text);
        transition: transform 0.2s cubic-bezier(0.4, 0, 0.2, 1), width 0.2s cubic-bezier(0.4, 0, 0.2, 1);
    }"""
content = content.replace(old_css_pills, new_css_pills)

# 7. Update Grid and Cards
old_css_grid = """    .services-grid {
      display: grid;
      grid-template-columns: repeat(2, minmax(0, 1fr));
      gap: 12px;
      margin-top: 10px;
    }
    .service-card {
      min-height: 154px;
      border-radius: 16px;
      background: var(--card);
      border: 1px solid var(--line);
      padding: 14px 10px 12px;
      text-align: center;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      gap: 10px;
      transition: 180ms ease;
      box-shadow: inset 0 0 0 1px rgba(255,255,255,0.02);
    }
    .service-card.active {
      border-color: rgba(255,255,255,0.85);
      transform: translateY(-1px);
      box-shadow: 0 0 16px rgba(255,255,255,0.12);
    }
    .service-icon {
      width: 48px;
      height: 48px;
      border-radius: 999px;
      border: 1px solid rgba(255,255,255,0.2);
      display: grid;
      place-items: center;
      color: #f4f4f5;
      font-size: 1.35rem;
      background: rgba(255,255,255,0.03);
    }
    .service-name {
      font-size: 0.88rem;
      font-weight: 800;
      line-height: 1.18;
    }
    .service-price {
      font-size: 1.05rem;
      font-weight: 800;
    }
    .service-meta {
      color: var(--muted);
      font-size: 0.74rem;
      display: flex;
      align-items: center;
      gap: 4px;
    }"""

new_css_grid = """    .services-grid {
        display: flex;
        flex-direction: column;
        gap: 16px;
    }
    @media (min-width: 768px) {
        .services-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 24px;
        }
    }
    .service-card {
        background: transparent;
        border: 0.5px solid var(--line);
        padding: 32px 24px;
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
        position: relative;
        cursor: pointer;
        transition: all var(--transition-speed) cubic-bezier(0.4, 0, 0.2, 1);
        overflow: hidden;
        min-height: 170px;
        color: var(--text);
    }
    @media (hover: hover) {
        .service-card:hover {
            border-color: var(--border-hover);
            transform: translateY(-2px);
            box-shadow: 0 8px 24px rgba(0, 0, 0, 0.6);
        }
        .service-card:hover::before {
            opacity: 1;
        }
    }
    .service-card::before {
        content: '';
        position: absolute;
        top: 0; left: 0; right: 0; bottom: 0;
        box-shadow: inset 0 0 40px rgba(245, 244, 240, 0.03);
        opacity: 0;
        transition: opacity var(--transition-speed) ease;
        pointer-events: none;
    }
    .service-card.active {
        border-color: var(--text);
        background-color: rgba(245, 244, 240, 0.02);
    }
    .service-card.active::after {
        content: '';
        position: absolute;
        left: 0;
        top: 0;
        bottom: 0;
        width: 3px;
        background-color: var(--text);
    }
    .checkmark {
        position: absolute;
        top: 16px;
        right: 16px;
        opacity: 0;
        transform: scale(0.8);
        transition: all var(--transition-speed) cubic-bezier(0.4, 0, 0.2, 1);
    }
    .service-card.active .checkmark {
        opacity: 1;
        transform: scale(1);
    }
    .service-icon {
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
    }
    .service-meta {
        font-size: 11px;
        color: var(--muted);
        margin-top: 4px;
        letter-spacing: 1px;
        text-transform: uppercase;
    }"""
content = content.replace(old_css_grid, new_css_grid)

# 8. Update CTA styles
old_css_cta = """    .sticky-cta {
      position: fixed;
      left: 50%;
      bottom: 18px;
      transform: translateX(-50%);
      width: calc(100% - 32px);
      max-width: 386px;
      z-index: 30;
    }
    .sticky-cta button {
      width: 100%;
      min-height: 56px;
      border-radius: 999px;
      border: 1px solid rgba(255,255,255,0.75);
      background: #0b0b0f;
      color: #fff;
      font-weight: 800;
      font-size: 1rem;
      box-shadow: 0 0 18px rgba(255,255,255,0.14);
    }"""

new_css_cta = """    .sticky-cta {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        padding: 16px 16px calc(16px + var(--safe-area-bottom));
        background: linear-gradient(to top, rgba(10, 10, 10, 1) 50%, rgba(10, 10, 10, 0));
        display: flex;
        justify-content: center;
        z-index: 30;
    }
    .sticky-cta button {
        width: 100%;
        max-width: 600px;
        background-color: var(--text);
        color: var(--bg);
        border: none;
        border-radius: 4px;
        padding: 0 24px;
        font-family: var(--font-sans);
        font-size: 13px;
        font-weight: 500;
        letter-spacing: 2px;
        text-transform: uppercase;
        cursor: pointer;
        height: 56px;
        transition: all 0.2s ease;
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 8px;
    }
    @media (hover: hover) {
        .sticky-cta button:not(:disabled):hover {
            background-color: #e8e8e8;
            transform: scale(1.01);
        }
    }
    .sticky-cta button:active {
        transform: scale(0.98);
    }
    .sticky-cta button:disabled {
        opacity: 0.2;
        cursor: not-allowed;
        transform: none;
    }"""
content = content.replace(old_css_cta, new_css_cta)

# 9. Update HTML Structure for Header & Step 1
old_html_header = """      <div class="progress-wrap">
        <div class="progress-top">
          <span id="stepText">Paso 1 de 4: Servicios</span>
          <span id="stepPct">25%</span>
        </div>
        <div class="progress-bar">
          <div class="progress-fill" id="progressFill"></div>
        </div>
      </div>
    </header>

    <main>
      <section class="step active" id="step1">
        <h2 class="title">¿Qué servicio buscas?</h2>
        <div class="pills" id="categoryPills"></div>
        <div class="services-grid" id="servicesGrid"></div>
      </section>"""

new_html_header = """      <div class="progress-wrap">
        <div class="progress-bar" id="progressBar">
            <div class="progress-segment active"></div>
            <div class="progress-segment"></div>
            <div class="progress-segment"></div>
            <div class="progress-segment"></div>
        </div>
        <div class="progress-label" id="stepLabel">Step 1 of 4</div>
      </div>
    </header>

    <main>
      <section class="step active" id="step1">
        <h2 class="title">Choose your service</h2>
        <div class="nav-tabs" id="categoryTabs">
            <div class="nav-underline" id="navUnderline"></div>
        </div>
        <div class="services-grid" id="servicesGrid"></div>
      </section>"""
content = content.replace(old_html_header, new_html_header)

# 10. Update JS logic
old_js_progress = """    function syncProgress() {
      document.getElementById("stepText").textContent = steps[currentStep - 1];
      document.getElementById("stepPct").textContent = percentages[currentStep - 1];
      document.getElementById("progressFill").style.width = percentages[currentStep - 1];
      document.getElementById("ctaBtn").innerHTML = currentStep === 4
        ? 'Reservar ahora <i class="ph-bold ph-check"></i>'
        : 'Continuar <i class="ph-bold ph-arrow-right"></i>';
    }"""

new_js_progress = """    function syncProgress() {
      document.getElementById("stepLabel").textContent = "Step " + currentStep + " of 4";
      const segments = document.querySelectorAll('.progress-segment');
      segments.forEach((seg, idx) => {
          if(idx < currentStep) seg.classList.add('active');
          else seg.classList.remove('active');
      });
      
      const btn = document.getElementById("ctaBtn");
      if(currentStep === 4) {
          btn.innerHTML = 'RESERVAR AHORA';
      } else {
          if (currentStep === 1 && selectedService) {
              btn.innerHTML = 'CONTINUAR • ' + formatCurrency(selectedService.precio);
          } else {
              btn.innerHTML = 'CONTINUAR';
          }
      }
      
      if(currentStep === 1) {
          btn.disabled = selectedService === null;
      } else if (currentStep === 2) {
          btn.disabled = selectedBarber === null;
      } else if (currentStep === 3) {
          btn.disabled = selectedDate === null || selectedHour === null;
      } else {
          btn.disabled = false;
      }
    }"""
content = content.replace(old_js_progress, new_js_progress)

# Replace renderCategoryPills with renderCategoryTabs
old_js_pills = """    function renderCategoryPills() {
      const container = document.getElementById("categoryPills");
      container.innerHTML = "";
      categories.forEach((category) => {
        const button = document.createElement("button");
        button.className = `pill${currentCategory === category ? " active" : ""}`;
        button.textContent = category;
        button.onclick = () => {
          currentCategory = category;
          renderCategoryPills();
          renderServices();
        };
        container.appendChild(button);
      });
    }"""

new_js_pills = """    function updateUnderline() {
        const activeTab = document.querySelector('.nav-tab.active');
        const underline = document.getElementById('navUnderline');
        if (activeTab && underline) {
            underline.style.width = `${activeTab.offsetWidth}px`;
            underline.style.transform = `translateX(${activeTab.offsetLeft}px)`;
        }
    }

    function renderCategoryTabs() {
      const container = document.getElementById("categoryTabs");
      // Keep underline
      const underline = document.getElementById('navUnderline');
      container.innerHTML = "";
      container.appendChild(underline);
      
      categories.forEach((category) => {
        const button = document.createElement("button");
        button.className = `nav-tab${currentCategory === category ? " active" : ""}`;
        button.textContent = category;
        button.onclick = () => {
          currentCategory = category;
          renderCategoryTabs();
          renderServices();
          setTimeout(updateUnderline, 50);
        };
        container.insertBefore(button, underline);
      });
      setTimeout(updateUnderline, 50);
    }"""
content = content.replace(old_js_pills, new_js_pills)
content = content.replace("renderCategoryPills()", "renderCategoryTabs()")

# Replace renderServices logic
old_js_services = """    const iconByCategory = {
      Cortes: "ph-scissors",
      Barba: "ph-mask-happy",
      Combos: "ph-sparkle"
    };"""

new_js_services = """    const svgs = {
        scissors: '<svg viewBox="0 0 24 24"><circle cx="6" cy="6" r="2.5"/><circle cx="6" cy="18" r="2.5"/><path d="M8.5 7.5L20 19M8.5 16.5L12 13M16 9L20 5"/></svg>',
        razor: '<svg viewBox="0 0 24 24"><path d="M16 4H8v5c0 1.5-1 3-3 3H4v8h12c1.5 0 3-1.5 3-3V9c0-1.5 1-3 3-3h1V4h-7z"/></svg>',
        comb: '<svg viewBox="0 0 24 24"><path d="M4 8h16v4c0 1.1-.9 2-2 2H6c-1.1 0-2-.9-2-2V8z"/><path d="M6 8v4M9 8v4M12 8v4M15 8v4M18 8v4"/></svg>',
        combo: '<svg viewBox="0 0 24 24"><path d="M16 4h4v16h-4z"/><path d="M16 6h-4M16 10h-3M16 14h-4M16 18h-3M4 14l5-5-2-2-5 5z"/></svg>'
    };
    
    const iconByCategory = {
      Cortes: svgs.scissors,
      Barba: svgs.razor,
      Combos: svgs.combo,
      Extras: svgs.comb
    };"""
content = content.replace(old_js_services, new_js_services)

old_js_renderservices = """    function renderServices() {
      const grid = document.getElementById("servicesGrid");
      grid.innerHTML = "";
      getServicesFiltered().forEach((service) => {
        const icon = iconByCategory[service.categoria] || "ph-scissors";
        const card = document.createElement("button");
        card.className = `service-card${selectedService?.id === service.id ? " active" : ""}`;
        card.innerHTML = `
          <div class="service-icon"><i class="ph ${icon}"></i></div>
          <div class="service-name">${service.nombre}</div>
          <div class="service-price">${formatCurrency(service.precio)}</div>
          <div class="service-meta"><i class="ph ph-clock"></i> ${service.duracion} min</div>
        `;
        card.onclick = () => {
          selectedService = service;
          selectedHour = null;
          renderServices();
          updateSummary();
        };
        grid.appendChild(card);
      });
    }"""

new_js_renderservices = """    function renderServices() {
      const grid = document.getElementById("servicesGrid");
      grid.innerHTML = "";
      getServicesFiltered().forEach((service) => {
        const iconSvg = iconByCategory[service.categoria] || svgs.scissors;
        const isActive = selectedService?.id === service.id;
        const card = document.createElement("div");
        card.className = `service-card${isActive ? " active" : ""}`;
        
        card.innerHTML = `
          <div class="checkmark">
              <svg width="24" height="24" viewBox="0 0 24 24">
                  <path d="M5 13l4 4L19 7" stroke="var(--text)" stroke-width="1" fill="none" stroke-linecap="square"/>
              </svg>
          </div>
          <div class="service-icon">${iconSvg}</div>
          <div class="service-name">${service.nombre}</div>
          <div class="service-price">${formatCurrency(service.precio)}</div>
          <div class="service-meta">${service.duracion} min</div>
        `;
        card.onclick = (e) => {
          // Ripple
          const circle = document.createElement("span");
          const diameter = Math.max(card.clientWidth, card.clientHeight);
          const radius = diameter / 2;
          const rect = card.getBoundingClientRect();
          circle.style.width = circle.style.height = `${diameter}px`;
          circle.style.left = `${e.clientX - rect.left - radius}px`;
          circle.style.top = `${e.clientY - rect.top - radius}px`;
          circle.classList.add("ripple");
          const oldRipple = card.querySelector(".ripple");
          if (oldRipple) oldRipple.remove();
          card.appendChild(circle);

          if (selectedService?.id === service.id) {
              selectedService = null;
          } else {
              selectedService = service;
          }
          selectedHour = null;
          setTimeout(() => {
              renderServices();
              updateSummary();
              syncProgress();
          }, 150);
        };
        grid.appendChild(card);
      });
    }"""
content = content.replace(old_js_renderservices, new_js_renderservices)

# Add event listener for resize
content = content.replace(
    'window.addEventListener("DOMContentLoaded", () => {',
    'window.addEventListener("resize", updateUnderline);\n    window.addEventListener("DOMContentLoaded", () => {'
)

# Update barber and date clicks to sync progress properly
content = content.replace(
    'updateSummary();\n        };',
    'updateSummary();\n          syncProgress();\n        };'
)

# Inject CTA btn initial update call
content = content.replace(
    'showStep(1);\n    });',
    'showStep(1);\n      syncProgress();\n    });'
)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated successfully")
