// config.js
// Plantilla base para nuevos clientes.
// Este clon queda preparado en Mockup Mode para una demo aislada.

const SHOP = {
  nombre: "Elegance Barbershop",
  nombreCorto: "ELEGANCE",
  slogan: "CORTES PREMIUM",
  direccion: "Ecuador 243 | Viña del Mar",
  horario: "Lunes-Sáb: 10-20h | Dom: 12-20h",
  telefono: "56900000000",
  club: "Club Elegance",
  repoName: "plantilla",
  infoHeadline: "𝐄𝐥𝐞𝐠𝐚𝐧𝐜𝐞 𝐛𝐚𝐫𝐛𝐞𝐫𝐬𝐡𝐨𝐩 | Cortes premium.",
  infoAddress: "📍 Ecuador 243 | Viña del Mar",
  infoHours: "🕒 Lunes-Sáb: 10-20h | Dom: 12-20h. ¡Reserva ya! #EleganceBarbershop"
};

const DEMO_SERVICES = [
  { id: "srv-premium", nombre: "Corte Premium", precio: 15000, duracion: 60, categoria: "Cortes", descripcion: "Corte de precisión y acabado premium." },
  { id: "srv-fade", nombre: "Corte Degradado", precio: 15000, duracion: 60, categoria: "Cortes", descripcion: "Fade limpio con acabado nítido." },
  { id: "srv-tijera", nombre: "Corte con Tijera", precio: 15000, duracion: 45, categoria: "Cortes", descripcion: "Trabajo clásico y textura controlada." },
  { id: "srv-combo", nombre: "Corte + Barba", precio: 20000, duracion: 90, categoria: "Combos", descripcion: "Experiencia completa de alto contraste." },
  { id: "srv-combo-premium", nombre: "Corte + Barba Premium", precio: 23000, duracion: 80, categoria: "Combos", descripcion: "Diseño integral con toalla caliente." },
  { id: "srv-barba-premium", nombre: "Barba Premium", precio: 10000, duracion: 30, categoria: "Barba", descripcion: "Afeitado con vapor y toalla caliente." },
  { id: "srv-barba", nombre: "Barba Simple", precio: 8000, duracion: 20, categoria: "Barba", descripcion: "Perfilado rápido y limpio." },
  { id: "srv-spa", nombre: "Spa Facial", precio: 12000, duracion: 45, categoria: "Extras", descripcion: "Limpieza facial de presentación." }
];

const DEMO_BARBERS = [
  { id: "barber-any", nombre: "Cualquier Barbero", subtitulo: "Disponible antes" },
  { id: "barber-carlos", nombre: "Carlos", subtitulo: "Especialista en fades" },
  { id: "barber-david", nombre: "David", subtitulo: "Barba y perfilado" }
];

const DEMO_REWARDS = [
  { id: "reward-1", nombre: "Lavado premium", costoSellos: 3 },
  { id: "reward-2", nombre: "Perfilado de barba", costoSellos: 6 },
  { id: "reward-3", nombre: "Corte gratis", costoSellos: 10 }
];

const MOCK_MODE = true;
