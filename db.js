// db.js
// Demo datastore basado en localStorage para presentar la maqueta sin backend activo.

(function () {
  const KEYS = {
    services: "elegance_demo_services",
    barbers: "elegance_demo_barbers",
    rewards: "elegance_demo_rewards",
    bookings: "elegance_demo_bookings",
    users: "elegance_demo_users",
    currentUser: "elegance_demo_current_user"
  };

  const SETTINGS = {
    weekdayStart: "10:00",
    sundayStart: "12:00",
    end: "20:00",
    interval: 30
  };

  function read(key, fallback) {
    try {
      const raw = localStorage.getItem(key);
      return raw ? JSON.parse(raw) : fallback;
    } catch (_) {
      return fallback;
    }
  }

  function write(key, value) {
    localStorage.setItem(key, JSON.stringify(value));
  }

  function toMinutes(time) {
    const [h, m] = time.split(":").map(Number);
    return h * 60 + m;
  }

  function toTime(total) {
    const h = String(Math.floor(total / 60)).padStart(2, "0");
    const m = String(total % 60).padStart(2, "0");
    return `${h}:${m}`;
  }

  function formatCurrency(value) {
    return new Intl.NumberFormat("es-CL", {
      style: "currency",
      currency: "CLP",
      maximumFractionDigits: 0
    }).format(value);
  }

  function getToday() {
    const now = new Date();
    return new Date(now.getFullYear(), now.getMonth(), now.getDate());
  }

  function isoDate(date) {
    const y = date.getFullYear();
    const m = String(date.getMonth() + 1).padStart(2, "0");
    const d = String(date.getDate()).padStart(2, "0");
    return `${y}-${m}-${d}`;
  }

  function ensureSeed() {
    if (!localStorage.getItem(KEYS.services)) write(KEYS.services, DEMO_SERVICES);
    if (!localStorage.getItem(KEYS.barbers)) write(KEYS.barbers, DEMO_BARBERS);
    if (!localStorage.getItem(KEYS.rewards)) write(KEYS.rewards, DEMO_REWARDS);
    if (!localStorage.getItem(KEYS.users)) {
      write(KEYS.users, [
        {
          id: "guest-demo",
          nombre: "Invitado Elegance",
          email: "demo@elegance.local",
          telefono: "+56 9 0000 0000",
          password: "demo123",
          stamps: 4
        }
      ]);
    }
    if (!localStorage.getItem(KEYS.currentUser)) {
      write(KEYS.currentUser, { id: "guest-demo" });
    }
    if (!localStorage.getItem(KEYS.bookings)) {
      const today = getToday();
      const tomorrow = new Date(today);
      tomorrow.setDate(today.getDate() + 1);
      write(KEYS.bookings, [
        {
          id: "bk-1",
          fecha: isoDate(today),
          hora: "10:00",
          clienteNombre: "Martín Soto",
          clienteTelefono: "+56 9 1111 1111",
          clienteEmail: "martin@example.com",
          servicioId: "srv-premium",
          servicioNombre: "Corte Premium",
          duracionServicio: 60,
          precioServicio: 15000,
          barbero: "Carlos",
          estado: "Confirmada",
          nota: "Cliente frecuente"
        },
        {
          id: "bk-2",
          fecha: isoDate(today),
          hora: "11:30",
          clienteNombre: "Joaquín Díaz",
          clienteTelefono: "+56 9 2222 2222",
          clienteEmail: "joaquin@example.com",
          servicioId: "srv-barba",
          servicioNombre: "Perfilado de Barba",
          duracionServicio: 30,
          precioServicio: 8000,
          barbero: "David",
          estado: "Pendiente",
          nota: ""
        },
        {
          id: "bk-3",
          fecha: isoDate(tomorrow),
          hora: "12:00",
          clienteNombre: "Álvaro Pérez",
          clienteTelefono: "+56 9 3333 3333",
          clienteEmail: "alvaro@example.com",
          servicioId: "srv-combo",
          servicioNombre: "Corte + Barba",
          duracionServicio: 90,
          precioServicio: 20000,
          barbero: "Carlos",
          estado: "Confirmada",
          nota: ""
        }
      ]);
    }
  }

  function getServices() {
    return read(KEYS.services, DEMO_SERVICES);
  }

  function getBarbers() {
    return read(KEYS.barbers, DEMO_BARBERS);
  }

  function getRewards() {
    return read(KEYS.rewards, DEMO_REWARDS);
  }

  function getBookings() {
    return read(KEYS.bookings, []);
  }

  function saveBookings(bookings) {
    write(KEYS.bookings, bookings);
  }

  function getBookingsByDate(date) {
    return getBookings()
      .filter((booking) => booking.fecha === date)
      .sort((a, b) => a.hora.localeCompare(b.hora));
  }

  function getBookingsByBarberAndDate(date, barberName) {
    return getBookingsByDate(date).filter((booking) => booking.barbero === barberName);
  }

  function getWorkingHours(dateString) {
    const date = new Date(`${dateString}T12:00:00`);
    const isSunday = date.getDay() === 0;
    return {
      start: isSunday ? SETTINGS.sundayStart : SETTINGS.weekdayStart,
      end: SETTINGS.end
    };
  }

  function getAvailableHours(dateString, duration, barberName) {
    const hours = getWorkingHours(dateString);
    const start = toMinutes(hours.start);
    const end = toMinutes(hours.end);
    const bookings = getBookingsByDate(dateString)
      .filter((booking) => {
        if (barberName === "Cualquier Barbero") return true;
        return booking.barbero === barberName;
      })
      .filter((booking) => booking.estado !== "Cancelada");

    const slots = [];
    for (let cursor = start; cursor + duration <= end; cursor += SETTINGS.interval) {
      const occupied = bookings.some((booking) => {
        const bookingStart = toMinutes(booking.hora);
        const bookingEnd = bookingStart + Number(booking.duracionServicio || 30);
        return cursor < bookingEnd && cursor + duration > bookingStart;
      });

      slots.push({
        time: toTime(cursor),
        occupied
      });
    }

    return slots;
  }

  function saveBooking(payload) {
    const bookings = getBookings();
    const booking = {
      id: `bk-${Date.now()}`,
      estado: "Confirmada",
      nota: "",
      ...payload
    };
    bookings.push(booking);
    saveBookings(bookings);
    return booking;
  }

  function updateBookingStatus(id, estado) {
    const bookings = getBookings().map((booking) =>
      booking.id === id ? { ...booking, estado } : booking
    );
    saveBookings(bookings);
  }

  function upsertUser(profile) {
    const users = read(KEYS.users, []);
    const existing = users.find((user) => user.email === profile.email);
    const nextUser = existing
      ? { ...existing, ...profile }
      : {
          id: `usr-${Date.now()}`,
          stamps: 0,
          ...profile
        };

    const nextUsers = existing
      ? users.map((user) => (user.email === profile.email ? nextUser : user))
      : [...users, nextUser];

    write(KEYS.users, nextUsers);
    write(KEYS.currentUser, { id: nextUser.id });
    return nextUser;
  }

  function login(email, password) {
    const users = read(KEYS.users, []);
    const match = users.find((user) => user.email === email && user.password === password);
    if (!match) return null;
    write(KEYS.currentUser, { id: match.id });
    return match;
  }

  function getCurrentUser() {
    const current = read(KEYS.currentUser, null);
    const users = read(KEYS.users, []);
    return users.find((user) => user.id === current?.id) || users[0] || null;
  }

  function logout() {
    write(KEYS.currentUser, { id: "guest-demo" });
  }

  function stampUser(email, amount) {
    const users = read(KEYS.users, []).map((user) =>
      user.email === email ? { ...user, stamps: Math.max(0, Number(user.stamps || 0) + amount) } : user
    );
    write(KEYS.users, users);
  }

  ensureSeed();

  window.DemoDB = {
    formatCurrency,
    getServices,
    getBarbers,
    getRewards,
    getBookings,
    getBookingsByDate,
    getBookingsByBarberAndDate,
    getAvailableHours,
    getWorkingHours,
    saveBooking,
    updateBookingStatus,
    upsertUser,
    login,
    logout,
    getCurrentUser,
    stampUser,
    isoDate
  };
})();
