package PCKModelo;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;



public class Conexion {

    //private final String base = "mydb";
    private final String user = "root";
    private final String password = "Laureano";
    private final String url = "jdbc:mysql://127.0.0.1:3306/mydb?useUnicode=true&useJDBCCompliantTimezoneShift=true&useLegacyDatetimeCode=false&serverTimezone=UTC";
    private Connection con = null;

    public Connection getConexion() {

        try {
            Class.forName("com.mysql.cj.jdbc.Driver");
            con = DriverManager.getConnection(this.url, this.user, this.password);
            //JOptionPane.showInputDialog(null, "Se realizo la Conexion");
        } catch (SQLException | ClassNotFoundException e) {
            System.err.println(e);
        }
       
        return con;
    }

}
