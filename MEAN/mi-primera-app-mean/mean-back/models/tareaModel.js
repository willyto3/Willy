const { Schema, model } = require("mongoose");

const tarea = new Schema({
  nombre: {
    type: String,
    required: true,
    trim: true,
  },
  createdAt: {
    type: Date,
    default: Date.now(),
    required: true,
  },
  createdBy: {
    type: Schema.Types.ObjectId,
    trim: true,
    ref: "Usuario",
  },
});

module.exports = model("Tarea", tarea);
