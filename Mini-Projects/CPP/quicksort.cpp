/*
Write C++ program to store first year percentage of students in array. Sort array of floating
point numbers in ascending order using quick sort and display top five scores.
*/
#include<iostream>
using namespace std;
void quicksort(float x[],int left,int right)
{
	if (left<right)
	{
		int i,j,pivot;
		do
		{
			i=left;
			j=right+1;
			pivot=x[left];
			do {i++;}while(x[i]<pivot);
			do{j--;}while (x[j]>pivot);
			if (i<j) swap (x[i],x[j]);
		}while (i<j);
		swap (x[j],x[left]);
		quicksort(x,left,j-1);
		quicksort(x,j+1,right);
	}
}
int main()
{
	float x[100];
	int n;
	cout<<"Enter total number of students who appeared for the test"<<endl;
	cin>>n;
	cout<<"Start entering their marks"<<endl;
	for (int i=0;i<n;i++)
	{
		cin>>x[i];
	}
	quicksort(x,0,n-1);
	cout<<"The marks scored by students in assending order are "<<endl;
	for (int i=0;i<n;i++)
	{
		cout<<x[i]<<" ";
	}
	cout<<endl;
	cout<<"Marks scored by top 5 students are"<<endl;
	for (int i=n-1;i>n-1-5;i--)
	{
		cout<<x[i]<<" ";
	}
	cout<<endl;
	return 0;
}
