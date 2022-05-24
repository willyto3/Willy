// Sentencia Switch - La comparacion es estricta, se revisa el valor y el tipo

// Ejemplo 1
let numeroTexto = "Valor Desconocido";

switch (numero) {
  case 1:
    numeroTexto = "Número Uno";
    break;
  case 2:
    numeroTexto = "Número Dos";
    break;
  case 3:
    numeroTexto = "Número Tres";
    break;
  case 4:
    numeroTexto = "Número Cuatro";
    break;
  default:
    numeroTexto = "Caso No Encontrado";
}
console.log(numeroTexto);

// Ejemplo 2
let mes = 4;
let estacion = "Estacion Desconocida";

switch (numero) {
  case 1:
  case 2:
  case 12:
    estacion = "Invierno";
    break;
  case 3:
  case 4:
  case 5:
    estacion = "Primavera";
    break;
  case 6:
  case 7:
  case 8:
    estacion = "Verano";
    break;
  case 9:
  case 10:
  case 11:
    estacion = "Otoño";
    break;
  default:
    estacion = "Caso No Encontrado";
}
console.log(estacion);
