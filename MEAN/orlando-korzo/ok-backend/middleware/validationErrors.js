import { validationResult } from "express-validator";

export const validationErrors = (req, res, next) => {
  const errors = validationResult(req);
  if (!errors.isEmpty()) {
    return res.status(501).json({
      ok: false,
      errors: errors.mapped(),
    });
  }

  next();
};
