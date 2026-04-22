// backend/firebase-admin.js
// Reemplaza "path/to/serviceAccountKey.json" por la ruta real del nuevo proyecto Elegance.

var admin = require("firebase-admin");
var serviceAccount = require("path/to/serviceAccountKey.json");
admin.initializeApp({
  credential: admin.credential.cert(serviceAccount)
});
