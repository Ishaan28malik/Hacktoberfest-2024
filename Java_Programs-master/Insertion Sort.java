import java.util.Arrays; 

public class Pattern { public static void main(String args[]) { 

int[] unsorted = { 32, 23, 45, 87, 92, 31, 19 }; 
System.out.println("integer array before sorting : " + Arrays.toString(unsorted)); 
insertionSort(unsorted); 
System.out.println("integer array after sorting : " + Arrays.toString(unsorted)); } 


public static void insertionSort(int[] unsorted) { 
for (int i = 1; i < unsorted.length; i++) { 
  int current = unsorted[i]; 
  int j = i;  
  
  while (j > 0 && unsorted[j - 1] > current) { 
    unsorted[j] = unsorted[j - 1]; j--; } 
    
  unsorted[j] = current; 
  } 
 }
}
