const ingresos = [
  new Ingreso("Salario", 3000000),
  new Ingreso("venta Coche", 4000000),
  new Ingreso("Alquiler", 1000000),
];

const egresos = [
  new Egreso("Luz", 500000),
  new Egreso("Agua", 2000000),
  new Egreso("Internet", 5000000),
];

let cargarApp = () => {
  cargarCabecero();
  cargarIngreso();
  cargarEgreso();
};

let totalIngresos = () => {
  let totalIngresos = 0;
  for (let ingreso of ingresos) {
    totalIngresos += ingreso.valor;
  }
  return totalIngresos;
};

let totalEgresos = () => {
  let totalEgresos = 0;
  for (let egreso of egresos) {
    totalEgresos += egreso.valor;
  }
  return totalEgresos;
};

let cargarCabecero = () => {
  let presupuesto = totalIngresos() - totalEgresos();
  let porcentajeEgreso = totalEgresos() / totalIngresos();
  document.getElementById("presupuesto").innerHTML = formatoMoneda(presupuesto);
  document.getElementById("porcentaje").innerHTML =
    formatoPorcentaje(porcentajeEgreso);
  document.getElementById("ingresos").innerHTML = formatoMoneda(
    totalIngresos()
  );
  document.getElementById("egresos").innerHTML = formatoMoneda(totalEgresos());
};

const formatoMoneda = (valor) => {
  return valor.toLocaleString("en-US", {
    style: "currency",
    currency: "USD",
    minimumFractionDigits: 0,
  });
};

const formatoPorcentaje = (valor) => {
  return valor.toLocaleString("en-US", {
    style: "percent",
    minimumFractionDigits: 2,
  });
};

// INGRESOS

const cargarIngreso = () => {
  let ingresosHTML = "";
  for (let ingreso of ingresos) {
    ingresosHTML += crearIngresoHTML(ingreso);
  }
  document.getElementById("lista-ingresos").innerHTML = ingresosHTML;
};

const crearIngresoHTML = (ingreso) => {
  let ingresoHTML = `
    <div class="elemento limpiarEstilos">
      <div class="elemento_descripcion">${ingreso.descripcion}</div>
      <div class="derecha limpiarEstilos">
        <div class="elemento_valor">${formatoMoneda(ingreso.valor)}</div>
        <div class="elemento_eliminar">
          <button class="elemento_eliminar--btn">
            <ion-icon name="close-circle-outline" onclick="eliminarIngreso(${
              ingreso.id
            })"></ion-icon>
          </button>
        </div>
      </div>
    </div>
  `;
  return ingresoHTML;
};

const eliminarIngreso = (id) => {
  let indiceEliminar = ingresos.findIndex((ingreso) => ingreso.id === id);
  ingresos.splice(indiceEliminar, 1);
  cargarCabecero();
  cargarIngreso();
};

// EGRESOS

const cargarEgreso = () => {
  let egresosHTML = "";
  for (let egreso of egresos) {
    egresosHTML += crearEgresoHTML(egreso);
  }
  document.getElementById("lista-egresos").innerHTML = egresosHTML;
};

const crearEgresoHTML = (egreso) => {
  let egresoHTML = `
    <div class="elemento limpiarEstilos">
      <div class="elemento_descripcion">${egreso.descripcion}</div>
      <div class="derecha limpiarEstilos">
        <div class="elemento_valor">- ${formatoMoneda(egreso.valor)}</div>
        <div class="elemento_porcentaje">${formatoPorcentaje(
          egreso.valor / totalEgresos()
        )}</div>
        <div class="elemento_eliminar">
          <button class="elemento_eliminar--btn">
            <ion-icon name="close-circle-outline" onclick="eliminarEgreso(${
              egreso.id
            })"></ion-icon>
          </button>
        </div>
      </div>
    </div>
  `;
  return egresoHTML;
};

const eliminarEgreso = (id) => {
  let indiceEliminar = egresos.findIndex((egreso) => egreso.id === id);
  egresos.splice(indiceEliminar, 1);
  cargarCabecero();
  cargarEgreso();
};

let agregarDato = () => {
  let formulario = document.forms["formulario"];
  let tipo = formulario["tipo"];
  let descripcion = formulario["descripcion"];
  let valor = formulario["valor"];

  if (descripcion.value !== "" && valor.value !== "") {
    if (tipo.value === "ingreso") {
      ingresos.push(new Ingreso(descripcion.value, +valor.value));
      cargarCabecero();
      cargarIngreso();
    } else if (tipo.value === "egreso") {
      egresos.push(new Egreso(descripcion.value, +valor.value));
      cargarCabecero();
      cargarEgreso();
    }
  }
};
