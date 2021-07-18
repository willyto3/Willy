package PCKModelo;

import java.sql.Date;

public class Persona {

    private long cedula;
    private String pnombre;
    private String snombre;
    private String papellido;
    private String sapellido;
    private long celular;
    private String email;
    private Date fechanacimiento;
    private String direccion;
    private String fkidgeneros;
    private String fkidcargos;

    public long getCedula() {
        return cedula;
    }

    public String getDireccion() {
        return direccion;
    }

    public void setDireccion(String direccion) {
        this.direccion = direccion;
    }

    public String getFkidgeneros() {
        return fkidgeneros;
    }

    public void setFkidgeneros(String fkidgeneros) {
        this.fkidgeneros = fkidgeneros;
    }

    public String getFkidcargos() {
        return fkidcargos;
    }

    public void setFkidcargos(String fkidcargos) {
        this.fkidcargos = fkidcargos;
    }

    public String getfkidgeneros() {
        return fkidgeneros;
    }

    public void setfkidgeneros(String fkidgeneros) {
        this.fkidgeneros = fkidgeneros;
    }

    public void setCedula(long cedula) {
        this.cedula = cedula;
    }

    public String getPnombre() {
        return pnombre;
    }

    public void setPnombre(String pnombre) {
        this.pnombre = pnombre;
    }

    public String getSnombre() {
        return snombre;
    }

    public void setSnombre(String snombre) {
        this.snombre = snombre;
    }

    public String getPapellido() {
        return papellido;
    }

    public void setPapellido(String papellido) {
        this.papellido = papellido;
    }

    public String getSapellido() {
        return sapellido;
    }

    public void setSapellido(String sapellido) {
        this.sapellido = sapellido;
    }

    public long getCelular() {
        return celular;
    }

    public void setCelular(long celular) {
        this.celular = celular;
    }

    public String getEmail() {
        return email;
    }

    public Date getFechanacimiento() {
        return fechanacimiento;
    }

    public void setFechanacimiento(Date fechanacimiento) {
        this.fechanacimiento = fechanacimiento;
    }

    public void setEmail(String email) {
        this.email = email;
    }

}
