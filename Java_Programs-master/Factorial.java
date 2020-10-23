public class Factorial
{
    public static void main(String [] args)
    {
        int number = 5;
        int fact = 1;
        int i;
        for(i = 1; i <= number; i++)
        {
            fact = fact * i;
        }
        System.out.println("\nFactorial of " + number + " is : " + fact);
    }
}
