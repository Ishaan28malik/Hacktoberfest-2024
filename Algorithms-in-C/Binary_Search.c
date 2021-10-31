#include<stdio.h>
int main()
{
  int  i, j,a[100], n,temp;
  printf("Enter the length of your array : ");
  scanf("%d",&n);
  for( i=0;i<n;i++)
  {
    printf("Enter the elements : %d :",i+1);
    scanf("%d",&a[i]);
  }
  for (i = 0; i < n-1; i++)
                for (j = 0; j < n-i-1; j++)
                            if (a[j] > a[j+1])
          {
            temp = a[j];
            a[j] = a[j+1];
            a[j+1] = temp;
          }
  printf("\nThe sorted array");
  for(int i=0;i<n;i++)
        {
                printf("\n The element at : %d :",i+1);
    printf(" %d ",a[i]);
        }
  int ele,rtn=-1;
  printf("\nEnter the element you want to search : ");
        scanf("%d",&ele);
  //binary search
   int f=0,l=n-1;
        int mid=(f+l)/2;
        for( i=0;f<l;i++)
        {
    if(ele<a[mid])
                {
                        l=mid;
                        mid=(f+l)/2;
                }
                else if(ele >a[mid])
                {
                        f=mid+1;
                        mid=(f+l)/2;
    }
                else if(ele==a[mid])
                {
                        rtn=1;
                        break;

                }
  }
if(rtn==1)
{
  printf("\nThe element is found");
  printf("position is: %d \n",mid+1);

}
else
{
   printf("\n The element is not found \n");
}
}
