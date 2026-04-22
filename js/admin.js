/* ============================================
   ELEGANCE BARBERSHOP — admin.js
   ============================================ */

const ADMIN_USER = 'admin';
const ADMIN_PASS = 'elegance2024';

function adminLogin() {
  const u = document.getElementById('admin-user').value;
  const p = document.getElementById('admin-pass').value;
  if (u === ADMIN_USER && p === ADMIN_PASS) {
    sessionStorage.setItem('eb_admin', '1');
    document.getElementById('admin-login').classList.add('hidden');
    document.getElementById('admin-panel').classList.remove('hidden');
    loadDashboard();
  } else {
    alert('Credenciales incorrectas.\n(Demo: admin / elegance2024)');
  }
}

function adminLogout() {
  sessionStorage.removeItem('eb_admin');
  location.reload();
}

function switchTab(tab) {
  document.querySelectorAll('.admin-tab').forEach(t => t.classList.remove('active'));
  document.querySelectorAll('.admin-section').forEach(s => s.classList.remove('active'));
  event.target.classList.add('active');
  document.getElementById('tab-' + tab).classList.add('active');
  if (tab === 'clientes') renderClients();
  if (tab === 'barberos') renderBarbers();
  if (tab === 'dev') renderDev();
}

function loadDashboard() {
  const users = JSON.parse(localStorage.getItem('eb_users') || '{}');
  const bookings = JSON.parse(localStorage.getItem('eb_bookings') || '[]');
  const config = JSON.parse(localStorage.getItem('eb_config') || '{"sillas":6}');

  document.getElementById('stat-registros').textContent = Object.keys(users).length;
  document.getElementById('stat-reservas').textContent = bookings.length;
  document.getElementById('stat-sillas').textContent = config.sillas || 6;
  document.getElementById('cfg-sillas').value = config.sillas || 6;

  renderClients();
}

function renderClients() {
  const users = JSON.parse(localStorage.getItem('eb_users') || '{}');
  const tbody = document.getElementById('clients-tbody');
  const entries = Object.entries(users);

  if (entries.length === 0) {
    tbody.innerHTML = '<tr><td colspan="6" style="text-align:center;color:var(--gray-500);padding:20px;">Sin registros aún.</td></tr>';
    return;
  }

  tbody.innerHTML = entries.map(([email, u], i) => {
    const levelBadge = {
      'Oro': '<span class="badge badge-gold">🥇 Oro</span>',
      'Plata': '<span class="badge badge-silver">🥈 Plata</span>',
      'Bronce': '<span class="badge badge-bronze">🥉 Bronce</span>'
    }[u.level] || u.level;
    return `<tr>
      <td style="font-family:var(--font-mono,monospace);font-size:11px;color:var(--gray-500);">ID${String(i+1).padStart(3,'0')}</td>
      <td>${u.name || '—'}</td>
      <td style="color:var(--gray-500);">${email}</td>
      <td>${levelBadge}</td>
      <td>${u.visits || 0}</td>
      <td>${u.stamps || 0}</td>
    </tr>`;
  }).join('');
}

function renderBarbers() {
  const bookings = JSON.parse(localStorage.getItem('eb_bookings') || '[]');
  const barbers = ['jose','pedro','luigi','carlos'];
  const names = { jose:'Jose', pedro:'Pedro', luigi:'Luigi', carlos:'Carlos' };
  const tbody = document.getElementById('barbers-tbody');

  tbody.innerHTML = barbers.map(id => {
    const mine = bookings.filter(b => b.barber?.id === id || b.barber?.id === 'cualquiera');
    const pending = mine.filter(b => !b.confirmed && !b.blocked && !b.sealed).length;
    const confirmed = mine.filter(b => b.confirmed && !b.sealed).length;
    const sealed = mine.filter(b => b.sealed).length;
    return `<tr>
      <td><strong>${names[id]}</strong></td>
      <td style="color:var(--warn);">${pending}</td>
      <td style="color:var(--info);">${confirmed}</td>
      <td style="color:var(--white);">${sealed}</td>
    </tr>`;
  }).join('');
}

function renderDev() {
  const users = JSON.parse(localStorage.getItem('eb_users') || '{}');
  const bookings = JSON.parse(localStorage.getItem('eb_bookings') || '[]');
  const today = new Date().toDateString();

  const todayBookings = bookings.filter(b => new Date(b.timestamp).toDateString() === today);
  const todaySeals = bookings.filter(b => b.sealed && new Date(b.timestamp).toDateString() === today);

  document.getElementById('dev-users').textContent = Object.keys(users).length;
  document.getElementById('dev-today').textContent = todayBookings.length;
  document.getElementById('dev-seals').textContent = todaySeals.length;

  // Anomaly detection: multiple seals same day same client
  const sealMap = {};
  bookings.filter(b => b.sealed).forEach(b => {
    const day = new Date(b.timestamp).toDateString();
    const key = `${b.name?.toLowerCase()}__${day}`;
    sealMap[key] = (sealMap[key] || 0) + 1;
  });

  const anomalies = Object.entries(sealMap).filter(([, count]) => count > 1);
  const box = document.getElementById('anomalies-list');

  if (anomalies.length === 0) {
    box.innerHTML = '<div class="anomaly-item" style="color:var(--gray-500);">Sin anomalías detectadas.</div>';
  } else {
    box.innerHTML = anomalies.map(([key, count]) => {
      const [name, day] = key.split('__');
      return `<div class="anomaly-item">⚠ ${count} sellos el mismo día para "${name}" (${day})</div>`;
    }).join('');
  }
}

function saveConfig() {
  const sillas = parseInt(document.getElementById('cfg-sillas').value) || 6;
  const open = document.getElementById('cfg-open').value;
  const close = document.getElementById('cfg-close').value;
  localStorage.setItem('eb_config', JSON.stringify({ sillas, open, close }));
  document.getElementById('stat-sillas').textContent = sillas;
}

window.addEventListener('DOMContentLoaded', () => {
  if (sessionStorage.getItem('eb_admin')) {
    document.getElementById('admin-login').classList.add('hidden');
    document.getElementById('admin-panel').classList.remove('hidden');
    loadDashboard();
  }
});
