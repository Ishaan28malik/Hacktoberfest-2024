#include<stdio.h>
#include<math.h>
int prime(int n)
{
    for(int i=2;i<=sqrt(n);i++)
    if(n%i==0)
    return 0;
    return 1;
}
int main()
{
    int a,b,n,i;
    scanf("%d %d",&a,&b);
    for(n=a;n<=b;n++)
    {
        i=prime(n);
        if(i==0)
        printf("No\n");
        else
        printf("Yes\n");
    }
    return 0;
}
