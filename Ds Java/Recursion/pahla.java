package Ds.Recursion;

import java.util.Scanner;

public class pahla {

	public static void main(String []args) {
		 Scanner sc=new Scanner(System.in);
		 int n=sc.nextInt();
//		 int p=sc.nextInt();
		 System.out.println(factorial(n));
	}
	static int power(int n,int p) {
		if(p==0) {
			return 1;
		}
		
		int prevPower = power(n , p-1);
		return n*prevPower;
	}
	static int factorial(int n) {
		if(n==0) {
			return 1;
		}
		
		int prevFact=factorial(n-1);
		return n*prevFact;
	}
}
