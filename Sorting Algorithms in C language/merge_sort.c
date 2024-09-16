#include<stdio.h>

//MERGE SORT 

void merge(int *a, int low, int high) {
	int mid = (low + high) / 2;
	
	int i = low;
	int j = mid+1;
	int k = low;
	
	int temp[n+1];
	
	while(i <= mid && j <= high) {
		if(a[i] < a[j]) {
			temp[k++] = a[i++];
		} else {
			temp[k++] = a[j++];
		}
	} 
	
	while(i <= mid) {
		temp[k++] = a[i++];
	}
	while(j <= high) {
		temp[k++] = a[j++];
	}
	
	for(int l = low; l <=high; l++) {
		a[l] = temp[l];
	}
	
}

void merge_sort(int a[],int low, int high) {
	int mid;
	
	if(low >= high) {
		return;
	}
	mid = (low + high) / 2;
	
	merge_sort(a, low, mid);
	merge_sort(a, mid+1 , high);
	merge(a, low, high);	
}

void merge_sort_func(int a[]) {
	merge_sort(a, 0, n-1);
	// printing the sorted array
	
	printf("\n\nThe Sorted array ( using Merge Sort ) is : ");
	
	for(int i=0; i < n; i++) {
		printf("%d ",a[i]);
	}
	
	printf("\n\n");		
}


void main() {
	printf("Total number of integers to be sorted: ");
	scanf("%d", &n);

	int a[n];
	
	printf("\n Enter the integers to be sorted: ");
	
	for(int i = 0; i < n; i++) {
		scanf("%d",&a[i]);
	}
	
	//CALLING THE FUNCTION FOR MERGE SORT
	merge_sort_func(a);	
		
}

