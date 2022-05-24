"use strict";

class Raton extends DispositivoEntrada {
    static contadorRatones = 0;

    constructor(tipoEntrada, marca) {
        super(tipoEntrada, marca);
        this._idRaton = ++Raton.contadorRatones;
    }
    // Metodos Get
    get idRaton() {
        return this._idRaton;
    }
    // Metodo toString
    toString() {
        return `Raton: [idRaton: ${this._idRaton}, Tipo Entrada: ${this._tipoEntrada}, Marca: ${this._marca}]`;
    }
}
