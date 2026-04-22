// firebaseUtils.js
// Wrapper compatible en modo demo. Cuando Firebase real esté listo,
// estas funciones pueden reconectarse a Firestore sin cambiar la UI.

window.FDB = {
  async getServicios() {
    return DemoDB.getServices();
  },
  async getConfig() {
    return {
      horarioInicio: "10:00",
      horarioFin: "20:00",
      intervaloMinutos: 30,
      telefonoAdmin: SHOP.telefono
    };
  },
  async getCitas(fecha) {
    return DemoDB.getBookingsByDate(fecha);
  },
  async addCita(cita) {
    return DemoDB.saveBooking(cita);
  },
  async getPremios() {
    return DemoDB.getRewards();
  }
};
