import java.util.Scanner;

public class pattern {
   
    public static void main(String[] args) {

        System.out.println("De cuanto quieres la fila?");
        Scanner sc = new Scanner(System.in);

        int noDeFila = sc.nextInt();
        int FilaCount = noDeFila;

        System.out.println("Esta es la piramide");

        for (int i = 0; i < noDeFila; i++) {
            for (int j = 1; j <= i * 2; j++){
                System.out.print(" ");
            }
            for (int j = 1; j <= FilaCount; j++) {
                System.out.print(j + " ");
            }
            for (int j = FilaCount - 1; j >= 1; j--) {
                System.out.print(j + " ");
            }
            System.out.println();
            FilaCount--;
        }
    }
}
