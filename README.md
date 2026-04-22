# Elegance Barbershop — Web App

> *No es un corte, es elegancia que te mereces.*

Aplicación web completa para la gestión de reservas, fidelización de clientes y panel administrativo de **Elegance Barbershop**, Viña del Mar.

---

## Estructura del proyecto

```
elegance-barbershop/
├── index.html              # Flujo de reserva (5 pasos)
├── pages/
│   ├── club.html           # Mi Club — registro y sellos de fidelidad
│   ├── barbero.html        # Panel del barbero — agenda individual
│   └── admin.html          # Panel administrador + vista desarrollador
├── css/
│   └── main.css            # Estilos globales (design system B&W)
├── js/
│   ├── booking.js          # Lógica del flujo de reserva
│   ├── club.js             # Registro, login y dashboard del club
│   ├── barbero.js          # Panel de citas del barbero
│   └── admin.js            # Administración y monitor de anomalías
└── assets/                 # (para imágenes del lookbook y logo)
```

---

## Módulos

### `/` — Reserva (index.html)
Flujo de 5 pasos:
1. **Servicio** — Cortes, Barba, Combos, Extras
2. **Barbero** — Jose, Pedro, Luigi, Carlos o Cualquiera
3. **Fecha & Hora** — carrusel de días + grilla de horarios
4. **Datos de contacto** — nombre, apellido, teléfono (+569)
5. **Confirmación** — resumen completo + mensaje de fidelidad

### `/pages/club.html` — Mi Club
- Registro e inicio de sesión
- Sellos de fidelidad (10 por ciclo)
- Premios: Corte gratis (10), Barba gratis (20), Combo VIP (30)
- Niveles: 🥉 Bronce (1–9), 🥈 Plata (10–24), 🥇 Oro (25+)
- Lookbook de cortes

### `/pages/barbero.html` — Panel Barbero
- Login por nombre + contraseña (`1234` en demo)
- Vista de agenda individual
- Acciones: **Confirmar**, **Rechazar**, **Bloquear**, **Sellar**
- El sello suma puntos automáticamente al cliente en el club

### `/pages/admin.html` — Administrador
- Login: `admin` / `elegance2024`
- Tabla de clientes con ID único, nivel y visitas
- Resumen por barbero
- Config: número de sillas y horarios
- **Monitor de Anomalías**: detecta múltiples sellos en el mismo día

---

## Tecnologías
- HTML5 + CSS3 (sin frameworks)
- JavaScript vanilla (ES6+)
- `localStorage` para persistencia de datos en demo
- Google Fonts: Cormorant Garamond + DM Sans

---

## Deploy

Sube la carpeta completa a cualquier hosting estático:

```bash
# GitHub Pages
git init
git add .
git commit -m "feat: Elegance Barbershop v1.0"
git remote add origin https://github.com/tu-usuario/elegance-barbershop.git
git push -u origin main
# Activa GitHub Pages desde Settings > Pages > branch main
```

También compatible con **Netlify**, **Vercel**, o cualquier servidor web estático.

---

## Credenciales demo
| Rol | Usuario | Contraseña |
|-----|---------|-----------|
| Barbero | (cualquiera) | `1234` |
| Admin | `admin` | `elegance2024` |

---

## Roadmap sugerido
- [ ] Backend con Node.js / Supabase para persistencia real
- [ ] Notificaciones WhatsApp vía Twilio
- [ ] Autenticación segura con JWT
- [ ] Panel de estadísticas con gráficos
- [ ] App móvil con React Native o PWA

---

Desarrollado en Valparaíso con ☕ por **SinapTech Spa**
