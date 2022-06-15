// Requisites
import "dotenv/config";

//Importations
// Dependencies
import express from "express";
import cors from "cors";
import morgan from"morgan";
// Services
const api = process.env.API_URL;
import "./db/config.js";

// Routes
import userRouter from "./routes/user.routes.js";
import projectRouter from "./routes/project.routes.js";
import categoryRouter from "./routes/category.routes.js";

// Start app
const app = express();

//FIXME Esta pendiente arreglar esta parte
//app.use("/", express.static(__dirname + "/public"));

// Middleware
app.use(express.json());
app.use(morgan("tiny"));
app.use(cors());

// Routes
app.use(`${api}/user`, userRouter);
app.use(`${api}/category`, categoryRouter);
app.use(`${api}/project`, projectRouter);

// Start app
app.listen(process.env.PORT || 5000, () => {
  console.log(`App Running in port ${process.env.PORT}`);
});
