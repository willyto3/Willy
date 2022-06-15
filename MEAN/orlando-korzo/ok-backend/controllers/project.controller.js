// Importations
import { Project } from "../models/project.model.js";
import { Category } from "../models/category.model.js";

// GET PROJECTS LIST
export const getProject = async (req, res) => {
  try {
    const projectList = await Project.find().populate("category");

    if (projectList.length == 0) {
      return res.status(500).json({
        ok: false,
        msg: "No hay Proyectos registrados",
      });
    }
    return res
      .status(200)
      .json({ ok: true, msg: "Hay Proyectos registrados", projectList });
  } catch (error) {
    res.json({ ok: false, msg: "Error al Buscar" });
  }
};

// REGISTER PROJECT
export const registerProject = async (req, res) => {
  const { name, description, image, images, categoryName } = req.body;
  const id = req.uid;

  const categorySearch = await Category.findOne({ categoryName: categoryName });

  if (!categorySearch)
    return res.status(404).json({ ok: false, msg: "Categoria Invalida" });

  try {
    const project = await Project.findOne({ name });

    if (project) {
      return res.status(501).json({
        ok: false,
        msg: "Proyecto ya Registrada",
      });
    }

    const newProject = new Project({
      name,
      description,
      image,
      images,
      category: categorySearch.id,
      createdBy: id,
    });

    await newProject.save();
    res.status(200).json({ ok: true, msg: "Project Created", newProject });
  } catch (error) {
    res.json({ ok: false, msg: "Error al Registrar", error });
  }
};

// DELETE PROJECT
export const deleteProject = async (req, res) => {
  const { name } = req.body;

  try {
    const project = await Project.findOneAndRemove({ name });
    return res.status(200).json({ ok: true, msg: "Proyecto Eliminado" });
  } catch (error) {
    res.status(404).json({ ok: false, msg: "Error al Eliminar", error });
  }
};

// UPDATE PROJECT
export const updateProject = async (req, res) => {
  const { id } = req.params;
  const { name, description, image, images, dateCreated, category } = req.body;

  try {
    const project = await Project.findByIdAndUpdate(
      id,
      { name, description, image, images, dateCreated, category },
      { new: true }
    );
    return res
      .status(200)
      .json({ ok: true, msg: "Proyecto Actualizado", project });
  } catch (error) {
    res.status(404).json({ ok: false, msg: "Error al Actualizar", error });
  }
};
