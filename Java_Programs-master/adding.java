// program adds two numbers from input

import java.util.Scanner;
class adding{
    public static void main(String[] args){
        int x, y, total;
        Scanner user = new Scanner(System.in);
        System.out.println("Enter a number: ");
        x = user.nextInt();
        System.out.println("Enter another number: ");
        y = user.nextInt();
        total = x + y;
        System.out.println("Sum is: " + total);
    }
}