package searching_and_sorting;

import java.util.Scanner;

public class Selection_sort {
	
	static Scanner s = new Scanner(System.in);

	//function to take input
		public static int[] takeInput(){
			
			int size = s.nextInt();
			int[] input = new int[size];
			for(int i = 0; i < size; i++){
				input[i] = s.nextInt();
			}
			return input;
		}
		//end
		
		//function to sort
		public static void selectionSort(int [] arr)
		{
			for(int i = 0; i < arr.length - 1; i++)
			{
				int min = arr[i];
				int minIndex = i;
				
				for(int j = i + 1; j < arr.length; j++)
				{
					if(arr[j] < min)
					{
						min = arr[j];
						minIndex = j;
					}
				}
					if(minIndex != i)
					{
						arr[minIndex] = arr[i];
						arr[i] = min;
					}
			}
		}
		//end
		
		//function to print array
		public static void printArray(int[] arr) {	
			for (int i = 0; i < arr.length; i++) {
				System.out.print(arr[i] + " ");
			}

			System.out.println();
		}
		//end
		
		
	public static void main(String[] args) {
		
		int[] arr = takeInput();
		selectionSort(arr);
		printArray(arr);
	}

}
