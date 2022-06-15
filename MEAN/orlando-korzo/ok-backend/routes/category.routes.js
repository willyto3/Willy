// Importations
import { Router } from "express";
import { check } from "express-validator";
import { validationErrors } from "../middleware/validationErrors.js";
import { verifyToken } from "../middleware/verifyToken.js";
import {
  registerCategory,
  getCategory,
  deleteCategory,
  updateCategory,
} from "../controllers/category.controller.js";

const categoryRouter = Router();

// GET CATEGORIES
categoryRouter.get("/get", getCategory);

// REGISTER CATEGORY
categoryRouter.post(
  "/register",
  [
    check("categoryName", "El nombre de la categoria es requerido").not().isEmpty(),
    validationErrors,
    verifyToken,
  ],
  registerCategory
);

// DELETE CATEGORY
categoryRouter.post(
  "/delete",
  [
    check("category", "El nombre de la categoria es requerido").not().isEmpty(),
    validationErrors,
    verifyToken,
  ],
  deleteCategory
);

// UPDATE CATEGORY
categoryRouter.put(
  "/update/:id",
  [
    check("category", "El nombre de la categoria es requerido").not().isEmpty(),
    validationErrors,
    verifyToken,
  ],
  updateCategory
);

export default categoryRouter;
