// Una funcion es un codigo reutilizable que se puede llamar antes o despues de definirla

// Llamado antes de definir la funcion
miFuncion(2, 9);
miFuncion(6, 1);

//Declaracion de la funcion
function miFuncion(a, b) {
  console.log("Suma: " + (a + b));
}

// Llamado de la funcion despues de la funcion
miFuncion(1, 3);
miFuncion(8, 5);

// Regresas valores de las funciones
function miFuncion2(a, b) {
  //para conocer cuantos argumentos tiene una funcion
  console.log(arguments.length);
  return a + b;
}

let resultado = miFuncion2(5, 5);
console.log(resultado);

// Declaracion Funciones tipo Expresion o funciones anonimas, debe terminar en punto y coma
let sumar = function (a, b) {
  return a + b;
};

resultado = sumar(1, 2);
console.log(resultado);

//funcion anonima que se llama a si misma, no se puede reutilizar
(function () {
  console.log("Ejecutando la funcion" + (a + b));
})(3, 4);

// Funciones como objetos
var miFuncionTexto = miFuncion2.toString();
console.log(miFuncionTexto);

// Declaracion Funciones Flecha, al realizar la funcion de esta manera no se puede llamar antes de declarar la funcion
const sumarFuncionTipoFlecha = (a, b) => a + b;
resultado = sumarFuncionTipoFlecha(3, 5);
console.log(resultado);

// Asignar Valores por defecto de parametros en una funcion
let resta = function (a = 4, b = 1) {
  console.log(arguments[0]);
  console.log(arguments[1]);
  return a - b;
};

resultado = resta();
console.log(resultado);
resultado = resta(3, 2);
console.log(resultado);

// Paso por Valor
let x = 10;
function cambiarValor(a) {
  a = 20;
}
cambiarValor(x);
console.log(x);
console.log(a);

//Paso por referencia
const persona = {
  nombre: "Juan",
  apellido: "Perez",
};

function cambiarValorObjeto(p1) {
  p1.nombre = "Carlos";
  p1.apellido = "Rojas";
}

console.log(persona);
cambiarValorObjeto(persona);
console.log(persona);