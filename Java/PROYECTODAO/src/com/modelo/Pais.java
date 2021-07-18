
package com.modelo;
/**
 * Nombre de la clase: pais
 * Versión: 1.5
 * Fecha 20/07/2017
 * copyrights: Grupo1
 * @author Daniel Angel, Nicolas Escobar, William Rosales, 
 * Erika Galdamez, Joseline Asuzena
 */
public class Pais {
    //<editor-fold defaultstate="list" desc="variables generales">
    private int idPais;
    private String codigoPais;
    private String nombrePais;
    private int numeroDepartamentos;
    private int numeroMunicipios;
    private String categoria;
//</editor-fold>
    
    //<editor-fold defaultstate="collapsed" desc="constructores">
    public Pais() {
    }

    public Pais(int idPais, String codigoPais, String nombrePais, int numeroDepartamentos, int numeroMunicipios, String categoria) {
        this.idPais = idPais;
        this.codigoPais = codigoPais;
        this.nombrePais = nombrePais;
        this.numeroDepartamentos = numeroDepartamentos;
        this.numeroMunicipios = numeroMunicipios;
        this.categoria = categoria;
    }   
//</editor-fold>
    
    //<editor-fold defaultstate="collapsed" desc="getter y setter">
    public int getIdPais() {
        return idPais;
    }

    public void setIdPais(int idPais) {
        this.idPais = idPais;
    }

    public String getCodigoPais() {
        return codigoPais;
    }

    public void setCodigoPais(String codigoPais) {
        this.codigoPais = codigoPais;
    }

    public String getNombrePais() {
        return nombrePais;
    }

    public void setNombrePais(String nombrePais) {
        this.nombrePais = nombrePais;
    }

    public int getNumeroDepartamentos() {
        return numeroDepartamentos;
    }

    public void setNumeroDepartamentos(int numeroDepartamentos) {
        this.numeroDepartamentos = numeroDepartamentos;
    }

    public int getNumeroMunicipios() {
        return numeroMunicipios;
    }

    public void setNumeroMunicipios(int numeroMunicipios) {
        this.numeroMunicipios = numeroMunicipios;
    }

    public String getCategoria() {
        return categoria;
    }

    public void setCategoria(String categoria) {
        this.categoria = categoria;
    }
    
    //</editor-fold>
    
}