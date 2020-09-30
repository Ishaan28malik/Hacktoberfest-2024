#include<stdio.h>
int main()
{
    int a,b,i,j,t;
    scanf("%d %d\n",&a,&b);
    if(a==b)
    {
     int n,arr[a][b];
     for(i=0;i<a;i++)
     {
        for(j=0;j<b;j++)
        {
            scanf("%d ",&arr[i][j]);
        }
        scanf("\n");
     }
     for(i=0;i<a;i++)
     {
        for(j=0;j<b;j++)
        {
            if(i==j)
            {
               t= arr[i][j];
               arr[i][j]=arr[i][a-j-1];
               arr[i][a-j-1]=t;
            }
        }
     }
     for(i=0;i<a;i++)
     {
        for(j=0;j<b;j++)
        {
            printf("%d ",arr[i][j]);
        }
        printf("\n");
     }
    }
    else
    printf("Diagonal elements are defined in square matrix.");
    return 0;
}