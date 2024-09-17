package dp;

import java.util.Arrays;
import java.util.Scanner;

public class MatrixChainMultiplication {

	static int solve(int[] a, int i, int j) {
		if(i>=j)
			return 0;
		int min=Integer.MAX_VALUE;
		for (int k = i; k < j; k++) {
			min=Math.min(min,  solve(a, i, k)+solve(a, k+1, j)+a[i-1]*a[k]*a[j]);
		}
		return min;
	}
	
	
	static int solvee(int[] a, int i, int j) {
		if(dp[i][j]!=-1)
			return dp[i][j];
		if(i>=j)
			return dp[i][j]=0;
		int min=Integer.MAX_VALUE;
		for (int k = i; k < j; k++) {
			min=Math.min(min, solvee(a, i, k)+solvee(a, k+1, j)+a[i-1]*a[k]*a[j]);
		}
		return dp[i][j]=min;
	}
	
	static int[][] dp;
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		int n=sc.nextInt();
		int[] a=new int[n];
		for (int i = 0; i < a.length; i++) {
			a[i]=sc.nextInt();
		}
		System.out.println(solve(a, 1, a.length-1));
		dp=new int[a.length+1][a.length+1];
		for (int i = 0; i < a.length; i++) {
			Arrays.fill(dp[i], -1);
		}
		System.out.println(solvee(a, 1, a.length-1));
	}
}
