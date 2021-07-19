import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class SchoolGradingSystem {
    private float nombre;
    private float genero;
    private float materia;
    private float calificacion;
    private static List<SchoolGradingSystem> desempeño_de_estudiantes = new ArrayList<>();

    public SchoolGradingSystem() {
    }

    public SchoolGradingSystem(float nombre, float genero, float materia, float calificacion) {
        this.nombre = nombre;
        this.genero = genero;
        this.materia = materia;
        this.calificacion = calificacion;
    }

    public float getNombre() {
        return nombre;
    }

    public void setNombre(float nombre) {
        this.nombre = nombre;
    }

    public float getGenero() {
        return genero;
    }

    public void setGenero(float genero) {
        this.genero = genero;
    }

    public float getMateria() {
        return materia;
    }

    public void setMateria(float materia) {
        this.materia = materia;
    }

    public float getCalificacion() {
        return calificacion;
    }

    public void setCalificacion(float calificacion) {
        this.calificacion = calificacion;
    }

    public static void readData() {
        SchoolGradingSystem estudiante;
        Scanner entrada = new Scanner(System.in);

        // Generamos las entradas al programa:número de estudiantes al programa
        int numero_de_estudiantes = entrada.nextInt();

        // Generamos la matriz de [número_de_estudiantes][3]
        // float desempeño_de_estudiantes[][] = new float[numero_de_estudiantes][4];

        // Usamos el ciclo for para alimentar la matriz desempeño_de_estudiantes
        for (int fila = 0; fila < numero_de_estudiantes; fila++) {
            // Generamos la lista de entradas: nombre, genero, matería y calificación
            // System.out.println("Ingrese el nombre, genero, matería y calificación.
            // Separados por espacio");
            float nombre = entrada.nextFloat();
            float genero = entrada.nextFloat();
            float materia = entrada.nextFloat();
            float calificacion = entrada.nextFloat();

            estudiante = new SchoolGradingSystem(nombre, genero, materia, calificacion);
            desempeño_de_estudiantes.add(estudiante);

        }

    }

    public static void question1() {

        float sumatoria_de_notas = 0;
        // Calculamos el promedio de las notas, iniciando sumatoria_de_notas=0

        for (int i = 0; i < desempeño_de_estudiantes.size(); i++) {
            // System.out.println(desempeño_de_estudiantes.get(i).getCalificacion());
            sumatoria_de_notas += desempeño_de_estudiantes.get(i).getCalificacion();
        }

        float promedio_calificaciones = sumatoria_de_notas / desempeño_de_estudiantes.size();

        // Se contabiliza el número de notas inferiores al promedio de notas
        int notas_inferiores_a_promedio = 0;

        for (int i = 0; i < desempeño_de_estudiantes.size(); i++) {
            // sumatoria_de_notas += desempeño_de_estudiantes.get(i).getCalificacion();
            if (desempeño_de_estudiantes.get(i).getCalificacion() < promedio_calificaciones) {
                notas_inferiores_a_promedio += 1;
            }

        }

        System.out.println("Notas inferiores al promedio " + notas_inferiores_a_promedio);

    }

    public static void question2() {

        // Se contabiliza el número de notas inferiores al promedio de notas
        int notas_excelentes = 0;

        for (int i = 0; i < desempeño_de_estudiantes.size(); i++) {
            // sumatoria_de_notas += desempeño_de_estudiantes.get(i).getCalificacion();
            if (desempeño_de_estudiantes.get(i).getCalificacion() > 9) {
                notas_excelentes += 1;
            }
        }

        double b = notas_excelentes;
        double c = desempeño_de_estudiantes.size();

        Double porcentaje = (b) / c;
        porcentaje = Math.round(porcentaje * 100) / 100d;

        if (porcentaje == 0) {
            System.out.println("0.00");
        } else {
            System.out.println("Porcentaje superior a excelente " + porcentaje);
        }

    }

    public static void question3() {

        // ¿Cuál es la materia con el mayor numero de examenes reprobados
        // Definimos los contadores para las materias: 1,2 y 3
        int materia_1 = 0;
        int materia_2 = 0;
        int materia_3 = 0;

        for (int i = 0; i < desempeño_de_estudiantes.size(); i++) {
            if (desempeño_de_estudiantes.get(i).getMateria() == 1) {
                if (desempeño_de_estudiantes.get(i).getCalificacion() <= 6) {
                    materia_1 += 1;
                }
            } else if (desempeño_de_estudiantes.get(i).getMateria() == 2) {
                if (desempeño_de_estudiantes.get(i).getCalificacion() <= 6) {
                    materia_2 += 1;
                }
            } else {
                if (desempeño_de_estudiantes.get(i).getCalificacion() <= 6) {
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

    }

    public static void question4() {

        // ¿Cuál es el estudiante con el mejor desempeño para la materia idiomas?
        float mayor_nota = 0f;
        Float estudiante_mejor = 0f;
        for (int i = 0; i < desempeño_de_estudiantes.size(); i++) {
            if (desempeño_de_estudiantes.get(i).getMateria() == 1) {
                if (desempeño_de_estudiantes.get(i).getCalificacion() > mayor_nota) {
                    mayor_nota = desempeño_de_estudiantes.get(i).getCalificacion();
                    estudiante_mejor = desempeño_de_estudiantes.get(i).getNombre();
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
        System.out.println(nombreestudiante);

    }
}
