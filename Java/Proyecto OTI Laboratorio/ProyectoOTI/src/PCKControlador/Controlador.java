package PCKControlador;

import PCKModelo.*;
import PCKVista.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.File;
import java.util.Date;
import javax.swing.JFileChooser;
import javax.swing.JOptionPane;
import javax.swing.JTable;
import javax.swing.filechooser.FileNameExtensionFilter;
import javax.swing.table.DefaultTableModel;

public class Controlador implements ActionListener {

    private final Persona mod;
    private final Consulta modC;
    private final Vista frm;

    public Controlador(Persona mod, Consulta modC, Vista frm) {
        this.mod = mod;
        this.modC = modC;
        this.frm = frm;
        this.frm.btnBuscar.addActionListener(this);
        this.frm.btnEditar.addActionListener(this);
        this.frm.btnEliminar.addActionListener(this);
        this.frm.btnLimpiar.addActionListener(this);
        this.frm.btnGuardar.addActionListener(this);
        this.frm.btnCargar.addActionListener(this);
        this.frm.btnOK.addActionListener(this);
        this.frm.cbPais.addActionListener(this);
        this.frm.cbDepartamento.addActionListener(this);

    }

    public void iniciar() {
        frm.setTitle("BASE DE DATOS OTI");
        frm.setLocationRelativeTo(null);
        modC.listarPais(frm.cbPais);

    }

    public void llenarTabla(JTable tabla) {

        String Busca = frm.tfBusqueda.getText();
        DefaultTableModel modeloT = new DefaultTableModel() {
            @Override
            public boolean isCellEditable(int row, int column) {
                //all cells false
                return false;
            }
        };
        tabla.setModel(modeloT);

        modeloT.addColumn("Cedula");
        modeloT.addColumn("Nombres");
        modeloT.addColumn("Apellidos");

        Object[] columna = new Object[3];
        int numRegistros = modC.listPersona(Busca).size();
        for (int i = 0; i < numRegistros; i++) {
            columna[0] = modC.listPersona(Busca).get(i).getCedula();
            columna[1] = modC.listPersona(Busca).get(i).getPnombre();
            columna[2] = modC.listPersona(Busca).get(i).getPapellido();
            modeloT.addRow(columna);
        }

    }

    @Override
    public void actionPerformed(ActionEvent e) {

        if (e.getSource() == frm.btnGuardar) {
            mod.setCedula(Long.parseLong(frm.tfCedula.getText()));
            mod.setPnombre(frm.tfPNombre.getText());
            mod.setSnombre(frm.tfSNombre.getText());
            mod.setPapellido(frm.tfPApellido.getText());
            mod.setSapellido(frm.tfSApellido.getText());
            mod.setEmail(frm.tfEmail.getText());
            mod.setCelular(Long.parseLong(frm.tfCelular.getText()));

            Date date = frm.FechaNac.getDate();

            long d = date.getTime();
            java.sql.Date fecha = new java.sql.Date(d);

            mod.setFechanacimiento(fecha);
            mod.setDireccion(frm.tfDireccion.getText());
            mod.setfkidgeneros((String) frm.cbGenero.getSelectedItem());
            mod.setFkidcargos((String) frm.cbCargo.getSelectedItem());

            if (modC.Guardar(mod)) {
                JOptionPane.showMessageDialog(null, "Registro Guardado");
                limpiar();
            } else {
                JOptionPane.showMessageDialog(null, "Error al Guardar");
                limpiar();
            }
        }

        if (e.getSource() == frm.btnOK) {
            mod.setCedula(Long.parseLong(frm.tfCedula.getText()));
            mod.setPnombre(frm.tfPNombre.getText());
            mod.setSnombre(frm.tfSNombre.getText());
            mod.setPapellido(frm.tfPApellido.getText());
            mod.setSapellido(frm.tfSApellido.getText());
            mod.setEmail(frm.tfEmail.getText());
            mod.setCelular(Long.parseLong(frm.tfCelular.getText()));

            Date date = frm.FechaNac.getDate();

            long d = date.getTime();
            java.sql.Date fecha = new java.sql.Date(d);

            mod.setFechanacimiento(fecha);
            mod.setDireccion(frm.tfDireccion.getText());

            mod.setfkidgeneros((String) frm.cbGenero.getSelectedItem());
            mod.setFkidcargos((String) frm.cbCargo.getSelectedItem());

            if (modC.Ok(mod)) {
                JOptionPane.showMessageDialog(null, "Registro Modificado");
                limpiar();
            } else {
                JOptionPane.showMessageDialog(null, "Error al Modificar");
                limpiar();
            }
        }

        if (e.getSource() == frm.btnEliminar) {
            mod.setCedula(Long.parseLong(frm.tfCedula.getText()));

            if (modC.Eliminar(mod)) {
                JOptionPane.showMessageDialog(null, "Registro Eliminado");
                limpiar();
            } else {
                JOptionPane.showMessageDialog(null, "Error al Eliminar");
                limpiar();
            }
        }

        if (e.getSource() == frm.btnBuscar) {

            llenarTabla(frm.tBusqueda);

        }

        if (e.getSource() == frm.btnLimpiar) {

            limpiar();

        }

        if (e.getSource() == frm.btnEditar) {

            int filaEditar = frm.tBusqueda.getSelectedRow();
            int numFS = frm.tBusqueda.getSelectedRowCount();

            if (filaEditar >= 0 && numFS == 1) {

                String Ced;
                Ced = frm.tBusqueda.getValueAt(filaEditar, 0).toString();

                frm.tfCedula.setText(Ced);
                mod.setCedula(Long.parseLong(Ced));

                if (modC.Editar(mod)) {
                    frm.tfPNombre.setText(mod.getPnombre());
                    frm.tfSNombre.setText(mod.getSnombre());
                    frm.tfPApellido.setText(mod.getPapellido());
                    frm.tfSApellido.setText(mod.getSapellido());
                    frm.tfEmail.setText(mod.getEmail());
                    frm.tfCelular.setText(String.valueOf(mod.getCelular()));
                    frm.FechaNac.setDate(mod.getFechanacimiento());
                    frm.tfDireccion.setText(mod.getDireccion());
                    frm.cbGenero.setSelectedIndex(Integer.parseInt(mod.getFkidgeneros()));
                    frm.cbCargo.setSelectedIndex(Integer.parseInt(mod.getFkidcargos()));

                } else {
                    limpiar();
                }

            } else {
                JOptionPane.showMessageDialog(null, "Debe Seleccionar una sola Fila");
            }

        }

        if (e.getSource() == frm.btnCargar) {

            JFileChooser fc = new JFileChooser();
            fc.setDialogTitle("Buscar Foto ó Imagen");

            fc.setFileSelectionMode(JFileChooser.FILES_AND_DIRECTORIES);
            FileNameExtensionFilter filtro = new FileNameExtensionFilter("*.PNG", "*.jpg", "*.png", "*.JPG", "*.JPEG", "*.jpeg");
            fc.setFileFilter(filtro);

            int seleccion = fc.showOpenDialog(fc);

            if (seleccion == JFileChooser.APPROVE_OPTION) {

                File fichero = fc.getSelectedFile();
                String ruta = fichero.getAbsolutePath();

                rsscalelabel.RSScaleLabel.setScaleLabel(frm.jFoto, ruta);

            }
        }

        if (e.getSource() == frm.cbPais) {

            modC.listarDepartamento(frm.cbDepartamento, frm.cbPais.getSelectedItem().toString());
        }

        if (e.getSource() == frm.cbDepartamento) {

            modC.listarMunicipio(frm.cbMunicipio, frm.cbDepartamento.getSelectedItem().toString());
        }

    }

    public void limpiar() {

        frm.tfCedula.setText(null);
        frm.tfPNombre.setText(null);
        frm.tfSNombre.setText(null);
        frm.tfPApellido.setText(null);
        frm.tfSApellido.setText(null);
        frm.tfEmail.setText(null);
        frm.tfCelular.setText(null);
        frm.tfBusqueda.setText(null);
        frm.FechaNac.setDate(null);
        frm.tfDireccion.setText(null);
        frm.cbGenero.setSelectedIndex(0);
        frm.cbCargo.setSelectedIndex(0);
        limpiaTabla(frm.tBusqueda);
        rsscalelabel.RSScaleLabel.setScaleLabel(frm.jFoto, "src/imagenes/Grupo.jpg");

    }

    void limpiaTabla(JTable tabla) {

        tabla.setModel(new DefaultTableModel());

    }
}
