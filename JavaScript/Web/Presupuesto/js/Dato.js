class Dato {
  // Metodo Constructor
  constructor(descripcion, valor) {
    this._descripcion = descripcion;
    this._valor = valor;
  }

  // Metodos Get
  get descripcion() {
    return this._descripcion;
  }

  get valor() {
    return this._valor;
  }

  // Metodos Set
  set descripcion(descripcion) {
    this._descripcion = descripcion;
  }

  set valor(valor) {
    this._valor = valor;
  }
}