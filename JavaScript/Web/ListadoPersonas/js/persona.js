class Persona {
  // Construtor de la clase
  constructor(nombre, apellido) {
    this._nombre = nombre;
    this._apellido = apellido;
  }

  // Metodos Get
  get nombre() {
    return this._nombre;
  }

  get apellido() {
    return this._apellido;
  }

  // Metodos Set
  set nombre(nombre) {
    this._nombre = nombre;
  }

  set apellido(apellido) {
    this._apellido = apellido;
  }
}
