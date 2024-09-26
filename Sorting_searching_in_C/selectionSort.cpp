#include<stdio.h>   

int main(void)

{
    int array[25], small_num, n;

    printf("Number of entries: ");
    scanf("%d", &n);
    
    printf("Enter the %d elements: ", n);
    //user-input
    for(int i = 0; i < n; i++)
    {
        scanf("%d", &array[i]);
    }
    //the main algo of selection-sort
    for(int i = 0; i < n; i++)
    {
        for(int j = i+1; j < n; j++)
        {
            if(array[i] > array[j])
            {
                //swapping the entries
                small_num = array[j];
                array[j] = array[i];
                array[i] = small_num;
            }
            else
            {
                continue;
            }
        }
    }
    //printing the sorted array
    printf("The sorted array is: \n");
    for(int i = 0; i < n; i++)
    {
        printf("%d\n", array[i]);
    }

}