#include <stdio.h>
int main()
{
    //this algorithm is used to find product of two numbers
    // this theorem is much more effective than normal multiplication
    int a,b,sum=0;
    printf("please enter numbers :");
    scanf("%d %d",&a,&b);
   
    while(a>0)
    {
        if(a%2==1)
        {
            sum=sum+b;
        }           
        a=a>>1;
        b=b<<1;    
            
    }
     printf("product :%d",sum);
    return 0;
}
