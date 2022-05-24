// Funcion Constructor de Objetos
function Persona(nombre, apellido, email) {
  this.nombre = nombre;
  this.apellido = apellido;
  this.email = email;
  // agregar un metodo
  this.nombreCompleto = function () {
    return this.nombre + " " + this.apellido;
  };
}

// se crea un objeto tipo persona
let padre = new Persona("Juan", "Perez", "jperez@correo.com");
console.log(padre);

let madre = new Persona("Paula", "Hoyos", "phoyos@correo.com");
console.log(madre);

// llamado del metodo
console.log(padre.nombreCompleto());
console.log(madre.nombreCompleto());

// modificar un valor en un objeto
padre.nombre = "Carlos";
console.log(padre);
console.log(madre);

// distintas formas de crear objetos
let miObjeto = new Object();
let miObjeto2 = {};

// agregar una propiedad a nuestra funcion
Persona.prototype.tel="3407805";
console.log(padre);
console.log(madre);

// modificando la propiedad
padre.tel = "3017893883";
console.log(padre);
console.log(madre);
