import java.util.Scanner;

public class fib {

    public static void main(String args[]) {

        Scanner scanner = new Scanner(System.in);
        System.out.println("How many numbers do you want the sequence to show?");
        int sequenceStop = scanner.nextInt();
        System.out.println("--------------------------------------------------");
        int n1 = 0, n2 = 1, n3, i;
        System.out.println(n1 + "\n" + n2);

        for (i = 2; i < sequenceStop; ++i)
        {
            n3 = n1 + n2;
            System.out.println(n3);
            n1 = n2;
            n2 = n3;
        }

    }
}
