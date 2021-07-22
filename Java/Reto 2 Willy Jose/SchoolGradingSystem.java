public class SchoolGradingSystem {
    // atributos
    private double[][] datos;
    private int num_cal;

    // Metodos

    public void readData() {
        java.util.Scanner leer = new java.util.Scanner(System.in);
        String tmp;
        String[] linea;
        num_cal = Integer.parseInt(leer.nextLine());
        datos = new double[num_cal][4];
        for (int i = 0; i < num_cal; i++) {
            // 1. leer como texto
            tmp = leer.nextLine();
            // 2. dividir texto
            linea = tmp.split(" ");
            // 3. Transformar
            for (int j = 0; j < linea.length; j++) {
                datos[i][j] = Double.parseDouble(linea[j]);
            }

        }
        leer.close();
    }

    public double question1() {
        // Calculamos el promedio de las notas, iniciando sumatoria_de_notas=0
        double suma = 0.0;
        double prom = 0.0;

        for (int i = 0; i < num_cal; i++)
            suma += datos[i][3];

        prom = (suma) / (num_cal);

        return prom;
    }

    public double question2() {

        double suma_e = 0.0;
        double prom_e = 0.0;
        for (int i = 0; i < num_cal; i++) {

            if (datos[i][3] > 4.5 && datos[i][3] <= 5)
                suma_e += 1;

            if (num_cal > 0)
                prom_e = suma_e / num_cal;
        }
        return prom_e;
    }

    public String question3() {
        Double suma_h = 0.0;
        int notas_h = 0;
        Double suma_m = 0.0;
        int notas_m = 0;

        for (int i = 0; i < num_cal; i++) {

            if (datos[i][1] == 0) {
                suma_h += 1;
                notas_h += datos[i][3];
            } else {
                suma_m += 1;
                notas_m += datos[i][3];
            }
        }
        String genero = "f";
        if (notas_h / suma_h > notas_m / suma_m)
            genero = "m";

        return genero;
    }

    public String question4() {

        int quimica = 1;
        int posicion = 0;
        String[] estudiantes = { "armando", "nicolas", "daniel", "maria", "marcela", "alexandra" };

        for (int i = 0; i < num_cal; i++) {

            if (datos[i][2] == 1.0) {

                if ((datos[i][3] > datos[posicion][3])) {
                    quimica = (int) datos[i][0];
                    posicion = i;
                }
            }
        }

        return estudiantes[quimica - 1];
    }

}
