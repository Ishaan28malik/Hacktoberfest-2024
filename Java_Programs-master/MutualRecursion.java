import java.util.Scanner;

public class MutualRecursion {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Enter the number : ");
        int n = scanner.nextInt();

        if(even(n)){
            System.out.println(n + " is even number.");
        }
        else {
            System.out.println(n + " is odd number.");
        }
        scanner.close();
    }

    public static boolean even(int n){
        if(n==0)
            return true;
        else
            return odd(n-1);
    }

    public static boolean odd(int n){
        if(n==0)
            return false;
        else
            return even(n-1);
    }

}
