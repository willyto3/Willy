"use strict";

class Teclado extends DispositivoEntrada {
    static contadorTeclados = 0;

    constructor(tipoEntrada, marca) {
        super(tipoEntrada, marca);
        this._idTeclado = ++Teclado.contadorTeclados;
    }
    // Metodos Get
    get idTeclado() {
        return this._idTeclado;
    }
    // Metodo toString
    toString() {
        return `Teclado: [idTeclado: ${this._idTeclado}, Tipo Entrada: ${this._tipoEntrada}, Marca: ${this._marca}]`;
    }
}
