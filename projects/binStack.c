#include "stdio.h"
#include "stdlib.h"
struct xx
{
  int data;
  struct xx *link;
};
struct xx *sp=0,*q;
main()
{
  int n;
  printf("Enter a decimal number :");
  scanf("%d",&n);
  while(n>0)
    {
      if(n==0)
      {
        sp=(struct xx *)malloc(sizeof(struct xx));
        sp->data=n%2;
        sp->link=0;
      }
      else
      {
        q=(struct xx *)malloc(sizeof(struct xx));
        q->link=sp;
        sp=q;
        sp->data=n%2;
      }
      n=n/2;
    }
    while(sp!=0)
    {
      printf("%d ",sp->data);
      sp=sp->link;
    }
}
