/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.dao;

import com.conexion.Conexion;
import com.modelo.Persona;
import java.sql.*;
import java.util.*;

/**
 *
 * @author Nathaly Guevara
 */
public class ControlPersona extends Conexion{
    public void insertarPersona(Persona per) throws Exception{
        try {
            this.conectar();
            String sql="insert into persona (dui, nombre, apellido, edad, genero, telefono, direccion, idPais)"
                    + " values(?,?,?,?,?,?,?,(select idpais from pais where nombrepais=?))";
            PreparedStatement pre = this.getCon().prepareStatement(sql);
            pre.setString(1, per.getDui());
            pre.setString(2, per.getNombre());
            pre.setString(3, per.getApellido());
            pre.setInt(4, per.getEdad());
            pre.setString(5,per.getGenero());
            pre.setString(6, per.getTelefono());
            pre.setString(7, per.getDireccion());
            pre.setString(8, per.getPais());
            pre.executeUpdate();
             
        } catch (Exception e) {
            throw e;
        }
    }
     public void modificarPersona(Persona per) throws Exception{
        try {
            this.conectar();
            String sql="update persona set dui=?,nombre=?, apellido=?, edad=?,genero=?, telefono=?, direccion=?,"
                    + " idPais=(select idpais from pais where nombrepais=?) where idPersona=?";
            PreparedStatement pre = this.getCon().prepareStatement(sql);
            pre.setString(1, per.getDui());
            pre.setString(2, per.getNombre());
            pre.setString(3, per.getApellido());
            pre.setInt(4, per.getEdad());
            pre.setString(5,per.getGenero());
            pre.setString(6, per.getTelefono());
            pre.setString(7, per.getDireccion());
            pre.setString(8, per.getPais());
            pre.setInt(9, per.getIdPersona());
            pre.executeUpdate();
             
        } catch (Exception e) {
            throw e;
        }
    }
       public void eliminarPersona(Persona per) throws Exception{
        try {
            this.conectar();
            String sql="delete from persona where idPersona=?";
            PreparedStatement pre = this.getCon().prepareStatement(sql);
            pre.setInt(1, per.getIdPersona());
            pre.executeUpdate();
             
        } catch (Exception e) {
            throw e;
        }
    }
     public List mostrarPersona()throws Exception{
         ResultSet res;
         List listaPersona = new ArrayList();
         try {
             this.conectar();
             String sql="select * from persona";
             PreparedStatement pre = this.getCon().prepareCall(sql);
             res = pre.executeQuery();
             while (res.next()) {                 
             Persona per = new Persona();
             per.setIdPersona(res.getInt("idPersona"));
             per.setDui(res.getString("Dui"));
             per.setNombre(res.getString("nombre"));
             per.setApellido(res.getString("apellido"));
             per.setEdad(res.getInt("edad"));
             per.setGenero(res.getString("genero"));
             per.setTelefono(res.getString("telefono"));
             per.setDireccion(res.getString("direccion"));
             per.setPais(res.getString("idpais"));
             listaPersona.add(per);
            
             }
         } catch (Exception e) {
             throw e;
         }return listaPersona;
     }
    
}
