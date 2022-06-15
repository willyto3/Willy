import jwt from "jsonwebtoken";

export const verifyToken = (req, res, next) => {
  const token = req.header("x-auth-token");
  if (!token) {
    res.status(401).json({
      ok: false,
      msg: "Token no Valido",
    });
  }

  try {
    const payload = jwt.verify(token, process.env.SECRET);
    req.uid = payload.id;

    next();
  } catch (error) {
    res.status(401).json({
      ok: false,
      msg: "Token no Valido",
    });
  }
};
