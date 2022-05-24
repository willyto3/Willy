"use strict";

class DispositivoEntrada {
    constructor(tipoEntrada, marca) {
        this._tipoEntrada = tipoEntrada;
        this._marca = marca;
    }
    // Metodos Get
    get tipoEntrada() {
        return this._tipoEntrada;
    }

    get marca() {
        return this._marca;
    }

    // Metodos Set
    set tipoEntrada(tipoEntrada) {
        this._tipoEntrada = tipoEntrada;
    }
    set marca(marca) {
        this._marca = marca;
    }
}
