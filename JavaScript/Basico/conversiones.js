let miNumero = "10";

console.log(miNumero);
console.log(typeof miNumero);

let edad = Number(miNumero);
console.log(edad);
console.log(typeof edad);

if (edad > 18) {
  console.log("Puede Votar");
} else {
  console.log("No Puede Votar");
}

// Con el Operador Ternario
resultado = edad > 18 ? "Puede Votar" : "No Puede Votar";
console.log(resultado);

// Mejora verificando si el dato ingresado es un numero
if (isNaN(edad)) {
  console.log("No Es Un Número");
} else {
  if (edad > 18) {
    console.log("Puede Votar");
  } else {
    console.log("No Puede Votar");
  }
}
