/* ============================================
   ELEGANCE BARBERSHOP — booking.js
   ============================================ */

const state = {
  service: null,
  barber: null,
  date: null,
  time: null,
  name: '',
  surname: '',
  phone: ''
};

// ── Step Navigation ─────────────────────────
let currentStep = 1;

function goToStep(n) {
  document.querySelectorAll('.booking-step').forEach(s => s.classList.remove('active'));
  document.querySelectorAll('.step').forEach((s, i) => {
    s.classList.remove('active', 'done');
    if (i + 1 < n) s.classList.add('done');
    if (i + 1 === n) s.classList.add('active');
  });
  document.getElementById('step-' + n).classList.add('active');
  currentStep = n;
  window.scrollTo({ top: 0, behavior: 'smooth' });
}

// ── Step 1: Services ─────────────────────────
document.querySelectorAll('.service-card').forEach(card => {
  card.addEventListener('click', () => {
    document.querySelectorAll('.service-card').forEach(c => c.classList.remove('selected'));
    card.classList.add('selected');
    state.service = { id: card.dataset.id, name: card.dataset.name, price: card.dataset.price };
    document.getElementById('step1-next').disabled = false;
  });
});

document.getElementById('step1-next').addEventListener('click', () => goToStep(2));

// ── Step 2: Barber ───────────────────────────
document.querySelectorAll('.barber-card').forEach(card => {
  card.addEventListener('click', () => {
    document.querySelectorAll('.barber-card').forEach(c => c.classList.remove('selected'));
    card.classList.add('selected');
    state.barber = { id: card.dataset.id, name: card.dataset.name };
    document.getElementById('step2-next').disabled = false;
  });
});

document.getElementById('step2-next').addEventListener('click', () => {
  buildDateCarousel();
  buildTimeGrid();
  goToStep(3);
});

// ── Step 3: Date & Time ──────────────────────
function buildDateCarousel() {
  const container = document.getElementById('date-carousel');
  container.innerHTML = '';
  const today = new Date();
  const days = ['Dom','Lun','Mar','Mié','Jue','Vie','Sáb'];
  const months = ['Ene','Feb','Mar','Abr','May','Jun','Jul','Ago','Sep','Oct','Nov','Dic'];

  for (let i = 0; i < 10; i++) {
    const d = new Date(today);
    d.setDate(today.getDate() + i);
    if (d.getDay() === 0) continue; // closed Sundays

    const pill = document.createElement('div');
    pill.className = 'date-pill';
    pill.innerHTML = `<div class="date-day">${days[d.getDay()]} ${months[d.getMonth()]}</div><div class="date-num">${d.getDate()}</div>`;
    pill.addEventListener('click', () => {
      document.querySelectorAll('.date-pill').forEach(p => p.classList.remove('selected'));
      pill.classList.add('selected');
      state.date = `${days[d.getDay()]} ${d.getDate()} ${months[d.getMonth()]}`;
      checkStep3();
    });
    container.appendChild(pill);
  }
}

function buildTimeGrid() {
  const container = document.getElementById('time-grid');
  container.innerHTML = '';
  const slots = ['09:00','09:30','10:00','10:30','11:00','11:30','12:00','12:30',
                  '14:00','14:30','15:00','15:30','16:00','16:30','17:00','17:30'];

  slots.forEach(t => {
    const slot = document.createElement('div');
    slot.className = 'time-slot';
    slot.textContent = t;
    slot.addEventListener('click', () => {
      if (slot.classList.contains('unavailable')) return;
      document.querySelectorAll('.time-slot').forEach(s => s.classList.remove('selected'));
      slot.classList.add('selected');
      state.time = t;
      checkStep3();
    });
    container.appendChild(slot);
  });
}

function checkStep3() {
  document.getElementById('step3-next').disabled = !(state.date && state.time);
}

document.getElementById('step3-next').addEventListener('click', () => goToStep(4));

// ── Step 4: Contact ──────────────────────────
document.getElementById('step4-next').addEventListener('click', () => {
  state.name = document.getElementById('contact-name').value.trim();
  state.surname = document.getElementById('contact-surname').value.trim();
  state.phone = document.getElementById('contact-phone').value.trim();

  if (!state.name || !state.phone) {
    alert('Por favor completa nombre y teléfono.');
    return;
  }

  buildConfirmation();
  goToStep(5);
  saveBooking();
});

// ── Step 5: Confirmation ─────────────────────
function buildConfirmation() {
  document.getElementById('confirm-name').textContent = state.name;
  document.getElementById('confirm-datetime').textContent = `${state.date} · ${state.time}`;
  document.getElementById('confirm-service').textContent = `${state.service.name} — $${parseInt(state.service.price).toLocaleString('es-CL')}`;
  document.getElementById('confirm-barber').textContent = `Barbero: ${state.barber.name}`;
}

// ── Local storage persistence ────────────────
function saveBooking() {
  const bookings = JSON.parse(localStorage.getItem('eb_bookings') || '[]');
  bookings.push({ ...state, id: Date.now(), timestamp: new Date().toISOString() });
  localStorage.setItem('eb_bookings', JSON.stringify(bookings));
}

// ── Tab filtering (services) ─────────────────
document.querySelectorAll('.tab').forEach(tab => {
  tab.addEventListener('click', () => {
    document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
    tab.classList.add('active');
    const cat = tab.dataset.category;
    document.querySelectorAll('.service-card').forEach(card => {
      const cardCat = card.dataset.category || 'cortes';
      card.style.display = (cat === 'cortes' && !card.dataset.category) || cardCat === cat ? '' : 'none';
    });
  });
});
