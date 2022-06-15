// Importations
import { Category } from "../models/category.model.js";

// GET CATEGORY LIST
export const getCategory = async (req, res) => {
  try {
    const categoryList = await Category.find();

    if (categoryList.length == 0) {
      return res.status(500).json({
        ok: false,
        msg: "No hay categorias registradas",
      });
    }
    return res
      .status(200)
      .json({ ok: true, msg: "Hay categorias registradas", categoryList });
  } catch (error) {
    res.json({ ok: false, msg: "Error al Buscar", error });
  }
};

// REGISTER CATEGORY
export const registerCategory = async (req, res) => {
  const { categoryName, icon, color, image } = req.body;

  try {
    const category = await Category.findOne({ categoryName });

    if (category) {
      return res.status(501).json({
        ok: false,
        msg: "Categoria ya Registrada",
      });
    }

    const id = req.uid;
    const newCategory = new Category({
      categoryName,
      icon,
      color,
      image,
      createdBy: id,
    });

    await newCategory.save();
    res.status(200).json({ ok: true, msg: "Category Created", newCategory });
  } catch (error) {
    res.json({ ok: false, msg: "Error al Registrar" });
  }
};

// DELETE CATEGORY
export const deleteCategory = async (req, res) => {
  const { categoryName } = req.body;

  try {
    const category = await Category.findOneAndRemove({ categoryName });
    return res.status(200).json({ ok: true, msg: "Categoria Eliminada" });
  } catch (error) {
    res.status(404).json({ ok: false, msg: "Error al Eliminar", error });
  }
};

// UPDATE CATEGORY
export const updateCategory = async (req, res) => {
  const { id } = req.params;
  const { categoryName, icon, color, image } = req.body;

  try {
    const category = await Category.findByIdAndUpdate(
      id,
      { categoryName, icon, color, image },
      { new: true }
    );
    return res
      .status(200)
      .json({ ok: true, msg: "Categoria Actualizada", category });
  } catch (error) {
    res.status(404).json({ ok: false, msg: "Error al Actualizar", error });
  }
};
