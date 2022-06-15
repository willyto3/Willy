import bcryptjs from "bcryptjs";
import jwt from "jsonwebtoken";
import { User } from "../models/user.model.js";

// REGISTER USER
export const registerUser = async (req, res) => {
  const { email, password, username, image } = req.body;
  console.log(email);

  try {
    let user = await User.findOne({ email });

    if (user) {
      return res.status(501).json({
        ok: false,
        msg: "Correo ya Registrado",
      });
    }

    const newUser = new User({ email, password, username, image });

    const salt = bcryptjs.genSaltSync(12);
    newUser.password = bcryptjs.hashSync(password, salt);

    await newUser.save();

    const payload = {
      id: newUser.id,
    };
    jwt.sign(
      payload,
      process.env.SECRET,
      { expiresIn: 36000 },
      (error, token) => {
        res.json({
          ok: true,
          id: newUser.id,
          email,
          username,
          msg: "Usuario Creado",
          token,
        });
      }
    );
  } catch (error) {
    res.json({ ok: false, msg: "Error al Registrar", error });
  }
};

// LOGIN USER
export const loginUser = async (req, res) => {
  const { email, password } = req.body;

  try {
    let user = await User.findOne({ email });

    if (!user) {
      return res.status(401).json({
        ok: false,
        msg: "Correo o Contraseña Invalida",
      });
    }

    const passwordValid = bcryptjs.compareSync(password, user.password);

    if (!passwordValid) {
      return res.status(401).json({
        ok: false,
        msg: "Correo o Contraseña Invalida",
      });
    }

    const payload = {
      id: user.id,
    };

    jwt.sign(
      payload,
      process.env.SECRET,
      { expiresIn: 36000 },
      (error, token) => {
        if (error) res.json({ error });
        res.json({
          ok: true,
          id: user.id,
          email,
          username: user.username,
          msg: "Inicio Sesion",
          token,
        });
      }
    );
  } catch (error) {
    res.json({ ok: false, msg: "Error al Hacer Login", error });
  }
};
