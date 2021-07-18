package principal;

import java.sql.*;
import javax.swing.*;

/**
 *
 * @author Sony
 */

public class conectar {

    Connection conect = null;

    public Connection conexion() {
        try {
            Class.forName("com.mysql.jdbc.Driver");
            conect = DriverManager.getConnection("jdbc:mysql://localhost/enramada", "root", "root"); 
        } catch (Exception e) {
            JOptionPane.showMessageDialog(null, "Error en la conexión" + e);
        }
        return conect;
    }   
}
