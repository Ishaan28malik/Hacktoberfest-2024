#include<bits/stdc++.h>
using namespace std;

int partition(int arr[], int s, int e, int n)
{
        int start=s;
        int pivot=e;
        int i;
        for(i=s;i<e;i++)
        {
                if(arr[i]<arr[pivot])
                {
                        int temp;
                        temp=arr[i];
                        arr[i]=arr[start];
                        arr[start]=temp;
                        start++;
                }
        }
        int x;
        x=arr[pivot];
        arr[pivot]=arr[start];
        arr[start]=x;
//      int i;
        for(i=0;i<n;i++)
                cout << arr[i] << ' ';
        cout << endl;
        return start;
}

void quicksort(int arr[], int s, int e,int n)
{
        if(s>e)
                return;
        else
        {
                int pivot=partition(arr,s,e,n);
                if(s!=pivot-1)
                        quicksort(arr,s,pivot-1,n);
                if(e!=pivot+1)
                        quicksort(arr,pivot+1,e,n);
        }
}

int main()
{
        int n;
        cin >> n;
        int arr[n];
        int i;
        for(i=0;i<n;i++)
                cin >> arr[i];
        quicksort(arr,0,n-1,n);
//      for(i=0;i<n;i++)
//              cout << arr[i] << ' ';
//      cout << endl;
}
