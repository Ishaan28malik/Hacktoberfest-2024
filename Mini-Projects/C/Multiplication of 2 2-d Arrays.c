#multiplication of two array
#include <stdio.h>
int main()
{
    int a,b;
    scanf("%d %d\n",&a,&b);
    int i,j,arr1[a][b],arr2[a][b],arr[a][b];

    for(i=0;i<=a;i++)
    {
        for(j=0;j<=b;j++)
        {
            scanf("%d ",&arr1[i][j]);
        }
    }
    scanf("\n");
    for(i=0;i<=a;i++)
    {
        for(j=0;j<=b;j++)
        {
            scanf("%d ",&arr2[i][j]);
        }
    }
    for(i=0;i<=a;i++)
    {
        for(j=0;j<=b;j++)
        {
            arr[i][j]=arr[i][j]+arr1[i][j]*arr2[j][i];

        }
    }
    for(i=0;i<=a;i++)
    {
        for(j=0;j<=b;j++)
        {
            printf("%d ",arr[i][j]);
        }
        printf("\n");
    }
    return 0;
}