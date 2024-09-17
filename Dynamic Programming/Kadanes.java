package dp;

import java.util.Scanner;

public class Kadanes {

	
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		int n=sc.nextInt();
		int[] a=new int[n];
		for (int i = 0; i < a.length; i++) {
			a[i]=sc.nextInt();
		}
		
		
		int max=a[0];
		int curr_max=max;
		for (int i = 1; i < a.length; i++) {
			curr_max=Math.max(curr_max+a[i], a[i]);
			max=Math.max(max, curr_max);
		}
		
		System.out.println(max);
	}
}
