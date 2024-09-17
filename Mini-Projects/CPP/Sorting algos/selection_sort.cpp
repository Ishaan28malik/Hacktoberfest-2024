#include <iostream>
using namespace std;

void swap(int *x,int *y)
{
    int temp=*x;
    *x=*y;
    *y=temp;
}
void SelectionSort(int A[],int n)
{
    int i,j,k;
    for(i=0;i<n-1;i++)
    {
        for(j=k=i;j<n;j++)
        {
            if(A[j]<A[k])
            k=j;
        }
        swap(&A[i],&A[k]);
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
    SelectionSort(arr, n);
    delete []arr;
    return 0;
}