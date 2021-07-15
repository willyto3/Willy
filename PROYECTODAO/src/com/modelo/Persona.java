
package com.modelo;
/**
 * Nombre de la clase: Persona
 * Versión: 1.5
 * Fecha 20/07/2017
 * copyrights: Grupo1
 * @author Daniel Angel, Nicolas Escobar, William Rosales, 
 * Erika Galdamez, Joseline Asuzena
 */
public class Persona {
    //<editor-fold defaultstate="list" desc="variables globales">
    private int idPersona;
    private String dui;
    private String nombre;
    private String apellido;
    private int edad;
    private String genero;
    private String telefono;
    private String direccion;
    private String pais;

    public Persona() {
    }

    public Persona(int idPersona, String dui, String nombre, String apellido, int edad, String genero, String telefono, String direccion, String pais) {
        this.idPersona = idPersona;
        this.dui = dui;
        this.nombre = nombre;
        this.apellido = apellido;
        this.edad = edad;
        this.genero = genero;
        this.telefono = telefono;
        this.direccion = direccion;
        this.pais = pais;
    }

    public int getIdPersona() {
        return idPersona;
    }

    public void setIdPersona(int idPersona) {
        this.idPersona = idPersona;
    }

    public String getDui() {
        return dui;
    }

    public void setDui(String dui) {
        this.dui = dui;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getApellido() {
        return apellido;
    }

    public void setApellido(String apellido) {
        this.apellido = apellido;
    }

    public int getEdad() {
        return edad;
    }

    public void setEdad(int edad) {
        this.edad = edad;
    }

    public String getGenero() {
        return genero;
    }

    public void setGenero(String genero) {
        this.genero = genero;
    }

    public String getTelefono() {
        return telefono;
    }

    public void setTelefono(String telefono) {
        this.telefono = telefono;
    }

    public String getDireccion() {
        return direccion;
    }

    public void setDireccion(String direccion) {
        this.direccion = direccion;
    }

    public String getPais() {
        return pais;
    }

    public void setPais(String pais) {
        this.pais = pais;
    }
    
}
