public class App {
    public static void main(String[] args) throws Exception {
        SchoolGradingSystem reto2 = new SchoolGradingSystem();
        reto2.readData();
        System.out.printf("%.2f%n", reto2.question1());
        System.out.printf("%.2f%n", reto2.question2());
        System.out.println(reto2.question3());
        System.out.println(reto2.question4());
    }
}
