/* ============================================
   ELEGANCE BARBERSHOP — barbero.js
   ============================================ */

const DEMO_PASSWORD = '1234';

function barberLogin() {
  const barber = document.getElementById('barber-select').value;
  const pass = document.getElementById('barber-pass').value;
  if (!barber) { alert('Selecciona tu nombre.'); return; }
  if (pass !== DEMO_PASSWORD) { alert('Contraseña incorrecta. (Demo: 1234)'); return; }

  sessionStorage.setItem('eb_barber', barber);
  showPanel(barber);
}

function barberLogout() {
  sessionStorage.removeItem('eb_barber');
  document.getElementById('barber-panel').classList.add('hidden');
  document.getElementById('barber-login').classList.remove('hidden');
}

function showPanel(barber) {
  document.getElementById('barber-login').classList.add('hidden');
  document.getElementById('barber-panel').classList.remove('hidden');
  const names = { jose:'Jose', pedro:'Pedro', luigi:'Luigi', carlos:'Carlos' };
  document.getElementById('barber-panel-name').textContent = names[barber] || barber;
  renderAppointments(barber);
}

function getAppointments(barber) {
  const all = JSON.parse(localStorage.getItem('eb_bookings') || '[]');
  return all.filter(b => b.barber?.id === barber || b.barber?.id === 'cualquiera');
}

function updateAppointment(id, field, value) {
  const bookings = JSON.parse(localStorage.getItem('eb_bookings') || '[]');
  const idx = bookings.findIndex(b => b.id == id);
  if (idx !== -1) { bookings[idx][field] = value; localStorage.setItem('eb_bookings', JSON.stringify(bookings)); }
}

function sealClient(booking) {
  const users = JSON.parse(localStorage.getItem('eb_users') || '{}');
  const phone = '+569' + (booking.phone || '');
  const email = booking.email || '';
  for (const key in users) {
    if (users[key].name?.toLowerCase() === booking.name?.toLowerCase()) {
      users[key].stamps = (users[key].stamps || 0) + 1;
      users[key].visits = (users[key].visits || 0) + 1;
      const visits = users[key].visits;
      users[key].level = visits >= 25 ? 'Oro' : visits >= 10 ? 'Plata' : 'Bronce';
      localStorage.setItem('eb_users', JSON.stringify(users));
      return true;
    }
  }
  return false;
}

function renderAppointments(barber) {
  const list = document.getElementById('appointments-list');
  const bookings = getAppointments(barber);

  if (bookings.length === 0) {
    list.innerHTML = '<div class="empty-state">No hay citas registradas aún.</div>';
    return;
  }

  list.innerHTML = bookings.map(b => {
    const status = b.blocked ? 'blocked' : b.sealed ? 'sealed' : b.confirmed ? 'confirmed' : 'pending';
    const statusLabel = { blocked:'Bloqueado', sealed:'Sellado', confirmed:'Confirmado', pending:'Pendiente' }[status];
    return `
    <div class="appointment-card" id="appt-${b.id}">
      <div class="appt-header">
        <div>
          <div class="appt-client">${b.name || 'Sin nombre'} ${b.surname || ''}</div>
          <div class="appt-meta">${b.date || '—'} · ${b.time || '—'} · ${b.service?.name || '—'}</div>
          <div class="appt-meta">+569 ${b.phone || '—'}</div>
        </div>
        <div class="appt-status ${status}">${statusLabel}</div>
      </div>
      <div class="appt-actions">
        <button class="appt-btn confirm" onclick="confirmAppt(${b.id})" ${b.confirmed||b.blocked?'disabled':''}>Confirmar</button>
        <button class="appt-btn reject" onclick="rejectAppt(${b.id})" ${b.blocked?'disabled':''}>Rechazar</button>
        <button class="appt-btn block" onclick="blockAppt(${b.id})" ${b.blocked?'disabled':''}>Bloquear</button>
        <button class="appt-btn seal" onclick="sealAppt(${b.id})" ${b.sealed||b.blocked?'disabled':''}>Sellar</button>
      </div>
    </div>`;
  }).join('');
}

function confirmAppt(id) {
  updateAppointment(id, 'confirmed', true);
  renderAppointments(sessionStorage.getItem('eb_barber'));
}

function rejectAppt(id) {
  const bookings = JSON.parse(localStorage.getItem('eb_bookings') || '[]');
  const updated = bookings.filter(b => b.id != id);
  localStorage.setItem('eb_bookings', JSON.stringify(updated));
  renderAppointments(sessionStorage.getItem('eb_barber'));
}

function blockAppt(id) {
  updateAppointment(id, 'blocked', true);
  renderAppointments(sessionStorage.getItem('eb_barber'));
}

function sealAppt(id) {
  const bookings = JSON.parse(localStorage.getItem('eb_bookings') || '[]');
  const booking = bookings.find(b => b.id == id);
  if (booking) {
    const sealed = sealClient(booking);
    updateAppointment(id, 'sealed', true);
    alert(sealed ? `Sello registrado para ${booking.name}. ¡Gracias!` : `Cita sellada. Cliente no encontrado en el club.`);
    renderAppointments(sessionStorage.getItem('eb_barber'));
  }
}

window.addEventListener('DOMContentLoaded', () => {
  const barber = sessionStorage.getItem('eb_barber');
  if (barber) showPanel(barber);
});
