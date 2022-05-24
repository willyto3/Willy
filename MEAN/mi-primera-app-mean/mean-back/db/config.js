const mongoose = require("mongoose");

const conexionDB = async () => {
  try {
    await mongoose.connect(process.env.DB_CONEXION);
    console.log("Conectado a la base de datos");
  } catch (error) {
    console.log("Error al Conectar");
  }
};

module.exports = conexionDB;
