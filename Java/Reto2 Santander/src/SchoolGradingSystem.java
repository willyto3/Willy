//JORGE SANTANDER

// Reto 2 Curso Programacion Basica MINTIC - Universidad del Norte

// Se declaran las importaciones
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

// Se utiliza el metodo de camello para declarar todas las variables ejemplo unaVariable
// Se debe implementar todo el procesamiento de información y cálculos en una clase llamada SchoolGradingSystem.
public class SchoolGradingSystem {
    // se declaran las variables
    private float nombre;
    private float genero;
    private float materia;
    private float calificacion;
    // Declaracion de la lista desempeño de estudiantes para guardar los datos
    private static List<SchoolGradingSystem> desempeñoDeEstudiantes = new ArrayList<>();

    // Se genera el constructor Vacio
    public SchoolGradingSystem() {
    }

    // Se genera el contructor de las variables
    public SchoolGradingSystem(float nombre, float genero, float materia, float calificacion) {
        this.nombre = nombre;
        this.genero = genero;
        this.materia = materia;
        this.calificacion = calificacion;
    }

    // Metodo get de la variable nombre
    public float getNombre() {
        return nombre;
    }

    // Metodo set de la variable nombre
    public void setNombre(float nombre) {
        this.nombre = nombre;
    }

    // Metodo get de la variable genero
    public float getGenero() {
        return genero;
    }

    // Metodo set de la variable genero
    public void setGenero(float genero) {
        this.genero = genero;
    }

    // Metodo get de la variable materia
    public float getMateria() {
        return materia;
    }

    // Metodo set de la variable materia
    public void setMateria(float materia) {
        this.materia = materia;
    }

    // Metodo get de la variable calificacion
    public float getCalificacion() {
        return calificacion;
    }

    // Metodo set de la variable calificacion
    public void setCalificacion(float calificacion) {
        this.calificacion = calificacion;
    }

    // La clase SchoolGradingSystem debe contener un método llamado readData,
    // el cual no debe recibir ni retornar ningún parámetro.
    // El objetivo de este método es leer los valores de entrada del programa.
    public static void readData() {
        // Se declara el objeto estudiante de la clase SchoolGradingSystem
        SchoolGradingSystem estudiante;
        // Se genera el Scanner entrada para recopilar los datos
        Scanner entrada = new Scanner(System.in);
        // Generamos las entradas al programa:número de calificaciones
        int numeroDeCalificaciones = entrada.nextInt();
        // Usamos el ciclo for para solicitar los datos
        for (int fila = 0; fila < numeroDeCalificaciones; fila++) {
            float nombre = entrada.nextFloat();
            float genero = entrada.nextFloat();
            float materia = entrada.nextFloat();
            float calificacion = entrada.nextFloat();
            // creamos un objeto de la clase SchoolGradingSystem
            estudiante = new SchoolGradingSystem(nombre, genero, materia, calificacion);
            // Añadimos el objeto creado a la lista de objetos de la clase
            // SchoolGradingSystem
            desempeñoDeEstudiantes.add(estudiante);
        }
    }

    // La clase debe contener 4 métodos, estos métodos no deben recibir ningún
    // parámetro y la salida de estos métodos debe ser el valor que da respuesta a
    // cada uno de las preguntas. Los métodos deben ser nombrados question#, donde #
    // corresponde al número de la pregunta a la cual debe dar respuesta, para este
    // caso serían los números del 1 al 4
    // Realizamos el metodo question1 Notas inferiores al promedio
    public static void question1() {
        // Declaramos un acumulador de notas
        float sumatoriaDeNotas = 0;
        // Calculamos el promedio de las notas. recorriendo la lista desempeño de
        // estudiantes
        for (int i = 0; i < desempeñoDeEstudiantes.size(); i++) {
            sumatoriaDeNotas += desempeñoDeEstudiantes.get(i).getCalificacion();
        }
        // Calculamos el promedio de las calificaciones division de la sumatoria de
        // notas entre el tamaño de la lista desempeño de estudiantes
        float promedioCalificaciones = sumatoriaDeNotas / desempeñoDeEstudiantes.size();
        // Declaramos un contador de notas inferiores al promedio
        int notasInferioresAPromedio = 0;
        // Recorremos la lista desempeño de estudiantes para comparar el promedio de
        // notas con cada una de las notas de la lista
        for (int i = 0; i < desempeñoDeEstudiantes.size(); i++) {
            // Si la nota es inferior al promedio la contamos en nuestro contador notas
            // inferiores al promedio
            if (desempeñoDeEstudiantes.get(i).getCalificacion() < promedioCalificaciones) {
                notasInferioresAPromedio += 1;
            }
        }
        // Se imprime la cantidad de notas inferiores al promedio
        System.out.println(notasInferioresAPromedio);
    }

    // Realizamos el metodo question2 Porcentaje de notas excelentes
    public static void question2() {
        // Declaramos un contador de notas excelentes como double para despues hallar el
        // porcentaje
        int notasExcelentes = 0;
        // Recorremos la lista desempeño de estudiantes para comparar el valor de notas
        // excelente con cada una de las notas de la lista
        for (int i = 0; i < desempeñoDeEstudiantes.size(); i++) {
            // Si la nota es superior al valor de 9 la contamos en nuestro contador notas
            // excelentes
            if (desempeñoDeEstudiantes.get(i).getCalificacion() > 4.5) {
                notasExcelentes += 1;
            }
        }

        System.out.println(notasExcelentes);
    }

    // Realizamos el metodo question3 ¿Cuál es la materia con el peor desempeño
    // promedio para el género masculino?
    public static String question3() {

        // Definimos los contadores para las materias: 1,2 y 3
        float materia1 = 0;
        float materia2 = 0;
        float materia3 = 0;
        // Definimos los acumuladores de notas para las materias: 1,2 y 3
        float acumulador_nota_1 = 0;
        float acumulador_nota_2 = 0;
        float acumulador_nota_3 = 0;

        for (int fila = 0; fila < desempeñoDeEstudiantes.size(); fila++) {
            if (desempeñoDeEstudiantes.get(fila).getGenero() == 0) {
                if (desempeñoDeEstudiantes.get(fila).getMateria() == 1) {
                    materia1++;
                    acumulador_nota_1 += desempeñoDeEstudiantes.get(fila).getCalificacion();
                } else if (desempeñoDeEstudiantes.get(fila).getMateria() == 2) {
                    materia2++;
                    acumulador_nota_2 += desempeñoDeEstudiantes.get(fila).getCalificacion();
                } else {
                    materia3++;
                    acumulador_nota_3 += desempeñoDeEstudiantes.get(fila).getCalificacion();
                }
            }
        }
        // Calculamos promedio de cada materia
        float promedio_nota_1 = acumulador_nota_1 / materia1;
        float promedio_nota_2 = acumulador_nota_2 / materia2;
        float promedio_nota_3 = acumulador_nota_3 / materia3;

        // Se determina el peor promedio, buscando el promedio de la materia con el
        // menor valor
        if (promedio_nota_1 < promedio_nota_2 && promedio_nota_1 < promedio_nota_3) {
            return ("literatura");
        } else if (promedio_nota_2 < promedio_nota_1 && promedio_nota_2 < promedio_nota_3) {
            return ("biologia");
        } else {
            return ("geografia");
        }

    }

    // Realizamos el metodo question4 ¿Cuál es el estudiante con el mejor desempeño
    // para la materia literatura?
    public static String question4() {
        // Declaramos las constante Literatura - Constantes se declaran en Mayuscula
        // Sostenida
        final var LITERATURA = 1;
        // declaramos las variables mayor nota y mejor estudiante
        float mayorNota = 0f;
        Float estudianteMejor = 0f;
        // Recorremos la lista desempeño de estudiantes
        for (int i = 0; i < desempeñoDeEstudiantes.size(); i++) {
            // Buscamos las notas de la materia Literatura
            if (desempeñoDeEstudiantes.get(i).getMateria() == LITERATURA) {
                // Buscamos la nota mayor
                if (desempeñoDeEstudiantes.get(i).getCalificacion() > mayorNota) {
                    // Asignamos el dato a la mayor nota y al numero del mejor estudiante
                    mayorNota = desempeñoDeEstudiantes.get(i).getCalificacion();
                    estudianteMejor = desempeñoDeEstudiantes.get(i).getNombre();
                }
            }
        }
        // inicializamos la variable nombre estudiante
        var nombreestudiante = "";
        // Usamos el metodo Switch para buscar el mejor estudiante
        switch (Math.round(estudianteMejor)) {
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
        // Imprimimos el nombre del mejor estudiante
        return nombreestudiante;
    }
}