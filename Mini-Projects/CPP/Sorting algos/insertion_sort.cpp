#include<iostream>

using namespace std;

void InsertionSort(int A[], int n) 
{
    int i, j, key;
    for (i = 1; i < n; i++) 
    {
        key = A[i];
        j = i-1;
        
        while (j >= 0 && A[j] >key) 
        {
            A[j+1] = A[j];
            j--;
        }
        A[j +1] = key;
        
    }
    cout << "Sorted Array: \n";
    for(i=0; i<n; i++)
    {
        cout<<A[i]<<endl;
    }
}

int main()
{
    int *arr, n;
    cout<<"Enter the size of the array ";
    cin>>n;
    arr = new int[n];
    cout<<"\n Enter the elements into the array \n";
    for(int i=0; i<n; i++)
    {
        cin>>arr[i];
    }
    InsertionSort(arr, n);
    delete []arr;
    return 0;
}