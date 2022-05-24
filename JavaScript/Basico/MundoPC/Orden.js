"use strict";

class Orden {
    static contadorOrdenes = 0;

    constructor() {
        this._idOrden = ++Orden.contadorOrdenes;
        this._computadoras = [];
    }

    // Metodos Get
    get idOrden() {
        return this._idOrden;
    }

    // Metodo Agregar Computadora
    agregarComputadora(computadora) {
        this._computadoras.push(computadora);
    }

    // Metodo Mostrar Orden
    mostarOrden() {
        let computadorasOrden = "";
        for (let computadora of this._computadoras) {
            computadorasOrden += `\n ${computadora}`;
        }
        console.log(
            `Orden: ${this._idOrden}, Computadoras: ${computadorasOrden}`
        );
    }
}
