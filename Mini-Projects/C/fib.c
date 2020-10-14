#include <stdio.h>
#include <stdlib.h>

int main()
{
 int x,t;
 printf("enter the number you want");
 scanf("%d",&x);
 if(x<0)
 {
     printf("not a possible number");
 }
 else
 {
     for(t=0;t<=x;t++)
     {
     printf("the %d series is %d\n",t,fib(t));
     }
 }

}

int fib(int n)
{
    if(n<=1)
    {
        return n;

    }
    else
    {
        return fib(n-1)+fib(n-2);
    }
}


