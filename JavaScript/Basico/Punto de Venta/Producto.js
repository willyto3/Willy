class Producto {
  static contadorProducto = 0;

  constructor(nombre, precio) {
    this._idProducto = ++Producto.contadorProducto;
    this._nombre = nombre;
    this._precio = precio;
  }

  // Metodos Get
  get idProducto() {
    return this._idProducto;
  }

  get nombre() {
    return this._nombre;
  }

  get precio() {
    return this._precio;
  }

  // Metodos Set
  set nombre(nombre) {
    this._nombre = nombre;
  }

  set precio(precio) {
    this._precio = precio;
  }

  // Metodo to String
  toString() {
    return `idProducto: ${this._idProducto}, nombre: ${this._nombre}, precio: $ ${this._precio}`;
  }
}
