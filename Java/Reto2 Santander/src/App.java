//JORGE SANTANDER

// Reto 2 Curso Programacion Basica MINTIC - Universidad del Norte

// Iniciamos la clase App
public class App {
    // Clase principal MAIN
    public static void main(String[] args) throws Exception {
        // Se llama el metodo readData
        SchoolGradingSystem.readData();
        // Se llama el metodo question1
        SchoolGradingSystem.question1();
        // Se llama el metodo question2
        SchoolGradingSystem.question2();
        // Se llama el metodo question3
        System.out.println(SchoolGradingSystem.question3());
        // Se llama el metodo question4
        System.out.println(SchoolGradingSystem.question4());
    }
}
