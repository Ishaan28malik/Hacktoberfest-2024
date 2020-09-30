#include<stdio.h>
#include<string.h>
int main()
{
    int i,j,n,s,l;
    char arr[]="abcdefghijklmnopqrstuvwxyz";
    {
        char str[1000];       
        gets(str);
        n=strlen(str);
        int k=0;
        for(i=0;i<n;i++)
        {
            l=k;
            for(j=0;j<n;j++)
            {
              if(str[j]==arr[k]||str[j]==(arr[k]-32))
              {
                  k++;
                  break;//to avoid addition of one character
              }  
            }
            if(k==l)
            break;//character is not found
        }
        if(k==26)
        printf("pangram");
        else
        printf("not pangram");
    }
    return 0;
}
