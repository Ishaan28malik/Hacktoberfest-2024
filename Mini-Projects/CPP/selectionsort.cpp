#include<bits/stdc++.h>
using namespace std;

int A[10];

void swap(int *x, int *y)
{
	int temp = *x;
	*x = *y;
	*y = temp;
}

void selectionSort(int arr[10])
{
	int min;

	for(int i=0; i<10; i++)
	{
		min = i;

		for(int j=i+1; j<10; j++)
		{
			if(arr[j] < arr[min])
			{
				min = j;
			}
		}

		swap(&arr[min], &arr[i]);
	}
}

void print(int arr[10])
{
	cout<<"The sorted array is:"<<endl;

	for(int i=0; i<10; i++)
	{
		cout<<arr[i]<<" ";
	}
}

void input(int arr[10])
{
	for(int i=0; i<10; i++)
	{
		cin>>arr[i];
	}
}

int main()
{
	input(A);
	selectionSort(A);
	print(A);
	return 0;
}