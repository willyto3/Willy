
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class Conexion {

    public static Connection getConexion() {

        final String url = "jdbc:sqlite:BDatos.db";
        Connection conn = null;

        try {
            Class.forName("org.sqlite.JDBC");
            conn = DriverManager.getConnection(url);
            System.out.println("Se realizo la Conexion");
        } catch (SQLException | ClassNotFoundException e) {
            System.err.println(e);
        }

        return conn;
    }
}
