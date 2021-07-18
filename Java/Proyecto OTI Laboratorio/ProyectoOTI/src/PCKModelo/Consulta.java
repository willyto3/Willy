package PCKModelo;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import javax.swing.DefaultComboBoxModel;
import javax.swing.JComboBox;

public class Consulta extends Conexion {

    // Ingresar Persona en la Base de Datos 
    public boolean Guardar(Persona mod) {

        PreparedStatement ps = null;
        Connection con = getConexion();

        String sql = "INSERT INTO personas (Cedula, PrimerNombre, SegundoNombre, PrimerApellido, SegundoApellido, Celular, Email, FechaNacimiento,Direccion,  fkidgeneros, fkidcargos)"
                + "VALUES(?,?,?,?,?,?,?,?,?,(SELECT idgeneros FROM generos WHERE Genero=?), (SELECT idcargo FROM cargos WHERE Cargo=?))";

        try {
            ps = con.prepareStatement(sql);
            ps.setLong(1, mod.getCedula());
            ps.setString(2, mod.getPnombre());
            ps.setString(3, mod.getSnombre());
            ps.setString(4, mod.getPapellido());
            ps.setString(5, mod.getSapellido());
            ps.setLong(6, mod.getCelular());
            ps.setString(7, mod.getEmail());
            ps.setDate(8, mod.getFechanacimiento());
            ps.setString(9, mod.getDireccion());
            ps.setString(10, mod.getfkidgeneros());
            ps.setString(11, mod.getFkidcargos());
            ps.execute();

            return true;

        } catch (SQLException e) {

            System.err.println(e);
            return false;
        } finally {
            try {
                con.close();
            } catch (SQLException e) {
                System.err.println(e);
            }
        }

    }

    // Seleccionar Persona en la Base de Datos
    public boolean Editar(Persona mod) {

        PreparedStatement ps = null;
        ResultSet rs = null;
        Connection con = getConexion();

        String sql = "SELECT * FROM personas WHERE Cedula=?";

        try {

            ps = con.prepareStatement(sql);
            ps.setLong(1, mod.getCedula());
            rs = ps.executeQuery();

            if (rs.next()) {
                mod.setCedula(rs.getLong("Cedula"));
                mod.setPnombre(rs.getString("PrimerNombre"));
                mod.setSnombre(rs.getString("SegundoNombre"));
                mod.setPapellido(rs.getString("PrimerApellido"));
                mod.setSapellido(rs.getString("SegundoApellido"));
                mod.setCelular(rs.getLong("Celular"));
                mod.setEmail(rs.getString("Email"));
                mod.setFechanacimiento(rs.getDate("FechaNacimiento"));
                mod.setDireccion(rs.getString("Direccion"));
                mod.setFkidgeneros(rs.getString("fkidgeneros"));
                mod.setFkidcargos(rs.getString("fkidcargos"));

            }
            return true;

        } catch (SQLException e) {

            System.err.println(e);
            return false;
        } finally {
            try {
                con.close();
            } catch (SQLException e) {
                System.err.println(e);
            }
        }
    }

    // Ingresar Persona en la Base de Datos
    public boolean Ok(Persona mod) {

        PreparedStatement ps = null;
        Connection con = getConexion();

        String sql = "UPDATE personas SET PrimerNombre=?, SegundoNombre=?, PrimerApellido=?, SegundoApellido=?, Celular=?, Email=?, FechaNacimiento=?,"
                + "Direccion=?,"
                + "fkidgeneros=(SELECT idgeneros FROM generos WHERE Genero=?), fkidcargos=(SELECT idcargo FROM cargos WHERE Cargo=?) WHERE Cedula=?";

        try {
            ps = con.prepareStatement(sql);

            ps.setString(1, mod.getPnombre());
            ps.setString(2, mod.getSnombre());
            ps.setString(3, mod.getPapellido());
            ps.setString(4, mod.getSapellido());
            ps.setLong(5, mod.getCelular());
            ps.setString(6, mod.getEmail());
            ps.setDate(7, mod.getFechanacimiento());
            ps.setString(8, mod.getDireccion());
            ps.setString(9, mod.getfkidgeneros());
            ps.setString(10, mod.getFkidcargos());
            ps.setLong(11, mod.getCedula());
            ps.execute();

            return true;

        } catch (SQLException e) {

            System.err.println(e);
            return false;
        } finally {
            try {
                con.close();
            } catch (SQLException e) {
                System.err.println(e);
            }
        }

    }

    public boolean Eliminar(Persona mod) {

        PreparedStatement ps = null;
        Connection con = getConexion();

        String sql = "DELETE FROM personas WHERE Cedula=?";

        try {
            ps = con.prepareStatement(sql);
            ps.setLong(1, mod.getCedula());
            ps.execute();

            return true;

        } catch (SQLException e) {

            System.err.println(e);
            return false;
        } finally {
            try {
                con.close();
            } catch (SQLException e) {
                System.err.println(e);
            }
        }

    }

    public ArrayList<Persona> listPersona(String Busca) {

        ArrayList listaPersona = new ArrayList();
        Persona persona;
        PreparedStatement ps = null;
        ResultSet rs = null;
        Connection con = getConexion();
        String sql = "SELECT * FROM personas WHERE (Cedula like'" + Busca + "%' or PrimerNombre like'" + Busca + "%'or PrimerApellido like'" + Busca + "%'"
                + "or SegundoApellido like'" + Busca + "%'or SegundoNombre like'" + Busca + "%' or Celular like'" + Busca + "%'or Direccion like'" + Busca + "%') ";

        try {

            ps = con.prepareStatement(sql);
            rs = ps.executeQuery();

            while (rs.next()) {
                persona = new Persona();
                persona.setCedula(rs.getLong("Cedula"));
                persona.setPnombre(rs.getString("PrimerNombre"));
                persona.setPapellido(rs.getString("Primerapellido"));
                listaPersona.add(persona);

            }

        } catch (Exception e) {

        }

        return listaPersona;
    }

    public void listarPais(JComboBox box) {

        DefaultComboBoxModel value;
        PreparedStatement ps = null;
        ResultSet rs = null;
        Connection con = getConexion();

        try {
            ps = con.prepareStatement("SELECT * FROM paises");
            rs = ps.executeQuery();
            value = new DefaultComboBoxModel();
            box.setModel(value);
            value.addElement("Seleccione un Pais");

            while (rs.next()) {
                
                Pais pais = new Pais();
                 pais.setNombrePais(rs.getString("pais"));

                value.addElement(pais.getNombrePais());

            }

        } catch (SQLException ex) {

        } finally {
            try {
                con.close();
            } catch (SQLException ex) {
                System.err.println(ex);
            }
        }

    }
    
     public void listarDepartamento(JComboBox box,  String id) {

        DefaultComboBoxModel value;
        PreparedStatement ps = null;
        ResultSet rs = null;
        Connection con = getConexion();

        try {
            ps = con.prepareStatement("SELECT departamento FROM departamentos WHERE fkidpaises =(SELECT iDpaises FROM paises WHERE pais=?)");
            ps.setString(1, id);
            rs = ps.executeQuery();
            value = new DefaultComboBoxModel();
            box.setModel(value);
            value.addElement("Seleccione Departamento");

            while (rs.next()) {
                
                Departamento departamento = new Departamento();
                 departamento.setNombreDepartamento(rs.getString("departamento"));

                value.addElement(departamento.getNombreDepartamento());

            }

        } catch (SQLException ex) {

        } finally {
            try {
                con.close();
            } catch (SQLException ex) {
                System.err.println(ex);
            }
        }

    }
     
          public void listarMunicipio(JComboBox box,  String id) {

        DefaultComboBoxModel value;
        PreparedStatement ps = null;
        ResultSet rs = null;
        Connection con = getConexion();

        try {
            ps = con.prepareStatement("SELECT municipio FROM municipios WHERE fkiddepartamentos =(SELECT iddepartamentos FROM departamentos WHERE departamento=?)");
            ps.setString(1, id);
            rs = ps.executeQuery();
            value = new DefaultComboBoxModel();
            box.setModel(value);
            value.addElement("Seleccione Municipio");

            while (rs.next()) {
                
                Municipio municipio = new Municipio();
                 municipio.setNombreMunicipio(rs.getString("municipio"));

                value.addElement(municipio.getNombreMunicipio());

            }

        } catch (SQLException ex) {

        } finally {
            try {
                con.close();
            } catch (SQLException ex) {
                System.err.println(ex);
            }
        }

    }

}
