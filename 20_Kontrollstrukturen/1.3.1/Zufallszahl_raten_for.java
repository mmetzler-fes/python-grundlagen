import java.util.Random;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Random random = new Random();
        double x = random.nextDouble();
        int zahl = (int) (x * 10) + 1;
        boolean erfolg = false;
        for (int versuche = 1; versuche <= 5; versuche++) {
            Scanner scanner = new Scanner(System.in);
            System.out.print("Rate meine Zahl zwischen 1 und 10: ");
            String eingabe = scanner.nextLine();
            versuche += 1;
            if (zahl > Integer.parseInt(eingabe)) {
                System.out.println("Meine Zahl ist größer");
            } else if (zahl < Integer.parseInt(eingabe)) {
                System.out.println("Meine Zahl ist kleiner");
            } else {
                System.out.printf("Super. Richtig geraten in %d Versuchen%n", versuche);
                erfolg = true;
                break;
            }
        }
        if (!erfolg) {
            System.out.println("Du hast das Spiel leider verloren");
        }
    }
}