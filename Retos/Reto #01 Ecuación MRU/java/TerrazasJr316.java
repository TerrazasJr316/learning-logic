import java.util.Scanner;

public class TerrazasJr316 {

    public static void main(String[] args) {
        @SuppressWarnings("resource")
        Scanner scanner = new Scanner(System.in);

        System.out.println("Introduce la velocidad: ");
        float speed = scanner.nextFloat();

        System.out.println("Introduce el tiempo");
        float time = scanner.nextFloat();

        float distance = speed + time;

        System.out.println("La distancia es de: " + distance);
    }
}