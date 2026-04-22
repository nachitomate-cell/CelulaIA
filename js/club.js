/* ============================================
   ELEGANCE BARBERSHOP — club.js
   ============================================ */

let currentUser = null;

function switchAuth(mode) {
  document.querySelectorAll('.auth-tab').forEach((t, i) => t.classList.toggle('active', (mode === 'register' && i === 0) || (mode === 'login' && i === 1)));
  document.getElementById('form-register').classList.toggle('active', mode === 'register');
  document.getElementById('form-login').classList.toggle('active', mode === 'login');
}

function registerUser() {
  const name = document.getElementById('reg-name').value.trim();
  const email = document.getElementById('reg-email').value.trim();
  const pass = document.getElementById('reg-pass').value;
  if (!name || !email || !pass) { alert('Completa todos los campos.'); return; }

  const users = JSON.parse(localStorage.getItem('eb_users') || '{}');
  if (users[email]) { alert('Ya existe una cuenta con ese email. Inicia sesión.'); return; }

  const user = { name, email, stamps: 0, visits: 0, level: 'Bronce', joined: new Date().toISOString() };
  users[email] = user;
  localStorage.setItem('eb_users', JSON.stringify(users));
  localStorage.setItem('eb_current', email);

  currentUser = user;
  showDashboard();
}

function loginUser() {
  const email = document.getElementById('log-email').value.trim();
  if (!email) { alert('Ingresa tu email.'); return; }

  const users = JSON.parse(localStorage.getItem('eb_users') || '{}');
  if (!users[email]) { alert('No encontramos esa cuenta. Regístrate primero.'); return; }

  localStorage.setItem('eb_current', email);
  currentUser = users[email];
  showDashboard();
}

function showDashboard() {
  document.getElementById('auth-section').classList.add('hidden');
  document.getElementById('club-dashboard').classList.remove('hidden');
  renderDashboard();
}

function renderDashboard() {
  if (!currentUser) return;

  document.getElementById('profile-name').textContent = currentUser.name;
  document.getElementById('profile-visits').textContent = currentUser.visits;

  const badge = document.getElementById('profile-badge');
  const level = getLevel(currentUser.visits);
  badge.className = 'badge badge-' + level.key;
  badge.textContent = level.icon + ' ' + level.name;

  const stamps = currentUser.stamps % 10;
  const row = document.getElementById('stamps-row');
  row.innerHTML = '';
  for (let i = 0; i < 10; i++) {
    const s = document.createElement('div');
    s.className = 'stamp' + (i < stamps ? ' filled' : '');
    s.textContent = i < stamps ? '★' : '○';
    row.appendChild(s);
  }
  document.getElementById('stamp-count').textContent = `${stamps}/10 sellos para Premio ${Math.floor(currentUser.stamps / 10) + 1}`;

  updatePrize('prize-1', currentUser.stamps >= 10);
  updatePrize('prize-2', currentUser.stamps >= 20);
  updatePrize('prize-3', currentUser.stamps >= 30);
}

function updatePrize(id, unlocked) {
  const el = document.getElementById(id);
  const status = el.querySelector('.prize-status');
  if (unlocked) {
    el.classList.add('unlocked');
    status.classList.add('unlocked');
    status.classList.remove('locked');
    status.textContent = '¡Disponible!';
  }
}

function getLevel(visits) {
  if (visits >= 25) return { key: 'gold', name: 'Oro', icon: '🥇' };
  if (visits >= 10) return { key: 'silver', name: 'Plata', icon: '🥈' };
  return { key: 'bronze', name: 'Bronce', icon: '🥉' };
}

// Auto-login if session exists
window.addEventListener('DOMContentLoaded', () => {
  const email = localStorage.getItem('eb_current');
  if (email) {
    const users = JSON.parse(localStorage.getItem('eb_users') || '{}');
    if (users[email]) {
      currentUser = users[email];
      showDashboard();
    }
  }
});
