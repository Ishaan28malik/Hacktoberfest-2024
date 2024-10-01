package Ds.Recursion;

import java.util.Scanner;

public class practice2 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n=sc.nextInt();
		inc(n);

	}
    static void dec(int n) {
    	if (n==0) {
    		return;
    	}
    	System.out.println(n);
    	dec(n-1);
    }
    static void inc(int n) {
    	if (n==0) {
    		return;
    	}
    	
    	inc(n-1);
    	System.out.println(n);
    }
} 
