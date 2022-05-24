//FIXME Se debe colocar los comentarios

const express = require("express");
const app = express();
require("dotenv/config");
const api = process.env.API_URL;
const morgan = require("morgan");
const connectionDB = require("./db/config");

connectionDB();

// Middleware
app.use(express.json());
app.use(morgan("tiny"));

app.get(`${api}/projects`, (req, res) => {
  const project = {
    id: 1,
    nombre: "Prueba",
    image: "cualquier_url",
  };
  res.send(project);
});

app.post(`${api}/projects`, (req, res) => {
  const newProject = req.body;
  console.log(newProject);
  res.send(newProject);
});

app.listen(3000, () => {
  console.log(api);
  console.log(`Aplicacion Corriendo en el puerto 3000`);
});
