package Ds.Recursion;

import java.util.Scanner;

public class main {
    
	public static void main(String []args) {
 
    Scanner sc=new Scanner(System.in);
    int n=sc.nextInt();
    System.out.println(fib(n));
	} 
	static int sum (int n) {
		
		if(n==0) {
			return 0;
		}
		
		int prevSum = sum(n-1);
		return n+prevSum;
	}
	static int fib(int n) {
		if(n==0 || n==1) {
			return n;
		}
		
		
		return fib(n-1)+fib(n-2);
	}
}
