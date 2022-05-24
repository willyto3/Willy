let a = 3,
  b = 2,
  c = 1;

// Suma
let z = a + b;
console.log("El resultado de la suma es: " + z);

// Resta
z = a - b;
console.log("El resultado de la resta es: " + z);

// Multiplicacion
z = a * b;
console.log("El resultado de la multiplicacion es: " + z);

// Division
z = a / b;
console.log("El resultado de la division es: " + z);

// Modulo - Residuo
z = a % b;
console.log("El resultado del modulo es: " + z);

// Exponente
z = a ** b;
console.log("El resultado del exponente es: " + z);

// Incremento
//Pre-Incremento (el operador ++ antes de la variable)
z = ++a;
console.log(z);
console.log(a);

//Post-Incremento (el operador ++ despues de la variable)
z = b++;
console.log(b);
console.log(z);

// Decremento
//Pre-Decremento (el operador -- antes de la variable)
z = --a;
console.log(z);
console.log(a);

//Post-Decremento (el operador ++ despues de la variable)
z = b--;
console.log(b);
console.log(z);

// Operadores de Asignacion
a += 3; // a =a+3
console.log(a);

a -= 3; // a =a-3
console.log(a);

a *= 3; // a =a*3
console.log(a);

a /= 3; // a =a/3
console.log(a);

// Operadores de Comparacion
// Igualdad - Se revisa el valor sin importar el tipo
z = a == b;
console.log(z);

// Igualdad Estricta - Se revisa el valor y el tipo
z = a === b;
console.log(z);

// Distinto - Se revisa el valor sin importar el tipo
z = a != b;
console.log(z);

// Distinto - Se revisa el valor y el tipo
z = a !== b;
console.log(z);

// Menor
z = a < b;
console.log(z);

// Menor igual
z = a <= b;
console.log(z);

// Mayor
z = a > b;
console.log(z);

// Mayor igual
z = a >= b;
console.log(z);

// Operador AND (&&), Regresa True si todas las condiciones son verdaderas
let valMin = 0,
  valMax = 10;

if (a >= valMin && a <= valMax) {
  console.log("Dentro de Rango");
} else {
  console.log("Fuera de Rango");
}

// Operador OR (||), Regresa True si cualquier condicion es verdadera
let vacaciones = false,
  diaDescanso = false;

if (vacaciones || diaDescanso) {
  console.log("Padre puede asistir al juego");
} else {
  console.log("Padre esta en el trabajo");
}

// Operador Ternario
let resultado = 3 > 2 ? "verdadero" : "falso";
console.log(resultado);

let numero = 9;
resultado = numero % 2 == 0 ? "Número Par" : "Número Impar";
console.log(resultado);
