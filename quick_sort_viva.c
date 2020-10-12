#include<stdio.h>
#include<stdlib.h>
void swap(int* a,int* b)
{
	int temp;
	temp=*a;
	*a=*b;
	*b=temp;
}
int partition(int A[],int start,int end)
{
	int i;
	int pivot=A[end];
	int partitionIndex=start;
	for(i=start;i<end;i++)
	{
		if(A[i]<=pivot)
		{
			swap(&A[i],&A[partitionIndex]);
			partitionIndex++;
		}
	}
	swap(&A[partitionIndex],&A[end]);
	return partitionIndex;
}
void quicksort(int A[],int start,int end)
{
	if(start<end)
	{
		int partitionIndex=partition(A,start,end);
		quicksort(A,start,partitionIndex-1);
	     quicksort(A,partitionIndex+1,end);
	}
}

int main()
{
	int j;
	int A[]={7,2,1,6,8,5,3,4};
	quicksort(A,0,7);
	for(j=0;j<8;j++)
	{
		printf("\n%d\n",A[j]);
	}
}

