// Funcion Flecha para crear el reloj
const mostrarReloj = () => {

  // RELOJ
  let fecha = new Date();
  let hr = formatoHora(fecha.getHours());
  let min = formatoHora(fecha.getMinutes());
  let seg = formatoHora(fecha.getSeconds());
  document.getElementById("hora").innerHTML = `${hr}:${min}:${seg}`;

  // FECHA
  const meses = [
    "Enero",
    "Febrero",
    "Marzo",
    "Abril",
    "Mayo",
    "Junio",
    "Julio",
    "Agosto",
    "Septiembre",
    "Octubre",
    "Noviembre",
    "Diciembre",
  ];

  const dias = [
    "Lunes",
    "Martes",
    "Miercoles",
    "Jueves",
    "Viernes",
    "Sabado",
    "Domingo",
  ];

  let diaSemana = dias[fecha.getDay()];
  let dia = fecha.getDate();
  let mes = meses[fecha.getMonth()];
  let ano = fecha.getFullYear()

  document.getElementById("fecha").innerHTML = `${diaSemana}, ${dia} de ${mes} ${ano}` ;

  // ANIMACION AL CONTENEDOR
  // funcion toggle si esta aplicado lo quita y si no esta aplicado lo ejecuta
  document.getElementById("contenedor").classList.toggle("animar");
};

// Metodo para dar formatos
const formatoHora = (hora) => {
  if (hora < 10) hora = "0" + hora;
  return hora;
};

// Crear un intervalo para actualizar el reloj cada 1 segundo
setInterval(mostrarReloj, 1000);
