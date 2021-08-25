package aplicacion;

public class funciones {

    // Funcion para validar correo electronico
    public static boolean correoElectronicoValido(String email) {
        String regex = "^[\\w-_\\.+]*[\\w-_\\.]\\@([\\w]+\\.)+[\\w]+[\\w]$";
        return email.matches(regex);
    }

    // Funcion para capturar un numero entero
    public static int capturarNumeroEntero(String mensaje) {
        while (true) {
            try {
                System.out.printf("%s: ", mensaje);
                return Integer.parseInt(aplicacion.teclado.nextLine());
            } catch (NumberFormatException e) {
                System.out.println("MENSAJE: Digite un valor que corresponda con un número entero");
            }
        }
    }

    // Funcion para capturar cadenas de caracteres
    public static String capturarCadenaDeCaracteres(String mensaje) {
        String resultado;

        while (true) {
            System.out.printf("%s: ", mensaje);
            resultado = aplicacion.teclado.nextLine().strip();

            if (!resultado.isEmpty()) {
                return resultado;
            }
            System.out.println("MENSAJE: Especifique un valor correcto.");

        }
    }

    // Funcion para capturar un numero real
    public static double capturarNumeroReal(String mensaje) {
        while (true) {
            try {
                System.out.printf("%s: ", mensaje);
                return Double.parseDouble(aplicacion.teclado.nextLine());
            } catch (NumberFormatException e) {
                System.out.println("MENSAJE: Digite un valor que corresponda con un número real");
            }
        }
    }

    // Funcion para presentar en pantalla el menu principal
    public static void mostrarMenuPrincipal() {
        System.out.println("==MENU PRINCIPAL==");
        System.out.println("1. Gestion Clientes");
        System.out.println("2. Gestion Proveedores");
        System.out.println("3. Gestion Productos");
        System.out.println("4. Gestion Facturacion");
        System.out.println("0. Salir");
    }

    // Funcion para presentar en pantalla el sub menu Cliente, Proveedores y
    // Productos
    public static void mostrarSubMenu(String tipoMenu) {
        System.out.printf("**Menu Gestion %s**\n", tipoMenu);
        System.out.println("1. Crear");
        System.out.println("2. Buscar");
        System.out.println("3. Actualizar");
        System.out.println("4. Eliminar");
        System.out.println("0. Salir");
    }

    // Funcion para presentar en pantalla el sub menu Facturacion
    public static void mostrarSubMenuFacturacion() {
        System.out.printf("**Menu Gestion Facturacion**\n");
        System.out.println("1. Crear");
        System.out.println("2. Buscar");
        System.out.println("3. Eliminar");
        System.out.println("0. Salir");
    }

    // Funcion para focalizar la atencion del usuario
    public static void continuar() {
        System.out.println();
        System.out.println("Presione Enter para Continuar...");
        aplicacion.teclado.nextLine();
    }

}
