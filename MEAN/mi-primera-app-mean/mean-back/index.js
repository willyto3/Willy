require("dotenv").config();

const express = require("express");
const cors = require("cors");
const { default: mongoose } = require("mongoose");
const conexionDB = require("./db/config");
const authRouter = require("./routes/authRouter");
const taskRouter = require("./routes/tareasRouter");
const app = express();

conexionDB();

app.use(express.json());
app.use(cors());

app.use("/", express.static(__dirname + "/public"));

app.use("/auth", authRouter);
app.use("/task", taskRouter);

app.listen(process.env.PORT, () => {
  console.log(`Aplicacion Corriendo en el puerto ${process.env.PORT}`);
});
