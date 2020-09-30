#include<stdio.h>
void printSpiral(int r, int c,int a[r][c])
{
  int i=0,j=0,k;
  while(i<r&&j<c)
  {
    for(k=j;k<c;k++)//Print elements of 1st row
      printf("%d\n",a[i][k]);
    i++;
    for(k=i;k<r;k++)
      printf("%d\n",a[k][c-1]);//Print elemnts of last column
    c--;
    if(i<r)
    {
      for(k=c-1;k>=j;k--)
        printf("%d\n",a[r-1][k]);//Print elemnts of last row
      r--;
    }
    if(j<c)
    {
      for(k=r-1;k>=i;k--)
       printf("%d\n",a[k][j]);//Print elements of 1st column
      j++;
    }
  }
}
int main()
{
    int a,b,i,j;
    scanf("%d %d\n",&a,&b);
    int arr[a][b];
    for(i=0;i<a;i++)
    {
        for(j=0;j<b;j++)
        {
            scanf("%d ",&arr[i][j]);
        }
        scanf("\n");
    }
    printSpiral(a,b,arr);
    return 0;
}