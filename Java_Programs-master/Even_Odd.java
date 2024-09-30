import java.util.Scanner;

class CheckEvenOdd
{
  public static void main(String args[])
  {
    int num;
    System.out.println("Enter an integer:");

    //The input provided by the user is stored in num
    Scanner input = new Scanner(System.in);
    num = input.nextInt();

    /* If the number is divisible by 2 then it's an even number
     * else the number is odd*/
    if ( num % 2 == 0 )
        System.out.println("Entered number is even");
     else
        System.out.println("Entered number is odd");
  }
}
