// Declarar Arreglos
let autos = new Array("BMW", "Mercedes Benz", "Volvo"); // Descontinuado
console.log(autos);
const frutas = ["Pera", "Piña", "Fresas"];
console.log(frutas);

// Metodo de acceder a un solo elemento
console.log(autos[0]);
console.log(frutas[1]);

// Conocer el tamaño de un arreglo
console.log(frutas.length);

// Conocer si estamos trabajando con un arreglo
console.log(Array.isArray(frutas));
console.log(frutas instanceof Array);

// Recorrer un arreglo con un ciclo for
for (let i = 0; i < frutas.length; i++) {
  console.log(frutas[i]);
}

// Modificar un elemento en un arreglo
frutas[1] = "Papaya";
autos[2] = "Chevrolet";

// Agregar un nuevo elemento al final del arreglo
autos.push("Audi");
frutas.push("Patilla");
autos[autos.length]= "Cadillac";
frutas[frutas.length]="Kiwi";

