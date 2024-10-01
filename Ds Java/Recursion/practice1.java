package Ds.Recursion;

import java.util.Scanner;

public class practice1 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int arr[] = {1,6,3,4,5};
		System.out.println(sorted(arr,5));

	}
   static boolean sorted(int arr[],int n) {
	  if(n==1) {
		  return true;
	  }
      if(arr[n-1]>arr[n-2])
          return sorted(arr, n-1);
      else 
          return false;
   }
}
