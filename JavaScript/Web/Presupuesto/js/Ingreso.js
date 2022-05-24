class Ingreso extends Dato {
  // Variable Estatica
  static contadorIngreso = 0;

  // Constructor
  constructor(descripcion, valor) {
    super(descripcion, valor);
    this._id = ++Ingreso.contadorIngreso;
  }

  // Metodos Get
  get id(){
    return this._id;
  }
}
