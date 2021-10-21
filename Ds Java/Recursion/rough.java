package Ds.Recursion;

import java.util.Scanner;

public class rough {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
//		int a = sc.nextInt();
//		int b = sc.nextInt();
//		System.out.println(print(a , b));
		
   for(int x=0;x<6 ; x++) {
//	   for(int j=6; j-x>1 ; j--) {
//		   System.out.print("");
//	   }
	   for(int y=0 ; y<=x ;y++) {
		   System.out.print(print(x,y)+" ");
	   }
	   System.out.println();
   }
	}
//	 static int  GCD(int a , int b) {
//		if(b==0) {
//			return a;
//		}	 
//		int hi= GCD(b , a%b);
//		 return hi;
//	 }
	static int print(int row , int col) {
		if(row==col || col==0) {
			return 1;
		}
		return  print(row-1,col-1)+print(row-1,col) ;
	}
	
}
