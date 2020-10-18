import java.util.Arrays;
public class Sort{

     public static void main(String []args)
     {
        int arr[] = {4,6,21,9,1};
        System.out.println("Before Sorting");
        printArray(arr);
        Sort obj = new Sort();
         obj.insertionSort(arr);
         System.out.println();
         System.out.println("After Sorting");
         printArray(arr);
        // with Array method no need of printArray() to print sorted array
        // System.out.println(Arrays.toString(arr));
     }
     static void insertionSort(int arr[])
     {  int n = arr.length;    
         for(int i=1; i<n; i++)
         {    int key = arr[i];
             int j = i-1;
             while(j>=0 && arr[j]>key)
             {    arr[j+1] = arr[j];
                  j--;
             } 
             arr[j+1] = key;      }
     }
     
     static void printArray(int arr[])
     {  int n = arr.length;
        System.out.print("{");
        for(int i=0;i<n;i++) {
             System.out.print(arr[i]+" ");
         }  System.out.print("}");
     }
     
}