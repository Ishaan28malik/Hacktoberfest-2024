package Ds.Recursion;

import java.util.Scanner;

public class practice8 {

	public static void main(String[] args) {
		 Scanner sc=new Scanner(System.in);
			int n = sc.nextInt();	
			int [] arr = new int [n];
			for(int i=0 ; i<arr.length;i++) {
				arr[i]=sc.nextInt();
			}
         int x= sc.nextInt();
         int hi = firstIn(arr , 0 , x);
         System.out.println(hi);
	}
	static int firstIn(int [] arr , int inx , int x) {
		if(arr.length==inx) {
			return -1;
		}
		
		int small = firstIn(arr , inx+1 , x);
		if(arr[inx]==x) {
			return inx;
		}else {
			return small;
		}
	}
	
}	


