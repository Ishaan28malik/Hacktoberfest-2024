//C Program for Insertion Sort
#include <stdio.h>
#include <math.h>
void insertion_sort(int a[], int size){
    int i,j;

    for(i=0;i<size;i++)
    {
        j = i;

        //i is not the first element
        while(j>0)
        {
            //not in order
            if(a[j-1] > a[j])
            {
                //swapping
                int temp = a[j-1];
                a[j-1] = a[j];
                a[j] = temp;
            }
            //in order
            else
            {
                break;
            }
            j--;
        }
    }
}
// Function to print an array 
void printArray(int A[], int size) 
{ 
    int i; 
    for (i=0; i < size; i++) 
        printf("%d ", A[i]); 
    printf("\n"); 
} 
//Driver Program to test above functions
int main()
{
    int a[] = {16, 19, 11, 15, 10, 12, 14};
    int size = sizeof(a)/sizeof(a[0]);
    printf("Given array is \n"); 
    printArray(a,size);
    insertion_sort(a,size);
    printf("\nSorted array is \n"); 
    printArray(a,size);
    return 0;
}