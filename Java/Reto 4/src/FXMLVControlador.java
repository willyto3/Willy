
import java.net.URL;
import java.util.ResourceBundle;

import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.control.Button;
import javafx.scene.control.TextArea;
import javafx.scene.control.TextField;

public class FXMLVControlador implements Initializable {

    @FXML
    private ResourceBundle resources;

    @FXML
    private URL location;

    @FXML
    private Button btnGuardar;

    @FXML
    private TextField txtNombre;

    @FXML
    private TextField txtNota;

    @FXML
    private TextField txtMateria;

    @FXML
    private TextField txtGenero;

    @FXML
    private TextField txtNombre2;

    @FXML
    private TextField txtMateria2;

    @FXML
    private TextArea txtAProcesar;

    @FXML
    private TextArea txtACargar;

    @FXML
    private TextArea txtAConsultar;

    @FXML
    private Button btnCargar;

    @FXML
    private Button btnProcesar;

    @FXML
    private Button btnConsultar;

    @FXML
    private Button btnEliminar;

    @FXML
    void guardar(ActionEvent event) {
        String nombre = txtNombre.getText();
        String nota = txtNota.getText();
        String materia = txtMateria.getText();
        String genero = txtGenero.getText();

        Consulta.Guardar(nombre, genero, materia, nota);
    }

    @FXML
    void cargar(ActionEvent event) {
        txtACargar.clear();
        String listado = Consulta.Cargar();
        txtACargar.setText(listado);
    }

    @FXML
    void consultar(ActionEvent event) {
        String nombre = txtNombre2.getText();
        String materia = txtMateria2.getText();
        String listado;

        if (nombre.isEmpty()) {

            Integer llamado = 2;
            listado = Consulta.Consultar(materia, llamado);

        } else {

            Integer llamado = 1;
            listado = Consulta.Consultar(nombre, llamado);

        }

        if (listado.isEmpty()) {

            txtAConsultar.setText("No se Encontraron Resultados");
        } else {
            txtAConsultar.setText(listado);
        }
    }

    @FXML
    void eliminar(ActionEvent event) {
        String nombre = txtNombre2.getText();
        String materia = txtMateria2.getText();
        int cuenta = 0;

        if (nombre.isEmpty()) {

            Integer llamado = 2;
            cuenta = Consulta.Eliminar(materia, llamado);

        } else {

            Integer llamado = 1;
            cuenta = Consulta.Eliminar(nombre, llamado);

        }

        if (cuenta == 0) {

            txtAConsultar.setText("No se Encontraron Resultados");
        } else {
            txtAConsultar.setText("Se eliminaron los registros");
        }

    }

    @FXML
    void procesar(ActionEvent event) {

        String cuadroTexto = txtACargar.getText();

        // Se llama el metodo readData
        SchoolGradingSystem.loadData(cuadroTexto);

        // Se llama los metodos y se muestran en pantalla
        String texto = String.valueOf(SchoolGradingSystem.stat1()) + "\n" + String.valueOf(SchoolGradingSystem.stat2())
                + "\n" + SchoolGradingSystem.stat3() + "\n" + SchoolGradingSystem.stat4();

        txtAProcesar.setText(texto);
    }

    @Override
    public void initialize(URL url, ResourceBundle resources) {
        // TODO Auto-generated method stub

    }

}
