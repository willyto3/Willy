package col.com.willy.corzo;

import java.net.URL;
import java.sql.Connection;
import java.sql.DriverManager;

import javax.swing.JOptionPane;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.stage.Stage;

//WILLY CORZO

// Reto 3 Curso Programacion Basica MINTIC - Universidad del Norte

// Iniciamos la clase App
public class App extends Application {
    // Clase principal MAIN

    @Override
    public void start(Stage stage) throws Exception {

        Class.forName("org.sqlite.JDBC");
        conexion();
        // TODO Auto-generated method stub
        URL url = getClass().getClassLoader().getResource("GUI.fxml");
        FXMLLoader fxmlloader = new FXMLLoader(url);

        Parent root = fxmlloader.load();
        Scene scene = new Scene(root);

        stage.setTitle("SISTEMA ESTADISTICO");
        stage.setScene(scene);
        stage.show();
    }

    public static void main(String[] args) throws Exception {
        launch(args);

    }

    public static Connection conexion() {
        String url = "jdbc:sqlite: BaseDatos.db";
        Connection conn = null;

        try {
            conn = DriverManager.getConnection(url);
            JOptionPane.showMessageDialog(null, "Conexion a base de datos establecida", "Conexion",
                    JOptionPane.INFORMATION_MESSAGE);
        } catch (Exception e) {
            // TODO: handle exception
            JOptionPane.showMessageDialog(null, "se cago la Conexion a base de datos establecida", "Conexion",
                    JOptionPane.INFORMATION_MESSAGE);
            e.printStackTrace();
        }
        return conn;
    }
}
