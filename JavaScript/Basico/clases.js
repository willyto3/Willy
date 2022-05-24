class Persona {
  // Variables estaticas
  static contadorPersonas = 0; // Atributos de nuestra clases
  email = "Valor Default email"; // Atributos de nuestros objetos

  // Constante estaticas
  static get MAX_OBJ() {
    return 5;
  }

  //Metodo Constructor
  constructor(nombre, apellido) {
    this._nombre = nombre;
    this._apellido = apellido;
    if (Persona.contadorPersonas < Persona.MAX_OBJ) {
      this._id = ++Persona.contadorPersonas;
    } else {
      console.log("Se ha Superado el mayor número de Personas");
    }
  }
  // Metodo Get
  get nombre() {
    return this._nombre;
  }
  get apellido() {
    return this._apellido;
  }

  // Metodo Set
  set nombre(nombre) {
    this._nombre = nombre;
  }

  set apellido(apellido) {
    this._apellido = apellido;
  }

  // Metodo diferente
  nombreCompleto() {
    return this._id + " " + this._nombre + " " + this._apellido;
  }

  // sobre escribimos el metodo to String de Object
  toString() {
    return this.nombreCompleto();
  }
}

// Crear una clase Hija
class Empleado extends Persona {
  constructor(nombre, apellido, departamento) {
    super(nombre, apellido); // llamar al constructor de la clase padre
    this._departamento = departamento;
  }
  // Metodo Get
  get departamento() {
    this._departamento = departamento;
  }
  // Metodo Set
  set departamento(departamento) {
    this._departamento = departamento;
  }
  // Sobre Escritura de Metodo
  nombreCompleto() {
    return (
      super.nombreCompleto() +
      " y trabaja en el Departamento " +
      this._departamento
    );
  }

  // Metodo Estatico
  static saludar() {
    console.log("Saludos desde metodo estatico");
  }

  static saludar2(persona) {
    console.log("Saludos desde metodo Estatico " + persona.nombre);
  }
}

let persona1 = new Persona("Willy", "Corzo");
console.log(persona1);

let persona2 = new Persona("Juan", "Lopez");
console.log(persona2);

// Accediendo por el metodo Get
console.log(persona1.nombre);

// Cambiando datos por metodo Set
persona1.nombre = "Juan Carlos";
console.log(persona1.nombre);

// Creamos un empleado
let empleado1 = new Empleado("Maria", "Jimenez", "Sistemas");
console.log(empleado1);
console.log(empleado1.nombre); // Podemos acceder a los metodos de la clase padre

// Acceder al metodo de la clase padre
console.log(empleado1.nombreCompleto());

// Imprimiendo el metodo to string POLIMORFISMO (Multiples formas en tiempo de Ejecucion)
console.log(persona1.toString());
console.log(empleado1.toString());

// Ejecutando metodo estatico - Se asocian con la clase no con los objetos
persona1.saludar(); // No se puede llamar un metodo estatico desde un objeto
Persona.saludar();

Persona.saludar2(persona1);

Empleado.saludar();
Empleado.saludar2(empleado1);

// Variable Estatica
console.log(persona1.contadorObjetosPersonas); // No se puede llamar una variables estatica desde un objeto
console.log(Persona.contadorObjetosPersonas);
console.log(Empleado.contadorObjetosPersonas);

// Variable no estatica
console.log(persona1.email);
console.log(empleado1.email);
console.log(Persona.email); // se crea una nueva variable
console.log(Empleado.email); // se crea una nueva variable

console.log(Persona.MAX_OBJ);
