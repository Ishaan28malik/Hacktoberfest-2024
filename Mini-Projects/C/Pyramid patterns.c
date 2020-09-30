#include<stdio.h>
int main()
{
    int i,j,n,k;
    scanf("%d",&n);
    for(i=1;i<=n;i++)
    {
        for(k=2;k<=i;k++)
        {
            printf(" ");
        }
        for(j=n;j>=i;j--)
        {
            printf("%d",n-j+1);
            
        }
        for(j=n-i;j>=1;j--)
        {
            printf("%d",j);
        }
        printf("\n");
    }
    return 0;
}
