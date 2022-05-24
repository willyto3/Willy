const bcryptjs = require("bcryptjs");
const jwt = require("jsonwebtoken");
const {validationResult} = require("express-validator")
const usuarioModel = require("../models/usuarioModel");

const registerUsuario = async (req, res) => {




  const { email, password, username } = req.body;

  try {
    let usuario = await usuarioModel.findOne({ email });

    if (usuario) {
      return res.status(501).json({
        ok: false,
        msg: "Correo ya Registrado",
      });
    }

    const nuevoUsuario = new usuarioModel({ email, password, username });

    const salt = bcryptjs.genSaltSync(12);
    nuevoUsuario.password = bcryptjs.hashSync(password, salt);

    await nuevoUsuario.save();

    const payload = {
      id: nuevoUsuario.id,
    };
    jwt.sign(
      payload,
      process.env.SECRETA,
      { expiresIn: 36000 },
      (error, token) => {
        res.json({
          ok: true,
          id: nuevoUsuario.id,
          email,
          username,
          msg: "Usuario Creado",
          token,
        });
      }
    );
  } catch (error) {
    res.json({ ok: false, msg: "Error al Registrar" });
  }
};

const loginUsuario = async (req, res) => {
  const { email, password } = req.body;

  try {
    let usuario = await usuarioModel.findOne({ email });

    if (!usuario) {
      return res.status(401).json({
        ok: false,
        msg: "Correo o Contraseña Invalida",
      });
    }

    const passwordValido = bcryptjs.compareSync(password, usuario.password);

    if (!passwordValido) {
      return res.status(401).json({
        ok: false,
        msg: "Correo o Contraseña Invalida",
      });
    }

    const payload = {
      id: usuario.id,
    };

    jwt.sign(
      payload,
      process.env.SECRETA,
      { expiresIn: 3600 },
      (error, token) => {
        if (error) res.json({error})
        res.json({
          ok: true,
          id: usuario.id,
          email,
          username: usuario.username,
          msg: "Inicio Sesion",
          token,
        });
      }
    );
  } catch (error) {
    res.json({ ok: false, msg: "Error al Hacer Login" });
  }
};

module.exports = { loginUsuario, registerUsuario };
