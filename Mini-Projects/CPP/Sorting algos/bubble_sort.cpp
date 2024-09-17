#include<iostream>

using namespace std;

void Bubble(int A[], int n)
{
    int i, j, temp;
    for(i=0; i<n-1; i++)
    {
        for(j=0; j<n-i-1; j++)
        {
            if(A[j]>A[j+1])
            {
                temp = A[j];
                A[j] = A[j+1];
                A[j+1] = temp;
            }
        }
    }
    cout<<"\n The array is now sorted in assending order \n";
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
    Bubble(arr, n);
    delete []arr;
    return 0;
}