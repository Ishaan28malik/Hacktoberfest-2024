#include<iostream>
using namespace std;

void insertionSort(int a[],int n){
    int temp,j;
    for (int i = 1; i < n; i++) //till no. of passes and incremenent this loop for unsorted array
    {
        temp = a[i]; //assigning first element of unsorted array as temp
        j = i-1;  // decrement this loop for sorted array!
        
        while (j>=0 && a[j]>temp) //comparisons are done here
        {
            a[j+1] = a[j]; //right shift elements
            j--;
        }
        a[j+1] = temp; //correct position found !
    }
    cout<<"Sorted array:\n";
    for (int i = 0; i < n; i++)
    {
        cout<<a[i] << endl;
    }
}
int main()
{
    int arr[] = {5,4,10,1,6,2};
    int size = sizeof(arr)/sizeof(arr[0]);
    // cout<<size;
    insertionSort(arr,size);
    return 0;
}

// Best case- O(n) 
// Worst case- O(n^2) 
