#include<stdio.h>
int main()
{
    int num,rev=0;
    printf("\nEnter the Number : ");
    scanf("%d",&num);
    while(num!=0)
    {
        rev *= 10;
        rev = rev + num%10;
        num /=10;
    }
    printf("\nReverse is : %d",rev);
    return 0;
}
