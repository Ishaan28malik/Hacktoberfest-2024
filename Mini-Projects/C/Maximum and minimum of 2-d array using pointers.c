#include<stdio.h>
#include<limits.h>
#define a INT_MIN
#define b INT_MAX
int main()
{
    int i,j,m,n,s,l;
    int (*p)[n];//Initialise the pointer for 2-d array
    scanf("%d %d\n",&m,&n);
    int arr[m][n];
    p=&arr[0];//Assigning the base address of 2-d array to pointer
    for(i=0;i<m;i++)
    {
        for(j=0;j<n;j++)
        {
            scanf("%d ",&arr[i][j]);
        }
        scanf("\n");
    }
    for(i=0;i<m;i++)
    {
        s=a;
        l=b;
        for(j=0;j<n;j++)
        {
           if(*(*p+i*n+j)>s)
           s=*(*p+i*n+j);
           if(*(*p+i*n+j)<l)
           l=*(*p+i*n+j);
        }
            printf("Max and Min Elements in a row are:%d and %d respectively.\n",s,l);
    }
    return 0;
}