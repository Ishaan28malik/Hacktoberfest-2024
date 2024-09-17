package dp;

import java.util.Scanner;

public class Fibonacci {

	static int fib(int n){
		if(n<=1)
			return n;
		else
			return fib(n-1) + fib(n-2);
	}
	
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		int n=sc.nextInt(); 
		int[] f=new int[n];
		
		f[0]=1;
		f[1]=1;
		for (int i = 2; i < f.length; i++) {
			f[i]=f[i-1]+f[i-2];
		}
		for (int i = 0; i < f.length; i++) {
			System.out.print(f[i]+" ");
		}
		System.out.println();
		
		
	}
}
