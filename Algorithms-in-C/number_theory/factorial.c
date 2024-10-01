//Factorial of given number using recursion

#include <stdio.h>
#include <conio.h>
 
int factorial(int);
 
int main()
{
    int num;
    int result;
 
    printf("Enter a number to find it's Factorial: ");
    scanf("%d", &num);
    if (num < 0)
    {
        printf("Factorial of negative number not possible\n");
    }
    else
    {
        result = factorial(num);
        printf("The Factorial of %d is %d.\n", num, result);
    }
    return 0;
}
int factorial(int num)
{
    if (num == 0 || num == 1)
    {
        return 1;
    }
    else
    {
        return(num * factorial(num - 1));
    }
}
