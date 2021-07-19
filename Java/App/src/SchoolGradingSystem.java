import java.util.Scanner;

public class SchoolGradingSystem {
    private float nombre;
    private float genero;
    private float materia;
    private float calificacion;

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
    }

    public static void question1() {

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
    }

    public static void question2() {

    }

    public static void question3() {

    }

    public static void question4() {

    }

}
