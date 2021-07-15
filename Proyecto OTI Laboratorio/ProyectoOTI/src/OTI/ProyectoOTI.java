
package OTI;

import PCKControlador.Controlador;
import PCKModelo.Consulta;
import PCKModelo.Persona;
import PCKVista.Vista;


public class ProyectoOTI {

    
    public static void main(String[] args) {
        
        Persona mod = new Persona();
        Vista frm=new Vista();
        Consulta modC =new Consulta();
        
        Controlador ctrl = new Controlador(mod, modC, frm);
            
        ctrl.iniciar();
        frm.setVisible(true);
        
        
        
    }
    
}
