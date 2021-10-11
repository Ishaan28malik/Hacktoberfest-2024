hollow RECTANGULAR PATTERN
import java.util.*;

 public class patterns {
     public static void main(String argc[]) {
         Scanner sc = new Scanner(System.in);
         int a = sc.nextInt();
         for (int i = 1; i < a; i++) {

             for (int j = 1; j <= a; j++) {
                 if (i == 1 || j == a||j == 1 ||i==a-1) {
                     System.out.print("* ");
                 } else {
                    System.out.print("  ");
                 }
             }
            System.out.println("");
         }

    }
 }
