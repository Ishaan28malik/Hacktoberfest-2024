#include<iostream>  
using namespace std;  
int main ()  
{    
	int n;
	cout << "Enter number of elements: ";
	cin >> n;
    int *arr = new int [n];
    cout<<"\nEnter "<< n <<" elements\n";
    for(int i = 0; i < n; i++)
    	cin >> arr[i];
    cout<<"\nOriginal List\n";
    for(int i=0;i<n;i++)  
        cout <<arr[i]<<" ";  
    for(int i=1; i<n; i++)   
    {  
        int temp = arr[i];  
        int j= i-1;  
        while(j>=0 && temp <= arr[j])  
        {  
            arr[j+1] = arr[j];   
            j = j-1;  
        }  
        arr[j+1] = temp;  
    }  
    cout<<"\nSorted List in Ascending Order\n";
    for(int i=0;i<n;i++)  
        cout <<arr[i]<<" ";
     for(int i=1; i<n; i++)   
    {  
        int temp = arr[i];  
        int j= i-1;  
        while(j>=0 && temp >= arr[j])  
        {  
            arr[j+1] = arr[j];   
            j = j-1;  
        }  
        arr[j+1] = temp;  
    }  
    cout<<"\nSorted List in Descending Order\n";
    for(int i=0;i<n;i++)  
        cout <<arr[i]<<" ";
}  