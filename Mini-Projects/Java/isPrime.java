import java.util.*;
public class isPrime {
    static boolean isPrime(int x) {
        if (x == 2) {
            // 2 is prime
            return true;
        } else if (x % 2 == 0)
            // check if the number is divisible by 2. if it is divisible then its not a
            // prime number!
            return false;
        else if (x == 1) {
            // 1 is neither prime nor composite
            return false;
        }
        // Otherwise: 
        for (int i = 3; i <= Math.sqrt(x); i += 2) {
            if (x % i == 0)
                // if i is factor of x
                return false;
        }
        return true;

    }

    public static void main(String[] args) {
        Scanner myObj = new Scanner(System.in); // Create a Scanner object
        int number = myObj.nextInt();
        // For checking if the given number is prime or not
        if (isPrime(number)) {
            System.out.println("BOOM! its a prime number");
        } else {
            System.out.println("No it is not a prime number!");
        }

    }
}
// This code is contributed by Anoop Gupta
// Time complexity = O(n)