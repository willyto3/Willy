// Funciones Normales
function miFuncion1() {
    console.log("Funcion 1");
}

function miFuncion2() {
    console.log("Funcion 2");
}

miFuncion1();
miFuncion2();

// Funciones de tipo CallBack
function imprimir(mensaje) {
    console.log(mensaje);
}

// Segunda forma
let imp = function imprimir(mensaje) {
    console.log(mensaje);
};

function sumar(op1, op2, funcionCallBack) {
    let res = op1 + op2;
    funcionCallBack(`Resultado: ${res}`);
}

sumar(5, 3, imprimir);

sumar(5, 3, imp);

// Llamadas asincronas con uso setTimeout

function miFuncionCallBack() {
    console.log("Saludo Asincrono despues de 3 segundos");
}

setTimeout(miFuncionCallBack, 3000);

// Pasando directamente la funcion
setTimeout(function () {
    console.log("Saludo Asincrono 2");
}, 4000);

// Usando la funcion Flecha
setTimeout(() => {
    console.log("Saludo Asincrono Flecha");
}, 5000);

// Settimer
let reloj = () => {
    let fecha = new Date();
    console.log(
        `${fecha.getHours()}:${fecha.getMinutes()}:${fecha.getSeconds()}`
    );
};

setInterval(reloj, 10000);
