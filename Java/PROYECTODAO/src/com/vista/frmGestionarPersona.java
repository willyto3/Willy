/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.vista;

import com.conexion.Conexion;
import com.dao.ControlPersona;
import com.modelo.Persona;
import javax.swing.DefaultComboBoxModel;
import java.sql.*;
import java.util.List;
import javax.swing.JOptionPane;
import javax.swing.JTable;
import javax.swing.table.DefaultTableModel;
import javax.swing.table.TableColumnModel;

/**
 *
 * @author Nathaly Guevara
 */
public class frmGestionarPersona extends javax.swing.JFrame {
    DefaultComboBoxModel modelo;
    Persona per = new Persona();
    ControlPersona dao = new ControlPersona();
    /**
     * Creates new form frmGestionarPersona
     */
    public frmGestionarPersona() {
        initComponents();
        modelo = new DefaultComboBoxModel();
        cargarlistaEmpleados();
        tablaP();
        tbPersona.setAutoResizeMode(JTable.AUTO_RESIZE_OFF);
        TableColumnModel columnModel = tbPersona.getColumnModel();
        columnModel.getColumn(0).setPreferredWidth(50);
        columnModel.getColumn(1).setPreferredWidth(100);
        columnModel.getColumn(2).setPreferredWidth(150);
        columnModel.getColumn(3).setPreferredWidth(150);
        columnModel.getColumn(4).setPreferredWidth(150);
        columnModel.getColumn(5).setPreferredWidth(100);
        columnModel.getColumn(6).setPreferredWidth(100);
        columnModel.getColumn(7).setPreferredWidth(100);
        columnModel.getColumn(8).setPreferredWidth(150);

    }
     public void cargarlistaEmpleados() {
       Conexion con = new Conexion();
       Connection cn;
       ResultSet res;
       try {
            con.conectar();
            String sql="Select * from pais";
            PreparedStatement pre = con.getCon().prepareCall(sql);
            res = pre.executeQuery();
            modelo.removeAllElements();
            while(res.next()){
                 modelo.addElement(res.getString("nombrePais"));
             }
           jComboPais.setModel(modelo);
           con.desconectar();
         } catch (Exception e) {
             System.out.println("ERROR: failed to load HSQLDB JDBC driver.");
             e.printStackTrace();
         }
       
                    
      }
   public void insertar() throws Exception{
        per.setIdPersona(ICONIFIED);
        per.setDui(this.txtdui.getText());
        per.setNombre(this.txtnombre.getText());
        per.setApellido(this.txtApe.getText());
        per.setEdad(Integer.parseInt(this.jSEdad.getValue().toString()));
        if(this.jRF.isSelected()){
            per.setGenero("Femenino");
        }else{
            per.setGenero("Masculino");
        }
        per.setTelefono(this.txtTelefono.getText());
        per.setDireccion(this.txtDIr.getText());
        per.setPais(this.jComboPais.getSelectedItem().toString());
        dao.insertarPersona(per);
        JOptionPane.showMessageDialog(null, "Datos insertados");
       
    }
    public void modificar(){
        try {
        per.setIdPersona(Integer.parseInt(this.txtcod.getText()));
        per.setDui(this.txtdui.getText());
        per.setNombre(this.txtnombre.getText());
        per.setApellido(this.txtApe.getText());
        per.setEdad(Integer.parseInt(this.jSEdad.getValue().toString()));
        if(this.jRF.isSelected()){
            per.setGenero("Femenino");
        }else{
            per.setGenero("Masculino");
        }
        per.setTelefono(this.txtTelefono.getText());
        per.setDireccion(this.txtDIr.getText());
        per.setPais(this.jComboPais.getSelectedItem().toString());
        int SioNo = JOptionPane.showConfirmDialog(this, "Desea modificar?","Confirmacion"
                ,JOptionPane.YES_NO_OPTION);
          if (SioNo==0) {
               dao.modificarPersona(per);
               JOptionPane.showMessageDialog(this,"Datos modificados");
               tablaP();
               limpiar();
          }else{
              limpiar();
          }
          } catch (Exception e) {
              e.printStackTrace();
        }
       
    }
     public void eliminar(){
         try {
         per.setIdPersona(Integer.parseInt(this.txtcod.getText()));
        int SioNo = JOptionPane.showConfirmDialog(this, "Desea eliminar?","Confirmacion"
                ,JOptionPane.YES_NO_OPTION);
          if (SioNo==0) {
               dao.eliminarPersona(per);
               JOptionPane.showMessageDialog(this,"Datos modificados");
               tablaP();
          }else{
              limpiar();
          }              
         } catch (Exception e) {
             e.printStackTrace();
         }
       
    }
    public void tablaP(){
        String[] columnas ={"Cod","DUI","NOMBRE","APELLIDO", "EDAD", "GENERO", "TELEFONO","DIRECCION","NOMBRE-PAIS"};
        Object[] obj = new Object[9];
        DefaultTableModel tabla = new DefaultTableModel(null,columnas);
        List ls;
        try {
            ls = dao.mostrarPersona();
            for (int i = 0; i < ls.size(); i++) {
                per = (Persona) ls.get(i);
                obj[0] = per.getIdPersona();
                obj[1] = per.getDui();
                obj[2] = per.getNombre();
                obj[3] = per.getApellido();
                obj[4] = per.getEdad();
                obj[5] = per.getGenero();
                obj[6] = per.getTelefono();
                obj[7] = per.getDireccion();
                obj[8] = per.getPais();
                tabla.addRow(obj);
            }
            this.tbPersona.setModel(tabla);
        } catch (Exception e) {
            e.printStackTrace();
        }
        
    }
    public void limpiar(){
        this.txtcod.setText("");
        this.txtdui.setText("");
        this.txtApe.setText("");
        this.txtDIr.setText("");
        this.txtTelefono.setText("");
        this.jComboPais.setSelectedIndex(0);
        this.jRM.setSelected(false);
        this.jRM.setSelected(true);
        this.jSEdad.getModel().setValue(18);
            
    }
    
    /**
     * This method is called from within the constructor to initialize the form.
     * WARNING: Do NOT modify this code. The content of this method is always
     * regenerated by the Form Editor.
     */
    @SuppressWarnings("unchecked")
    // <editor-fold defaultstate="collapsed" desc="Generated Code">//GEN-BEGIN:initComponents
    private void initComponents() {

        jLabel10 = new javax.swing.JLabel();
        buttonGroup1 = new javax.swing.ButtonGroup();
        jLabel1 = new javax.swing.JLabel();
        jLabel2 = new javax.swing.JLabel();
        jLabel3 = new javax.swing.JLabel();
        jLabel4 = new javax.swing.JLabel();
        jLabel5 = new javax.swing.JLabel();
        jLabel6 = new javax.swing.JLabel();
        jLabel7 = new javax.swing.JLabel();
        jLabel8 = new javax.swing.JLabel();
        jLabel9 = new javax.swing.JLabel();
        txtcod = new javax.swing.JTextField();
        txtnombre = new javax.swing.JTextField();
        txtApe = new javax.swing.JTextField();
        txtDIr = new javax.swing.JTextField();
        jComboPais = new javax.swing.JComboBox<>();
        jScrollPane1 = new javax.swing.JScrollPane();
        tbPersona = new javax.swing.JTable();
        jPanel1 = new javax.swing.JPanel();
        jLabel11 = new javax.swing.JLabel();
        btnEliminar = new javax.swing.JButton();
        btnModificar = new javax.swing.JButton();
        btnLimpiar = new javax.swing.JButton();
        btnInsertar = new javax.swing.JButton();
        jRF = new javax.swing.JRadioButton();
        jRM = new javax.swing.JRadioButton();
        jSEdad = new javax.swing.JSpinner();
        txtdui = new javax.swing.JFormattedTextField();
        txtTelefono = new javax.swing.JFormattedTextField();

        jLabel10.setText("jLabel10");

        setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);
        getContentPane().setLayout(new org.netbeans.lib.awtextra.AbsoluteLayout());

        jLabel1.setText("Codigo:");
        getContentPane().add(jLabel1, new org.netbeans.lib.awtextra.AbsoluteConstraints(150, 110, -1, -1));

        jLabel2.setText("Nombre:");
        getContentPane().add(jLabel2, new org.netbeans.lib.awtextra.AbsoluteConstraints(52, 178, -1, -1));

        jLabel3.setText("Apellido:");
        getContentPane().add(jLabel3, new org.netbeans.lib.awtextra.AbsoluteConstraints(52, 230, -1, -1));

        jLabel4.setText("DUI:");
        getContentPane().add(jLabel4, new org.netbeans.lib.awtextra.AbsoluteConstraints(67, 146, -1, -1));

        jLabel5.setText("Edad:");
        getContentPane().add(jLabel5, new org.netbeans.lib.awtextra.AbsoluteConstraints(61, 278, -1, -1));

        jLabel6.setText("Genero:");
        getContentPane().add(jLabel6, new org.netbeans.lib.awtextra.AbsoluteConstraints(54, 316, -1, -1));

        jLabel7.setText("Telefono:");
        getContentPane().add(jLabel7, new org.netbeans.lib.awtextra.AbsoluteConstraints(47, 351, -1, -1));

        jLabel8.setText("Direccion:");
        getContentPane().add(jLabel8, new org.netbeans.lib.awtextra.AbsoluteConstraints(46, 392, -1, -1));

        jLabel9.setText("Pais:");
        getContentPane().add(jLabel9, new org.netbeans.lib.awtextra.AbsoluteConstraints(70, 430, -1, -1));

        txtcod.setEnabled(false);
        getContentPane().add(txtcod, new org.netbeans.lib.awtextra.AbsoluteConstraints(200, 110, 160, -1));
        getContentPane().add(txtnombre, new org.netbeans.lib.awtextra.AbsoluteConstraints(97, 175, 147, -1));
        getContentPane().add(txtApe, new org.netbeans.lib.awtextra.AbsoluteConstraints(97, 227, 147, -1));
        getContentPane().add(txtDIr, new org.netbeans.lib.awtextra.AbsoluteConstraints(97, 389, 147, -1));

        jComboPais.setModel(new javax.swing.DefaultComboBoxModel<>(new String[] { "Item 1", "Item 2", "Item 3", "Item 4" }));
        getContentPane().add(jComboPais, new org.netbeans.lib.awtextra.AbsoluteConstraints(97, 427, 147, -1));

        tbPersona.setModel(new javax.swing.table.DefaultTableModel(
            new Object [][] {
                {null, null, null, null},
                {null, null, null, null},
                {null, null, null, null},
                {null, null, null, null}
            },
            new String [] {
                "Title 1", "Title 2", "Title 3", "Title 4"
            }
        ));
        tbPersona.addMouseListener(new java.awt.event.MouseAdapter() {
            public void mouseClicked(java.awt.event.MouseEvent evt) {
                tbPersonaMouseClicked(evt);
            }
        });
        jScrollPane1.setViewportView(tbPersona);

        getContentPane().add(jScrollPane1, new org.netbeans.lib.awtextra.AbsoluteConstraints(40, 460, 490, 99));

        jPanel1.setBackground(new java.awt.Color(51, 51, 51));

        jLabel11.setFont(new java.awt.Font("Tahoma", 1, 36)); // NOI18N
        jLabel11.setForeground(new java.awt.Color(255, 255, 255));
        jLabel11.setText("Gestionar Persona");

        javax.swing.GroupLayout jPanel1Layout = new javax.swing.GroupLayout(jPanel1);
        jPanel1.setLayout(jPanel1Layout);
        jPanel1Layout.setHorizontalGroup(
            jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(jPanel1Layout.createSequentialGroup()
                .addGap(116, 116, 116)
                .addComponent(jLabel11)
                .addContainerGap(138, Short.MAX_VALUE))
        );
        jPanel1Layout.setVerticalGroup(
            jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, jPanel1Layout.createSequentialGroup()
                .addContainerGap(22, Short.MAX_VALUE)
                .addComponent(jLabel11)
                .addContainerGap())
        );

        getContentPane().add(jPanel1, new org.netbeans.lib.awtextra.AbsoluteConstraints(0, 0, 588, -1));

        btnEliminar.setFont(new java.awt.Font("Tahoma", 1, 24)); // NOI18N
        btnEliminar.setText("Eliminar");
        btnEliminar.addMouseListener(new java.awt.event.MouseAdapter() {
            public void mouseClicked(java.awt.event.MouseEvent evt) {
                btnEliminarMouseClicked(evt);
            }
        });
        btnEliminar.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                btnEliminarActionPerformed(evt);
            }
        });
        getContentPane().add(btnEliminar, new org.netbeans.lib.awtextra.AbsoluteConstraints(380, 286, 150, 70));

        btnModificar.setFont(new java.awt.Font("Tahoma", 1, 24)); // NOI18N
        btnModificar.setText("Modificar");
        btnModificar.addMouseListener(new java.awt.event.MouseAdapter() {
            public void mouseClicked(java.awt.event.MouseEvent evt) {
                btnModificarMouseClicked(evt);
            }
        });
        btnModificar.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                btnModificarActionPerformed(evt);
            }
        });
        getContentPane().add(btnModificar, new org.netbeans.lib.awtextra.AbsoluteConstraints(380, 196, 150, 70));

        btnLimpiar.setFont(new java.awt.Font("Tahoma", 1, 24)); // NOI18N
        btnLimpiar.setText("Limpiar");
        btnLimpiar.addMouseListener(new java.awt.event.MouseAdapter() {
            public void mouseClicked(java.awt.event.MouseEvent evt) {
                btnLimpiarMouseClicked(evt);
            }
        });
        btnLimpiar.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                btnLimpiarActionPerformed(evt);
            }
        });
        getContentPane().add(btnLimpiar, new org.netbeans.lib.awtextra.AbsoluteConstraints(380, 376, 150, 70));

        btnInsertar.setFont(new java.awt.Font("Tahoma", 1, 24)); // NOI18N
        btnInsertar.setText("Insetar");
        btnInsertar.addMouseListener(new java.awt.event.MouseAdapter() {
            public void mouseClicked(java.awt.event.MouseEvent evt) {
                btnInsertarMouseClicked(evt);
            }
        });
        btnInsertar.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                btnInsertarActionPerformed(evt);
            }
        });
        getContentPane().add(btnInsertar, new org.netbeans.lib.awtextra.AbsoluteConstraints(380, 106, 150, 70));

        buttonGroup1.add(jRF);
        jRF.setText("Femenino");
        getContentPane().add(jRF, new org.netbeans.lib.awtextra.AbsoluteConstraints(200, 310, -1, -1));

        buttonGroup1.add(jRM);
        jRM.setText("Masculino");
        getContentPane().add(jRM, new org.netbeans.lib.awtextra.AbsoluteConstraints(100, 310, -1, -1));
        getContentPane().add(jSEdad, new org.netbeans.lib.awtextra.AbsoluteConstraints(100, 270, 40, 30));

        try {
            txtdui.setFormatterFactory(new javax.swing.text.DefaultFormatterFactory(new javax.swing.text.MaskFormatter("########-#")));
        } catch (java.text.ParseException ex) {
            ex.printStackTrace();
        }
        getContentPane().add(txtdui, new org.netbeans.lib.awtextra.AbsoluteConstraints(100, 140, 150, -1));

        try {
            txtTelefono.setFormatterFactory(new javax.swing.text.DefaultFormatterFactory(new javax.swing.text.MaskFormatter("(+###)####-####")));
        } catch (java.text.ParseException ex) {
            ex.printStackTrace();
        }
        getContentPane().add(txtTelefono, new org.netbeans.lib.awtextra.AbsoluteConstraints(100, 350, 140, -1));

        pack();
    }// </editor-fold>//GEN-END:initComponents

    private void btnEliminarActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_btnEliminarActionPerformed
        // TODO add your handling code here:
    }//GEN-LAST:event_btnEliminarActionPerformed

    private void btnModificarActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_btnModificarActionPerformed
        // TODO add your handling code here:
    }//GEN-LAST:event_btnModificarActionPerformed

    private void btnLimpiarActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_btnLimpiarActionPerformed
        // TODO add your handling code here:
    }//GEN-LAST:event_btnLimpiarActionPerformed

    private void btnInsertarActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_btnInsertarActionPerformed
        // TODO add your handling code here:
    }//GEN-LAST:event_btnInsertarActionPerformed

    private void btnInsertarMouseClicked(java.awt.event.MouseEvent evt) {//GEN-FIRST:event_btnInsertarMouseClicked
        // TODO add your handling code here:
        try {
            insertar();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }//GEN-LAST:event_btnInsertarMouseClicked

    private void tbPersonaMouseClicked(java.awt.event.MouseEvent evt) {//GEN-FIRST:event_tbPersonaMouseClicked

        // TODO add your handling code here:
        int fila = this.tbPersona.getSelectedRow();
        this.txtcod.setText(String.valueOf(this.tbPersona.getValueAt(fila,0)));
        this.txtdui.setText(String.valueOf(this.tbPersona.getValueAt(fila,1)));
        this.txtnombre.setText(String.valueOf(this.tbPersona.getValueAt(fila, 2)));
        this.txtApe.setText(String.valueOf(this.tbPersona.getValueAt(fila, 3)));
        this.jSEdad.setValue(this.tbPersona.getValueAt(fila, 4));
         //Asignando el genero alos radios 
       if (String.valueOf(this.tbPersona.getValueAt(fila, 5)).equals("Masculino")) {
        
            jRM.setSelected(true);
            
        }else if ("Femenino".equals(String.valueOf(this.tbPersona.getValueAt(fila, 5)))) {
            
           jRF.setSelected(true);
        }
        this.txtTelefono.setText(String.valueOf(this.tbPersona.getValueAt(fila, 6)));
        this.txtDIr.setText(String.valueOf(this.tbPersona.getValueAt(fila, 7)));
        this.jComboPais.setSelectedItem(String.valueOf(this.tbPersona.getValueAt(fila, 8)));
    }//GEN-LAST:event_tbPersonaMouseClicked

    private void btnModificarMouseClicked(java.awt.event.MouseEvent evt) {//GEN-FIRST:event_btnModificarMouseClicked
        // TODO add your handling code here:
        modificar();
    }//GEN-LAST:event_btnModificarMouseClicked

    private void btnEliminarMouseClicked(java.awt.event.MouseEvent evt) {//GEN-FIRST:event_btnEliminarMouseClicked
        // TODO add your handling code here:
        eliminar();
    }//GEN-LAST:event_btnEliminarMouseClicked

    private void btnLimpiarMouseClicked(java.awt.event.MouseEvent evt) {//GEN-FIRST:event_btnLimpiarMouseClicked
        // TODO add your handling code here:
        limpiar();
    }//GEN-LAST:event_btnLimpiarMouseClicked

    /**
     * @param args the command line arguments
     */
    public static void main(String args[]) {
        /* Set the Nimbus look and feel */
        //<editor-fold defaultstate="collapsed" desc=" Look and feel setting code (optional) ">
        /* If Nimbus (introduced in Java SE 6) is not available, stay with the default look and feel.
         * For details see http://download.oracle.com/javase/tutorial/uiswing/lookandfeel/plaf.html 
         */
        try {
            for (javax.swing.UIManager.LookAndFeelInfo info : javax.swing.UIManager.getInstalledLookAndFeels()) {
                if ("Nimbus".equals(info.getName())) {
                    javax.swing.UIManager.setLookAndFeel(info.getClassName());
                    break;
                }
            }
        } catch (ClassNotFoundException ex) {
            java.util.logging.Logger.getLogger(frmGestionarPersona.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (InstantiationException ex) {
            java.util.logging.Logger.getLogger(frmGestionarPersona.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (IllegalAccessException ex) {
            java.util.logging.Logger.getLogger(frmGestionarPersona.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (javax.swing.UnsupportedLookAndFeelException ex) {
            java.util.logging.Logger.getLogger(frmGestionarPersona.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        }
        //</editor-fold>

        /* Create and display the form */
        java.awt.EventQueue.invokeLater(new Runnable() {
            public void run() {
                new frmGestionarPersona().setVisible(true);
            }
        });
    }

    // Variables declaration - do not modify//GEN-BEGIN:variables
    private javax.swing.JButton btnEliminar;
    private javax.swing.JButton btnInsertar;
    private javax.swing.JButton btnLimpiar;
    private javax.swing.JButton btnModificar;
    private javax.swing.ButtonGroup buttonGroup1;
    private javax.swing.JComboBox<String> jComboPais;
    private javax.swing.JLabel jLabel1;
    private javax.swing.JLabel jLabel10;
    private javax.swing.JLabel jLabel11;
    private javax.swing.JLabel jLabel2;
    private javax.swing.JLabel jLabel3;
    private javax.swing.JLabel jLabel4;
    private javax.swing.JLabel jLabel5;
    private javax.swing.JLabel jLabel6;
    private javax.swing.JLabel jLabel7;
    private javax.swing.JLabel jLabel8;
    private javax.swing.JLabel jLabel9;
    private javax.swing.JPanel jPanel1;
    private javax.swing.JRadioButton jRF;
    private javax.swing.JRadioButton jRM;
    private javax.swing.JSpinner jSEdad;
    private javax.swing.JScrollPane jScrollPane1;
    private javax.swing.JTable tbPersona;
    private javax.swing.JTextField txtApe;
    private javax.swing.JTextField txtDIr;
    private javax.swing.JFormattedTextField txtTelefono;
    private javax.swing.JTextField txtcod;
    private javax.swing.JFormattedTextField txtdui;
    private javax.swing.JTextField txtnombre;
    // End of variables declaration//GEN-END:variables
}
