const { Router } = require("express");
const { check } = require("express-validator");
const { registerUsuario } = require("../controllers/authController");
const { loginUsuario } = require("../controllers/authController");
const validationErrors = require("../middlewares/validationErrors");

const authRouter = Router();

authRouter.post(
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
  registerUsuario
);
authRouter.post(
  "/login",
  [
    check("email", "El Formato es Invalido").isEmail(),
    check(
      "password",
      "La contraseña debe ser de 6 caracteres como minimo"
    ).isLength({ min: 6 }),
    validationErrors,
  ],
  loginUsuario
);

module.exports = authRouter;
