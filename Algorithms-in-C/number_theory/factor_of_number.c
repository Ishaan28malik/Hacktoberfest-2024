#include <stdio.h>
int main()
{
    //This program shows factors of the number entered

    int number, i;
    printf("Enter a positive integer: ");
    scanf("%d",&number);
    printf("Factors of %d are: ", number);
    for(i=1; i <= number; ++i)
    {
        if (number%i == 0)
        {
            printf("%d ",i);
        }
    }
    return 0;
}
