// Importations
import { Router } from "express";
import { check } from "express-validator";
import {
  registerProject,
  getProject,
  updateProject,
  deleteProject,
} from "../controllers/project.controller.js";
import { validationErrors } from "../middleware/validationErrors.js";
import { verifyToken } from "../middleware/verifyToken.js";

const projectRouter = Router();

// GET PROJECTS
projectRouter.get("/get", getProject);

// REGISTER PROJECT
projectRouter.post(
  "/register",
  [
    check("name", "Nombre del Proyecto obligatorio").not().isEmpty(),
    check("description", "Se requiere una descripcion del Proyecto")
      .not()
      .isEmpty(),
    check("image", "Se requiere una imagen del Proyecto").not().isEmpty(),
    validationErrors,
    verifyToken,
  ],
  registerProject
);

// UPDATE PROJECT
projectRouter.put(
  "/update/:id",
  [
    check("name", "Nombre del Proyecto obligatorio").not().isEmpty(),
    validationErrors,
    verifyToken,
  ],
  updateProject
);

// DELETE PROJECT
projectRouter.delete("/delete/:id", [verifyToken], deleteProject);

export default projectRouter;
