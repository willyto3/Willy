
package PCKModelo;


public class Municipio {
    
    private int idMunicipio;
    private String NombreMunicipio;
    private int fkidDepartamento;

    public int getIdMunicipio() {
        return idMunicipio;
    }

    public void setIdMunicipio(int idMunicipio) {
        this.idMunicipio = idMunicipio;
    }

    public String getNombreMunicipio() {
        return NombreMunicipio;
    }

    public void setNombreMunicipio(String NombreMunicipio) {
        this.NombreMunicipio = NombreMunicipio;
    }

    public int getFkidDepartamento() {
        return fkidDepartamento;
    }

    public void setFkidDepartamento(int fkidDepartamento) {
        this.fkidDepartamento = fkidDepartamento;
    }
    
    
    
}
