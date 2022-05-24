"use strict";

class Monitor {
    static contadormonitores = 0;

    constructor(marca, tamano) {
        this._idMonitor = ++Monitor.contadormonitores;
        this._marca = marca;
        this._tamano = tamano;
    }

    // Metodos Get
    get idMonitor() {
        return this._idMonitor;
    }

    // Metodo toString
    toString() {
        return `Monitor: [idMonitor: ${this._idMonitor}, Marca: ${this._marca}, Tamaño: ${this._tamano}]`;
    }
}
