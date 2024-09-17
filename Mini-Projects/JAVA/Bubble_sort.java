package searching_and_sorting;

import java.util.Scanner;

public class Bubble_sort {

	static Scanner s = new Scanner(System.in);

	//function to print array
	public static void printArray(int[] arr) {
		for (int element : arr) {
			System.out.print(element + " ");
		}

		System.out.println();
	}
	//end
	
	//bubble sort function
	public static void bubbleSort(int[] arr){
    	for(int i = 0; i< arr.length - 1;i++)
    	{
    		for(int j = 0; j< arr.length - 1; j++)
    		{
    			if(arr[j] > arr[j + 1])
    			{
    				int temp = arr[j];
    				arr[j] = arr[j + 1];
    				arr[j + 1] = temp;
    			}
    		}
    	}
    }  
	//ends

	public static void main(String[] args) {
		int n = s.nextInt();

		int[] arr = new int[n];

		for (int i = 0; i < n; i++) {
			arr[i] = s.nextInt();
		}

		Bubble_sort.bubbleSort(arr);

		printArray(arr);

	}
}
