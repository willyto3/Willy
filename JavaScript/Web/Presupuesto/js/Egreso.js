class Egreso extends Dato {
  // Variable Estatica
  static contadorEgreso = 0;

  // Constructor
  constructor(descripcion, valor) {
    super(descripcion, valor);
    this._id = ++Egreso.contadorEgreso;
  }

  // Metodos Get
  get id() {
    return this._id;
  }
}
