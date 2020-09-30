#include <stdio.h>
int main()
{
    int a,b,i,j,n,l,k;
    scanf("%d\n",&a);
    for(l=1;l<=a;l++)
    {
      scanf("%d\n",&n);
      int arr[n][n],arr1[n][n];
      for(i=0;i<n;i++)
      {
        for(j=0;j<n;j++)
          scanf("%d ",&arr[i][j]);//Scan The Array
        scanf("\n");
      }
      for(i=0;i<n/2;i++)//n/2= no of cycles assume in case of 3X3 matrix cycle is in cycle runs only one time but in 4X4 matrix cycle runs 2 times
      {
        for(j=i;j<n-i-1;j++)
        {
          int t=arr[i][j];//Its same as as we copy the elements in other 2-d array but instead u can use swapping also though it is tough to remember but remember only the logic
          arr[i][j]=arr[n-j-1][i];
          arr[n-j-1][i]=arr[n-i-1][n-j-1];
          arr[n-i-1][n-j-1]=arr[j][n-i-1];
          arr[j][n-i-1]=t;
        } 
      }
      for(i=0;i<n;i++)
      {
        for(j=0;j<n;j++)
        {
          printf("%d",arr[i][j]);//Print the array
          if(j!=n-1)
          printf(" ");
        }
        printf("\n");
      }
      printf("\n");
    }
    return 0;
}