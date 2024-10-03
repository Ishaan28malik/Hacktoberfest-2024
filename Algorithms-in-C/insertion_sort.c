
#include<stdio.h>
#include<stdlib.h>

int main () {

    int n;
    printf("Enter the limit of the array: ");
    scanf("%d",&n);
    int a[n];
    printf("Enter the elements in the array: \n");
    for(int i = 0; i < n; i++){
        scanf("%d",&a[i]);
    }
    int i, key, j,c=0;
    for (i = 1; i < n; i++){
        key = a[i];
        j = i - 1;
        while (j >= 0 && a[j] > key){
            c++;
            a[j+1]=a[j];
            j=j-1;
        }
        a[j+1]=key;
    }
    printf("The Sorted array is: \n");
    for(int i=0; i < n; i++){
        printf("%d ",a[i]);
    }
    printf("\n%d",c );
   return 0; 
}