#include<stdio.h>

int main(void)
{
    int n, array[25], s, count = 0;

    printf("Enter the number of entries: ");
    scanf("%d", &n);
    printf("Enter the %d elements: ", n);
    //user-input
    for(int i = 0; i < n; i++)
    {
        scanf("%d", &array[i]);
    }
    printf("Enter the number to be searched: ");
    scanf("%d", &s);
    printf("\n");
    //traversing in the array to search the number
    //also the position is returned
    for (int i = 0; i < n; i++)
    {
        if(array[i] == s)
        {
            printf("NUMBER FOUND.\n");
            if((count + 1)%10 == 1)
            {
                printf("Location: %dst element of array\n", count + 1);
            }
            else if((count + 1)%10 == 2)
            {
                printf("Location: %dnd element of array\n", count + 1);
            }
            else if((count + 1)%10 == 3)
            {
                printf("Location: %drd element of array\n", count + 1);
            }
            else
            {
                printf("Location: %dth element of array\n", count + 1);
            }
        }
        else
        if (count == n - 1)
        {
            printf("Search completed. Number not found\n");
        }
        else
        {
            count++;
        }
    }   
}