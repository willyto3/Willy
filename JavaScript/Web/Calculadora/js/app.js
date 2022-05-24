console.log("Aplicacion Calculadora");

function sumar() {
  const formulario = document.getElementById("formulario");
  let operandoA = formulario["operandoA"];
  let operandoB = formulario["operandoB"];
  let resultado = parseInt(operandoA.value) + parseInt(operandoB.value);
  if (isNaN(resultado)) {
    document.getElementById("resultado").innerHTML =
      "Por favor introduzca los números";
  } else {
    document.getElementById(
      "resultado"
    ).innerHTML = `El Resultado de la Suma es ${resultado}`;
  }
}
