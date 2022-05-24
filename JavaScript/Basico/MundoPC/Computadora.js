"use strict";

class Computadora {
    static contadorComputadora = 0;

    constructor(nombre, monitor, raton, teclado) {
        this._idComputadora = ++Computadora.contadorComputadora;
        this._nombre = nombre;
        this._monitor = monitor;
        this._raton = raton;
        this._teclado = teclado;
    }

    // Metodo toString
    toString() {
        return `Computadora ${this._idComputadora}: ${this._nombre} \n ${this._raton} \n ${this._teclado}`;
    }
}
