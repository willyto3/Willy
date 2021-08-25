import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class GradingSystem {
    // se declaran las variables
    protected float nombre;
    protected float genero;
    protected float materia;
    protected float calificacion;

    // Declaracion de la lista desempeño de estudiantes para guardar los datos
    protected static List<SchoolGradingSystem> desempeñoDeEstudiantes = new ArrayList<>();

    public GradingSystem() {
    }

    public GradingSystem(float nombre, float genero, float materia, float calificacion) {
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

    @Override
    public String toString() {
        return "GradingSystem [calificacion=" + calificacion + ", genero=" + genero + ", materia=" + materia
                + ", nombre=" + nombre + "]";
    }

    public static void loadData() {
        
    }

    // La clase debe contener 4 métodos, estos métodos no deben recibir ningún
    // parámetro y la salida de estos métodos debe ser el valor que da respuesta a
    // cada uno de las preguntas. Los métodos deben ser nombrados question#, donde #
    // corresponde al número de la pregunta a la cual debe dar respuesta, para este
    // caso serían los números del 1 al 4
    // Realizamos el metodo question1 Notas inferiores al promedio
    public static int stat1() {
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
        return (notasInferioresAPromedio);
    }

    // Realizamos el metodo question2 Porcentaje de notas excelentes
    public static double stat2() {
        // Declaramos un contador de notas excelentes como double para despues hallar el
        // porcentaje
        double notasExcelentes = 0;
        // Recorremos la lista desempeño de estudiantes para comparar el valor de notas
        // excelente con cada una de las notas de la lista
        for (int i = 0; i < desempeñoDeEstudiantes.size(); i++) {
            // Si la nota es superior al valor de 9 la contamos en nuestro contador notas
            // excelentes
            if (desempeñoDeEstudiantes.get(i).getCalificacion() > 9) {
                notasExcelentes += 1;
            }
        }
        // Cambiamos el tamaño de el tamaño de la lista desempeño de estudiantes a
        // double para que no de error en la division
        double c = desempeñoDeEstudiantes.size();
        // Calculamos el porcentaje
        Double porcentaje = notasExcelentes / c;
        // Redondeamos a dos cifras decimales como lo solicita el ejercicio
        porcentaje = Math.round(porcentaje * 100) / 100d;
        // Empanada para colocar 0.00 si el porcentaje da cero
        if (porcentaje == 0) {
            return (0.00);
        } else {
            // Se imprime el valor del porcentaje con dos cifras decimales
            return (porcentaje);
        }
    }

    // Realizamos el metodo question3 Definir la materia con mayor numero de
    // examenes reprobado
    public static String stat3() {
        // Declaramos las constantes Ingles y Historia - Constantes se declaran en
        // Mayuscula Sostenida
        final var INGLES = 1;
        final var HISTORIA = 2;
        // Definimos los contadores para las materias: 1,2 y 3
        int materia_1 = 0;
        int materia_2 = 0;
        int materia_3 = 0;
        // Recorremos la lista desempeño de estudiantes
        for (int i = 0; i < desempeñoDeEstudiantes.size(); i++) {
            // comparamos si la materia es idiomas
            if (desempeñoDeEstudiantes.get(i).getMateria() == INGLES) {
                // Comparamos si la nota esta inferior a 6
                if (desempeñoDeEstudiantes.get(i).getCalificacion() <= 6) {
                    materia_1 += 1;
                }
                // comparamos si la materia es historia
            } else if (desempeñoDeEstudiantes.get(i).getMateria() == HISTORIA) {
                // Comparamos si la nota esta inferior a 6
                if (desempeñoDeEstudiantes.get(i).getCalificacion() <= 6) {
                    materia_2 += 1;
                }
                // comparamos si la materia es literatura
            } else {
                // Comparamos si la nota esta inferior a 6
                if (desempeñoDeEstudiantes.get(i).getCalificacion() <= 6) {
                    materia_3 += 1;
                }
            }
        }
        // Comparamos las cantidades de examenes reprobados de cada materia, para
        // definir la materia con mayor número de examenes reprobados
        if (materia_1 >= materia_2 && materia_1 >= materia_3) {
            return "idiomas";
            // System.out.println("idiomas");
        } else if (materia_2 >= materia_3 && materia_2 > materia_1) {
            return "historia";
            // System.out.println("historia");
        } else {
            return "literatura";
            // System.out.println("literatura");
        }
    }

    // Realizamos el metodo question4 ¿Cuál es el estudiante con el mejor desempeño
    // para la materia idiomas?
    public static String stat4() {
        // Declaramos las constante Ingles - Constantes se declaran en Mayuscula
        // Sostenida
        final var INGLES = 1;
        // declaramos las variables mayor nota y mejor estudiante
        float mayorNota = 0f;
        Float estudianteMejor = 0f;
        // Recorremos la lista desempeño de estudiantes
        for (int i = 0; i < desempeñoDeEstudiantes.size(); i++) {
            // Buscamos las notas de la materia ingles
            if (desempeñoDeEstudiantes.get(i).getMateria() == INGLES) {
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
