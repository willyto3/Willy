import React from "react";
import "../stylesheets/Testimonio.css"

function Testimonio(props) {
  return (
      <div className="contenedor-testimonio">
        <img
          className="imagen-testimonio"
          src={require(`../images/${props.imagen}.jpg`)}
          alt="Imagen de Perfil"
        />
        <div className="contenedor-texto-testimonio">
          <p className="nombre-testimonio">{props.nombre} de {props.pais}</p>
          <p className="cargo-testimonio">{props.cargo} en {props.empresa}</p>
          <p className="texto-testimonio">"{props.testimonio}"</p>
        </div>
      </div>
  );
}

export default Testimonio;
