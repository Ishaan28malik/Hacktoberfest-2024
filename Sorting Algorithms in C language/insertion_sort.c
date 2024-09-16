#include<stdio.h>

//Implimented insertion sort using array

 void insertion_sort(int a[n]) {
 	int temp; //temp is used to swap integers (to hold value temporarily) .
 
 	for(int i = 1; i < n+1; i++) {
 		for(int j = i; j > 0; j--) {
 			if(a[j] < a[j-1]) {
 				temp = a[j-1];
 				a[j-1] = a[j];
 				a[j] = temp;
 			}
 		}
 	}
 	printf("\n\nThe Sorted Array ( using Insertion Sort )  is : ");
	
 	for(int i = 0; i < n; i++) {
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
	
	//CALLING THE FUNCTION FOR INSERTION SORT
	insertion_sort(a);
	
}