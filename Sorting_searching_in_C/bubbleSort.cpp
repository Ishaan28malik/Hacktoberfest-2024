#include<stdio.h>

int main(void)
{
    int array[25], n, swap;
    //user-input
    printf("Number of entries: ");
    scanf("%d", &n);
    printf("Enter the %d entries: \n", n);
    
    for (int i = 0; i < n; i++)
    {
       scanf("%d", &array[i]);
    }
    
    int j = 0;
    while(j != n-1)
    {
        for (int i = 0; i < n; i++)
        {
            if (i == n-1)
            {
                continue;
            }
            else
            if (array[i] > array[i+1])
            {
                //swapping the elements
                swap = array[i];
                array[i] = array[i + 1];
                array[i + 1] = swap;
            }
        }
        j++;
    }
    //printing the sorted array
    printf("The sorted array is: \n");
    for (int i = 0; i < n; i++)
    {
        printf("%d\n", array[i]);
    }
}
