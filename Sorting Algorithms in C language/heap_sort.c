//HEAP SORT

void maxHeap(int a[], int N, int i) {
	int temp;
	int largest = i;
	int l = 2*i + 1;
	int r = 2*i + 2;
	
	if(l < N  && a[l] > a[largest]) {
		largest = l;
	}
	if(r < N && a[r] > a[largest]) {
		largest = r;
	}
	
	if(largest != i) {
		temp = a[i];
		a[i] = a[largest];
		a[largest] = temp;
		
		maxHeap(a, N, largest);
	}
}

void heap_sort(int a[]) {
	int temp;

	for(int i = (n / 2) - 1; i >= 0; i--) {
		maxHeap(a, n, i);
	}
	
	for(int i =  n - 1; i > 0; i--) {
		temp = a[0];
		a[0] = a[i];
		a[i] = temp;
		
		maxHeap(a, i, 0);
	}
	
	// printing the sorted array
	
	printf("\n\nThe Sorted array ( Using Heap sort ) is : ");
	
	for(int i=0; i < n; i++) {
		printf("%d ",a[i]);
	}
	
	printf("\n\n");		
}

//MAIN FUNCTION

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
	
	//CALLING THE FUNCTION FOR HEAP SORT
	heap_sort(a);
}