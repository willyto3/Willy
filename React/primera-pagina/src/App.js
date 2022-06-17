import "./App.css";
import Testimonio from "./components/Testimonio";

function App() {
  return (
    <div className="App">
      <div className="contenedor-principal">
        <h1>Esto es lo que dicen nuestros alumnos sobre prueba</h1>
        <Testimonio
          nombre="Emma Bostian"
          pais="Suecia"
          imagen="portada-foto-perfil-redes-sociales-consejos"
          cargo="Ingeniera de Software"
          empresa="Spotify"
          testimonio="dkjdfd fdafkdjfidiaj ddjfkdjfiadjdif dfjadjkadjd djkfjadijfadijdkja djidjadjddj difdjfijdkad difjdifjakdfjdkjdkjfd"
        />
        <Testimonio
          nombre="Orlando Corzo"
          pais="Corronchilandia"
          imagen="images"
          cargo="Marica de Profesion"
          empresa="Puteadero"
          testimonio="dkjdfd fdafkdjfidiaj ddjfkdjfiadjdif dfjadjkadjd djkfjadijfadijdkja djidjadjddj difdjfijdkad difjdifjakdfjdkjdkjfd"
        />

        <Testimonio
          nombre="Willy Corzo"
          pais="Soledad"
          imagen="lindolindo"
          cargo="Loca Amateur"
          empresa="Peluqueria Cenit"
          testimonio="dkjdfd fdafkdjfidiaj ddjfkdjfiadjdif dfjadjkadjd djkfjadijfadijdkja djidjadjddj difdjfijdkad difjdifjakdfjdkjdkjfd"
        />
      </div>
    </div>
  );
}

export default App;
