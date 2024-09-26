#include<stdio.h>

//function definition
//as we know that binary search requires array to be sorted beforehand here bubble sort is used first
int search(int mid, int arr[], int m, int num);

int main(void)
{
    int array[25], n = 0, count = 0, swap, mid, start = 0, s;
    //bubble sorting
    printf("NOTE: You can add the entries in random order.\n");
    //user-input
    printf("Number of entries: ");
    scanf("%d", &n);
    int end = n - 1;
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
                swap = array[i];
                array[i] = array[i + 1];
                array[i + 1] = swap;
            }
        }
        j++;
    }

    //As now the array is sorted start binary search
    printf("Your array is sorted now.\n");
    printf("Enter the number to be serached: ");
    scanf("%d", &s);
    mid = start + (end - start)/2;
    search(mid, array, n, s); //function call
}
//The main binary search
int search(int mid, int arr[], int m, int num)
{
    int new_mid, beg, end, count = 0;
    {
        //starting from the middle
        if (arr[mid] == num)
        {
            printf("Number found\n");
            count = mid;
            printf("Location: %d\n", count);

        }
        //if the number to be searched is less than the number in the middle of array move to left-mid of array
        else if(num < arr[mid])
        {
            beg = 0;
            end = mid;
            new_mid = beg + (end - beg)/2;
            search(new_mid, arr, m, num);
        }
        //if them number to be searched is less than the number in the middle of array move to right-mid of array
        else if(num > arr[mid])
        {
            beg = mid;
            end = m-1;
            new_mid = beg + (end - beg)/2;
            if(num == arr[m-1])
            {
                printf("Number found\n");
                printf("Location: %d\n", m-1);
                goto exit; //base case
            }
            //recursive statement
            search(new_mid, arr, m, num);
        }
        else
        {
            printf("The number is not there.");
        }
    }
exit:
    return 0;
}