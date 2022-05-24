let miPromesa = new Promise((resolver, rechazar) => {
    let expresion = false;
    if (expresion) resolver("Resolvio Correto");
    else rechazar("Se produjo un error");
});

miPromesa.then(
    (valor) => console.log(valor),
    (error) => console.log(error)
);

miPromesa
    .then((valor) => console.log(valor))
    .catch((error) => console.log(error));

let promesa = new Promise((resolver) => {
    setTimeout(() => resolver("Saludos con promesa y timeout"), 3000);
});

promesa.then((valor) => console.log(valor));

// Async indica que una funcion regresa una promesa
async function miFuncionConPromesa() {
    return "Saludos con Promesa y Async";
}

miFuncionConPromesa().then((valor) => console.log(valor));

// Asinc con Await
async function funcionConPromesaYAwait() {
    let miPromesa2 = new Promise((resolver) => {
        resolver("Promesa con Await");
    });
    console.log(await miPromesa2);
}

funcionConPromesaYAwait();

// Promesas, await, async y setTimeout
async function funcionConPromesaAwaitTimeout() {
    let miPromesa3 = new Promise((resolver) => {
        setTimeout(() => resolver("Promesa con Await y timeout"), 3000);
    });
    console.log(await miPromesa3);
}

funcionConPromesaAwaitTimeout();
