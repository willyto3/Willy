class Cliente extends Persona {
  static contadorClientes = 0;

  constructor(nombre, apellido, edad, fechaRegistro) {
    Persona.super(nombre, apellido, edad);
    this._idCliente = ++Cliente.contadorClientes;
    this._fechaRegistro = fechaRegistro;
  }

  // Metodos Get
  get idCliente() {
    return this._idCliente;
  }

  get fechaRegistro() {
    return this._fechaRegistro;
  }

  // Metodos Set
  set fechaRegistro(fechaRegistro) {
    this._fechaRegistro = fechaRegistro;
  }

  // Metodo To String
  toString() {
    return `${super.toString()} ${this._idCliente} ${this._fechaRegistro}`;
  }
}
