package Ds.Recursion;

import java.util.Scanner;

public class practice3 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		 int [] arr = {4,2,1,2,5,2,7};
		 System.out.println(lastocc(arr,7,0,2));
	}
   static int firstocc(int arr[] , int n, int i, int key){
	   if(i==n) {
		   return -1;
	   }
	   
	   if(arr[i]==key) {
		   return i;
	   }
	   return firstocc (arr,n,i+1,key);
  }
   static int lastocc(int arr[] , int n, int i, int key){
	   if(i==n) {
		   return -1;
	   }
	   int restArray=lastocc(arr,n,i+1,key);
	  if(restArray!=-1) {
		 return restArray; 
	  }
	  if(arr[i]==key) {
		  return i;
	  }
	  return -1;
  }
}
