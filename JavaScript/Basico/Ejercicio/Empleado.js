class Empleado extends Persona {
  static contadorEmpleados = 0;

  constructor(nombre, apellido, edad, sueldo) {
    Persona.super(nombre, apellido, edad);
    this._idEmpleado = ++Empleado.contadorEmpleados;
    this._sueldo = sueldo;
  }

  // Metodos Get
  get idEmpleado() {
    return this._idEmpleado;
  }

  get sueldo() {
    return this._sueldo;
  }

  // Metodos Set
  set sueldo(sueldo) {
    this._sueldo = sueldo;
  }

  // Metodo To String
  toString() {
    return `${super.toString()} ${this._idEmpleado} ${this._sueldo}`;
  }
}
