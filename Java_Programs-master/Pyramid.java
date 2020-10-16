package coba;

public class Pyramid {
    public static void main(String[] args) {
        for (int i = 1; i <= 6; i++) {
            for (int j = i; j <= 5; j++){
                System.out.print(" ");
            }

            for (int k = 0; k <= (i * 2) - 2; k++){
                System.out.print("*");
            }

            System.out.println();
        }
    }
}
