const personas = [
  new Persona("Willy", "Corzo"),
  new Persona("Paula", "Estrada"),
];

function mostrarPersonas() {
  let texto = "";
  for (persona of personas) {
    console.log(persona);
    texto += `<li>${persona.nombre} ${persona.apellido}`;
  }
  document.getElementById("personas").innerHTML = texto;
}

function agregarPersona() {
  const forma = document.forms["forma"];
  const nombre = forma["nombre"];
  const apellido = forma["apellido"];
  if(nombre.value !="" && apellido.value !=""){
    const persona = new Persona(nombre.value, apellido.value);
    personas.push(persona);
    mostrarPersonas();
  }else{
    alert("No hay Informacion de Nombre o Apellido")
  }

}
