Pseudocode:-

procedure selection sort 
   list  : array of items
   n     : size of list

   for i = 1 to n - 1
   /* set current element as minimum*/
      min = i    
  
      /* check the element to be minimum */
      for j = i+1 to n 
         if list[j] < list[min] then
            min = j;
         end if
      end for

      /* swap the minimum element with the current element*/
      if indexMin != i  then
         swap list[min] and list[i]
      end if
   end for
	
end procedure


Code:-

#include <stdio.h> 

void swap(int *x, int *y) 
{ 
	int temp = *x; 
	*x = *y; 
	*y = temp; 
} 

void selectionSort(int arr[], int n) 
{ 
	int i, j, min_idx;
	for (i = 0; i < n-1; i++) 
	{ 
		min_idx = i; 
		for (j = (i+1); j < n; j++){
		    if (arr[j] < arr[min_idx]){
		        min_idx = j; 
		    }
		} 
		swap(&arr[min_idx], &arr[i]); 
	} 
} 
