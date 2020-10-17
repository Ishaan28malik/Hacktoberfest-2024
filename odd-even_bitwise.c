/*we find odd even using bitwise 
  and operator*/

#include<stdio.h>

void main()
{
    int ary[]={10,11};
    int c;

    for(int i=0;i<=(sizeof(ary)/sizeof(int));++i)
    {
        c= ary[i]&1;
        if(c!=0)
        {
            printf("\nThe number %d is odd:",ary[i]);
        }
        else
        {
            printf("\nThe number %d is even:",ary[i]);
        }
        
    }
}
