// Importations
import { Router } from "express";
import { check } from "express-validator";
import { registerUser, loginUser } from "../controllers/user.controller.js";
import { validationErrors } from "../middleware/validationErrors.js";

const userRouter = Router();

// REGISTER USER
userRouter.post(
  "/register",
  [
    check("email", "El Formato es Invalido").isEmail(),
    check(
      "password",
      "La contraseña debe ser de 6 caracteres como minimo"
    ).isLength({ min: 6 }),
    check("username", "El nombre de usuario es requerido").not().isEmpty(),
    validationErrors,
  ],
  registerUser
);

// LOGIN USER
userRouter.post(
  "/login",
  [
    check("email", "El Formato es Invalido").isEmail(),
    check(
      "password",
      "La contraseña debe ser de 6 caracteres como minimo"
    ).isLength({ min: 6 }),
    validationErrors,
  ],
  loginUser
);

export default userRouter;
