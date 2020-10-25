/*
 * C Program Count the Number of Occurrences of an Element in the Linked List 
 * without using Recursion
 */

#include <stdio.h>



int occur(int [], int, int);



int main()

{

    int size, key, count;

    int list[20];

    int i;



    printf("Enter the size of the list: ");

    scanf("%d", &size);

    printf("Printing the list:\n");

    for (i = 0; i < size; i++)

    {

        list[i] = rand() % size;

        printf("%d    ", list[i]);

    }

    printf("\nEnter the key to find it's occurence: ");

    scanf("%d", &key);

    count = occur(list, size, key);

    printf("%d occurs for %d times.\n", key, count);

    return 0;

}



int occur(int list[], int size, int key)

{

    int i, count = 0;



    for (i = 0; i < size; i++)

    {

        if (list[i] == key)

        {

            count += 1;

        }

    }

    return count;

}
