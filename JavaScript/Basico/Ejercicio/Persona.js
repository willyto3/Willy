class Persona {
  static contadorPersonas = 0;

  constructor(nombre, apellido, edad) {
    this._idPersona = ++Persona.contadorPersonas;
    this._nombre = nombre;
    this._apellido = apellido;
    this._edad = edad;
  }

  // Metodos Get
  get idPersona() {
    return this._idPersona;
  }
  get nombre() {
    return this._nombre;
  }

  get apellido() {
    return this._apellido;
  }

  get edad() {
    return this._edad;
  }
  // Metodos Set
  set nombre(nombre) {
    this._nombre = nombre;
  }

  set apellido(apellido) {
    this._apellido = apellido;
  }

  set edad(edad) {
    this._edad = edad;
  }

  toString() {
    console.log(
      `${this._idPersona} ${this._nombre} ${this._apellido} ${this._edad}`
    );
  }
}
