#include<stdio.h>
#include<string.h>
int main()
{
    int i,j,k,n,s,l;
    scanf("%d\n",&l);
    char arr1[]="hackerrank",arr2[10000];
    while(l)
    {
        //(Alternate Method)char *arr2=(char *)malloc(512000*sizeof(char));
        scanf("%s\n",arr2);
        n=strlen(arr2);
        k=0;
        for(i=0;i<n;i++)
        {
            if(arr1[k]==arr2[i])
            {
                k++;
            }
        }
        if(k==10)
        printf("YES\n");
        else
        printf("NO\n");
        l--;
    }
    return 0;
}
