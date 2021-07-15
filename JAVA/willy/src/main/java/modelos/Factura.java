package modelos;

import java.util.ArrayList;
import java.util.Date;
import java.util.List;

public class Factura {
    private static int contadorIds=1;
    private int id;
    private Date fecha;
    private String cedulaCliente;
    private double impuestos;
    private double total;
    private List<Integer> idsProductos;

    public Factura() {
        idsProductos = new ArrayList<Integer>();
        id = contadorIds;
        ++contadorIds;
    }

    public Factura(String cedulaCliente, double impuestos) {
        this();
        fecha = new Date();
        this.cedulaCliente = cedulaCliente;
        this.impuestos = impuestos;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public Date getFecha() {
        return fecha;
    }

    public void setFecha(Date fecha) {
        this.fecha = fecha;
    }

    public String getCedulaCliente() {
        return cedulaCliente;
    }

    public void setCedulaCliente(String cedulaCliente) {
        this.cedulaCliente = cedulaCliente;
    }

    public double getImpuestos() {
        return impuestos;
    }

    public void setImpuestos(double impuestos) {
        this.impuestos = impuestos;
    }

    public double getTotal() {
        return total;
    }

    public void setTotal(double total) {
        this.total = total;
    }

    public void agregarIdProducto(Integer idProducto){
        idsProductos.add(idProducto);
    }

    public Integer[] getIdsProductos() {
        Integer [] idsProductosCopia = new Integer[idsProductos.size()];
        return idsProductosCopia;
    }

}
