let persona = {
  nombre: "Juan",
  apellido: "Perez",
  email: "jperez@correo.com",
  edad: 28,
  nombreCompleto: function () {
    return this.nombre + " " + this.apellido;
  },
};

console.log(persona.nombre);
console.log(persona.apellido);
console.log(persona.email);
console.log(persona.edad);
console.log(persona.nombreCompleto());

console.log(persona);

// Creacion de un objeto vacio
let persona2 = new Object();
persona2.nombre = "Carlos";
persona2.nombre = "Muñoz";
persona2.direccion = "Villavicencio";
persona2.tel = "3407805";

console.log(persona2.tel);

// otra forma de acceder a propiedades de un objeto
console.log(persona.nombre);
console.log(persona["nombre"]);

// Ciclo para recorrer las propiedades de un objeto
for (nombrePropiedad in persona) {
  console.log(nombrePropiedad);
  console.log(persona[nombrePropiedad]);
}

// agregar propiedades a objetos
persona.tel = "3407805";
console.log(persona);

//Eliminar propiedades a objetos
delete persona.tel;
console.log(persona);

//Formas de imprimir un objeto
// En Consola
console.log(persona);

// Concatenar cada valor con cada propiedad
console.log(persona.nombre + ", " + persona.apellido);

// for in
for (nombrePropiedad in persona) {
  console.log(persona[nombrePropiedad]);
}

// Como objeto
let personaArray = Object.values(persona);
console.log(personaArray);

// Con JSON
let personaString = JSON.stringify(persona);
console.log(personaString);

// Metodo Get y Set
let persona3 = {
  nombre: "Juan",
  apellido: "Perez",
  email: "jperez@correo.com",
  edad: 28,
  idioma: "es",
  get lang() {
    return this.idioma.toUpperCase();
  },
  set lang(lang) {
    this.idioma = lang.toUpperCase();
  },
  get nombreCompleto() {
    return this.nombre + " " + this.apellido;
  },
};

console.log(persona3.nombreCompleto);
console.log(persona3.lang);
persona3.lang = "en";
console.log(persona3.lang);

// Uso de call para usar un metodo de otro objeto
console.log(persona.nombreCompleto());
console.log(persona.nombreCompleto.call(persona2));


