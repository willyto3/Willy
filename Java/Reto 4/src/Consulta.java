import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

public class Consulta extends Conexion {

    // Ingresar Persona en la Base de Datos
    public static boolean Guardar(String nombre, String genero, String materia, String nota) {

        PreparedStatement ps = null;
        Connection conn = getConexion();

        String sql = "INSERT INTO estudiantes (nombre, genero, materia, nota)" + "VALUES(?,?,?,?)";

        try {
            ps = conn.prepareStatement(sql);
            ps.setString(1, nombre);
            ps.setString(2, genero);
            ps.setString(3, materia);
            ps.setString(4, nota);
            ps.execute();

            return true;

        } catch (SQLException e) {

            System.err.println(e);
            return false;
        } finally {
            try {
                conn.close();
            } catch (SQLException e) {
                System.err.println(e);
            }
        }

    }

    public static String Cargar() {

        PreparedStatement ps = null;
        ResultSet rs = null;
        Connection conn = getConexion();

        String sql = "SELECT * FROM estudiantes";

        try {

            ps = conn.prepareStatement(sql);
            rs = ps.executeQuery();

            String texto = "";

            while (rs.next()) {

                texto = texto + rs.getString("nombre") + " " + rs.getString("genero") + " " + rs.getString("materia")
                        + " " + rs.getString("nota") + "\n";

            }
            return texto;

        } catch (SQLException e) {

            System.err.println(e);
            return null;
        } finally {
            try {
                conn.close();
            } catch (SQLException e) {
                System.err.println(e);
            }
        }
    }

    public static String Consultar(String dato, Integer llamado) {
        String texto = "";
        PreparedStatement ps = null;
        ResultSet rs = null;
        Connection conn = getConexion();
        String sql;

        if (llamado == 1) {
            sql = "SELECT * FROM estudiantes WHERE nombre = ?";
        } else {
            sql = "SELECT * FROM estudiantes WHERE materia = ?";
        }
        try {

            ps = conn.prepareStatement(sql);
            ps.setString(1, dato);
            rs = ps.executeQuery();

            while (rs.next()) {

                texto = texto + rs.getString("nombre") + " " + rs.getString("genero") + " " + rs.getString("materia")
                        + " " + rs.getString("nota") + "\n";

            }

        } catch (Exception e) {
            return "No se Encontraron Datos";

        } finally {
            try {
                conn.close();
            } catch (SQLException e) {
                System.err.println(e);
            }
        }

        return texto;
    }

    public static Integer Eliminar(String dato, Integer llamado) {

        PreparedStatement ps = null;
        Connection conn = getConexion();
        String sql;
        int cuenta = 0;

        if (llamado == 1) {
            sql = "DELETE FROM estudiantes WHERE nombre=?";
        } else {
            sql = "DELETE FROM estudiantes WHERE materia=?";
        }

        try {
            ps = conn.prepareStatement(sql);
            ps.setString(1, dato);

            ps.execute();
            cuenta = ps.getUpdateCount();

            return cuenta;

        } catch (SQLException e) {

            System.err.println(e);
            return cuenta;
        } finally {
            try {
                conn.close();
            } catch (SQLException e) {
                System.err.println(e);
            }
        }

    }

}
