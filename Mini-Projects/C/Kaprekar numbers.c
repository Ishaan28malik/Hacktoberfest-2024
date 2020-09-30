#include<stdio.h>
#include<math.h>
int main()
{
    long int i,j,a,b,l,k,s=0,g;
    scanf("%ld\n%ld",&a,&b);
    for(i=a;i<=b;i++)
    {
        l=i*i;//Find the square of a number
        k=i;
        s=0;//Represents the number of digits
        while(k>0)
        {
            k=k/10;
            ++s;
        }
        g=pow(10,s);
        j=l%g+l/g;
        if(j==i)
        {
         printf("%ld ",j);
         a=-1;
        }
    }
    if(a!=-1)
    printf("INVALID RANGE");
    return 0;
}
