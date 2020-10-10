#include<stdio.h>

//QUICK SORT

int partition(int *a, int start, int end) {
	int pivote, p_index, temp;
	
	pivote = a[end];
	p_index = start;
	
	for(int i = start; i < end; i++) {
		if(a[i] < pivote) {
			temp = a[i];
			a[i] = a[p_index];
			a[p_index] = temp;
			
			++p_index;
		}
	}
	temp = a[p_index];
	a[p_index] = a[end];
	a[end] = temp;
	
	return p_index;
}

void quickSort(int a[], int start, int end) {
	int p_index;
	
	if (start >= end) {
		return;
	}
	
	p_index = partition(a, start, end);
	
	quickSort(a, start, p_index - 1);
	quickSort(a, p_index + 1, end);
}

void quick_sort_func(int a[]) {
	quickSort(a, 0, n);
	
	// printing the sorted array
	
	printf("\n\nThe Sorted array ( using Quick Sort ) is : ");
	
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
	
	printf("\nThe Given Array before sorting : ");
	
	 for(int i = 0; i < n; i++) {
 		printf("%d ",a[i]);
 	}
		
	//CALLING THE FUNCTION FOR QUICK SORT
	quick_sort_func(a);
	
}
