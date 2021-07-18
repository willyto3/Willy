
package PCKModelo;


public class Departamento {
   
    private int idDepartamento;
    private String NombreDepartamento;
    private int fkidPais;

    public int getIdDepartamento() {
        return idDepartamento;
    }

    public void setIdDepartamento(int idDepartamento) {
        this.idDepartamento = idDepartamento;
    }

    public String getNombreDepartamento() {
        return NombreDepartamento;
    }

    public void setNombreDepartamento(String NombreDepartamento) {
        this.NombreDepartamento = NombreDepartamento;
    }

    public int getFkidPais() {
        return fkidPais;
    }

    public void setFkidPais(int fkidPais) {
        this.fkidPais = fkidPais;
    }
    
    
}
