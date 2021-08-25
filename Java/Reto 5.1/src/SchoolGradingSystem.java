//WILLY CORZO

// Reto 2 Curso Programacion Basica MINTIC - Universidad del Norte

// Iniciamos la clase App
public class SchoolGradingSystem {
    // Clase principal MAIN
    public static void main(String[] args) throws Exception {
        // Se llama el metodo readData
        Student.loadData();
        // Se llama el metodo question1
        System.out.println(Student.stat1());
        // Se llama el metodo question2
        System.out.println(Student.stat2());
        // Se llama el metodo question3
        System.out.println(Student.stat3());
        // Se llama el metodo question4
        System.out.println(Student.stat4());
    }
}
