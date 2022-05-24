const Tarea = require("../models/tareaModel");

const createTarea = async (req, res) => {
  const { nombre } = req.body;
  const id = req.uid;
  const nuevaTarea = new Tarea({ nombre, createdBy: id });

  await nuevaTarea.save();

  res.status(200).json({
    ok: true,
    msg: "Tarea Creada",
    nuevaTarea,
  });
};

const readTarea = async (req, res) => {
  const id = req.uid;

  try {
    const tareas = await Tarea.find({
      createdBy: id,
    }).sort({ createdAt: -1 });

    return res.status(200).json({
      ok: true,
      tareas,
    });
  } catch (error) {
    res.status(404).json({
      ok: false,
      msg: "Tareas no Encontradas",
    });
  }
};

const updateTarea = async (req, res) => {
  const { id } = req.params;
  const { nombre } = req.body;

  try {
    const tarea = await Tarea.findByIdAndUpdate(id, { nombre }, { new: true });

    return res.status(200).json({
      ok: true,
      tarea,
    });
  } catch (error) {
    res.status(404).json({
      ok: false,
      msg: "Tarea no Actualizada",
      error,
    });
  }
};

const deleteTarea = async (req, res) => {
  const { id } = req.params;

  try {
    const tarea = await Tarea.findByIdAndRemove(id);

    return res.status(200).json({
      ok: true,
      msg: "Tarea Eliminada",
    });
  } catch (error) {
    res.status(404).json({
      ok: false,
      msg: "Tarea no Encontrada",
      error,
    });
  }
};

module.exports = { createTarea, readTarea, updateTarea, deleteTarea };
