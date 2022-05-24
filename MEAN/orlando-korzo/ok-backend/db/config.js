const mongoose = require("mongoose");

const connectionDB = async () => {
  try {
    await mongoose.connect(process.env.CONNECTION_DB);
    console.log("Conectado a la base de datos");
  } catch (error) {
    console.log("Error al Conectar");
  }
};

module.exports = connectionDB;
