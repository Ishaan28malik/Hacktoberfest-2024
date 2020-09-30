#include <stdio.h>
int main()
{
    int a,b,i,j,n,l,k;
    scanf("%d\n",&a);
    for(l=1;l<=a;l++)
    {
      scanf("%d\n",&n);
      int arr[n][n];
      for(i=0;i<n;i++)
      {
        for(j=0;j<n;j++)
          scanf("%d ",&arr[i][j]);//Scan The Array
        scanf("\n");
      }
      for(i=0;i<n;i++)
      {
        for(j=0;j<n;j++)
        {
          printf("%d",arr[n-j-1][i]);//Print the array
          if(j!=n-1)
          printf(" ");
        }
        printf("\n");
      }
      printf("\n");
    }
    return 0;
}