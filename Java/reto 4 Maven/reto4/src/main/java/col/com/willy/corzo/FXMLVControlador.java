package col.com.willy.corzo;

import java.net.URL;
import java.util.ResourceBundle;

import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.control.Button;
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

        SchoolGradingSystem.loadData(nombre, nota, materia, genero);
    }

    @FXML
    void cargar(ActionEvent event) {
        System.out.print("PRUEBA");
    }

    @FXML
    void consultar(ActionEvent event) {
        System.out.println("PRUEBA");
    }

    @FXML
    void eliminar(ActionEvent event) {
        System.out.println("PRUEBA");
    }

    @FXML
    void procesar(ActionEvent event) {
        System.out.println("PRUEBA");
    }

    @Override
    public void initialize(URL url, ResourceBundle resources) {
        // TODO Auto-generated method stub

    }

}
