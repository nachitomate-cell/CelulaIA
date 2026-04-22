// firebase-config.js
// Mockup Mode: este archivo NO contiene credenciales reales del cliente.
// Pega aquí las llaves del nuevo proyecto Firebase de Elegance cuando estén listas.

const firebaseConfig = {
  apiKey: "TU_API_KEY_AQUI",
  authDomain: "TU_AUTH_DOMAIN_AQUI",
  projectId: "TU_PROJECT_ID_AQUI",
  storageBucket: "TU_STORAGE_BUCKET_AQUI",
  messagingSenderId: "TU_MESSAGING_SENDER_ID_AQUI",
  appId: "TU_APP_ID_AQUI",
  measurementId: "TU_MEASUREMENT_ID_AQUI"
};

window.FIREBASE_SETUP_TODO = `
1. Crear un proyecto Firebase nuevo y aislado para Elegance.
2. Reemplazar los valores placeholder de firebaseConfig.
3. Configurar Auth, Firestore y Storage con esas nuevas credenciales.
4. Cargar la cuenta de servicio del backend en backend/serviceAccountKey.json.
`;

if (typeof window !== "undefined") {
  window.MOCK_MODE = true;
}
