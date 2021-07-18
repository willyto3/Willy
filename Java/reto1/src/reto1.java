
// Realizamos la importacion del metodo Scanner
import java.util.Scanner;

// Inicia la clase pública reto1
public class reto1 {

    // Inicio del programa
    public static void main(String[] args) throws Exception {
        // Inicializamos el scanner
        Scanner entrada = new Scanner(System.in);

        // Generamos las entradas al programa:número de estudiantes al programa
        int numero_de_estudiantes = entrada.nextInt();

        // Generamos la matriz de [número_de_estudiantes][3]
        float desempeño_de_estudiantes[][] = new float[numero_de_estudiantes][4];
        // Usamos el ciclo for para alimentar la matriz desempeño_de_estudiantes
        for (int fila = 0; fila < numero_de_estudiantes; fila++) {
            // Generamos la lista de entradas: nombre, genero, matería y calificación
            // System.out.println("Ingrese el nombre, genero, matería y calificación.
            // Separados por espacio");
            float nombre = entrada.nextFloat();
            float genero = entrada.nextFloat();
            float materia = entrada.nextFloat();
            float calificacion = entrada.nextFloat();
            desempeño_de_estudiantes[fila][0] = nombre;
            desempeño_de_estudiantes[fila][1] = genero;
            desempeño_de_estudiantes[fila][2] = materia;
            desempeño_de_estudiantes[fila][3] = calificacion;
        }

        float sumatoria_de_notas = 0;
        // Calculamos el promedio de las notas, iniciando sumatoria_de_notas=0
        for (int fila = 0; fila < numero_de_estudiantes; fila++) {
            sumatoria_de_notas += desempeño_de_estudiantes[fila][3];
        }
        float promedio_calificaciones = sumatoria_de_notas / numero_de_estudiantes;

        // Se contabiliza el número de notas inferiores al promedio de notas
        int notas_inferiores_a_promedio = 0;
        int notas_excelentes = 0;
        for (int fila = 0; fila < numero_de_estudiantes; fila++) {
            if (desempeño_de_estudiantes[fila][3] < promedio_calificaciones) {
                notas_inferiores_a_promedio += 1;
            }
            if (desempeño_de_estudiantes[fila][3] > 9) {
                notas_excelentes += 1;
            }

        }
        System.out.println(notas_inferiores_a_promedio);

        double b = notas_excelentes;
        double c = numero_de_estudiantes;

        Double porcentaje = (b) / c;
        porcentaje = Math.round(porcentaje * 100) / 100d;
        if (porcentaje == 0)
            System.out.println("0.00");
        else
            System.out.println(porcentaje);

        // ¿Cuál es la materia con el mayor numero de examenes reprobados
        // Definimos los contadores para las materias: 1,2 y 3
        int materia_1 = 0;
        int materia_2 = 0;
        int materia_3 = 0;

        for (int fila = 0; fila < numero_de_estudiantes; fila++) {
            if (desempeño_de_estudiantes[fila][2] == 1) {
                if (desempeño_de_estudiantes[fila][3] <= 6) {
                    materia_1 += 1;
                }
            } else if (desempeño_de_estudiantes[fila][2] == 2) {
                if (desempeño_de_estudiantes[fila][3] <= 6) {
                    materia_2 += 1;
                }
            } else {
                if (desempeño_de_estudiantes[fila][3] <= 6) {
                    materia_3 += 1;
                }
            }
        }

        // Comparamos las cantidades de examenes reprobados de cada materia, para
        // definir la materia con mayor número de examenes reprobados
        if (materia_1 >= materia_2 && materia_1 >= materia_3) {
            System.out.println("idiomas");
        } else if (materia_2 > materia_3) {
            System.out.println("historia");
        } else {
            System.out.println("literatura");
        }

        // ¿Cuál es el estudiante con el mejor desempeño para la materia idiomas?
        float mayor_nota = 0f;
        Float estudiante_mejor = 0f;
        for (int fila = 0; fila < numero_de_estudiantes; fila++) {
            if (desempeño_de_estudiantes[fila][2] == 1) {
                if (desempeño_de_estudiantes[fila][3] > mayor_nota) {
                    mayor_nota = desempeño_de_estudiantes[fila][3];
                    estudiante_mejor = desempeño_de_estudiantes[fila][0];
                }
            }
        }
        var nombreestudiante = "";
        switch (Math.round(estudiante_mejor)) {
            // Seleccionamos el caso que se debe ejecutar
            case 1:
                nombreestudiante = "armando";
                break;
            case 2:
                nombreestudiante = "nicolas";
                break;
            case 3:
                nombreestudiante = "daniel";
                break;
            case 4:
                nombreestudiante = "maria";
                break;
            case 5:
                nombreestudiante = "marcela";
                break;
            case 6:
                nombreestudiante = "alexandra";
                break;
        }