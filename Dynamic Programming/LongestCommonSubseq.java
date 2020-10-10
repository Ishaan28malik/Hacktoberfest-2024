package dp;

import java.util.Arrays;
import java.util.Scanner;

public class LongestCommonSubseq {

	static int lcs(String a, String b, int n, int m) {
		if(n==0 || m==0)
			return 0;
		if(a.charAt(n-1)==b.charAt(m-1))
			return 1+lcs(a, b, n-1, m-1);
		return Math.max(lcs(a, b, n-1, m), lcs(a, b, n, m-1));
	}
	
	static int lcsMemo(String a, String b, int n, int m) {
		if(dp[n][m]!=-1)
			return dp[n][m];
		if(n==0 || m==0)
			return dp[n][m]=0;
		if(a.charAt(n-1)==b.charAt(m-1))
			return dp[n][m]=1+lcsMemo(a, b, n-1, m-1);
		return dp[n][m]=Math.max(lcsMemo(a, b, n-1, m), lcsMemo(a, b, n, m-1));
	}
	
	static int lcsTopDwon(String a, String b) {
		int[][] dpp=new int[a.length()+1][b.length()+1];
		int[][] dp=new int[a.length()+1][b.length()+1];
		for (int i = 0; i < dp.length; i++) {
			for (int j = 0; j < dp[i].length; j++) {
				if(i==0 || j==0){
					dp[i][j]=0;
					dpp[i][j]=-1;
				}
				else if(a.charAt(i-1)==b.charAt(j-1)){
					dp[i][j]=dp[i-1][j-1]+1;
					dpp[i][j]=0;
				}
				else{
					dp[i][j]=Math.max(dp[i-1][j], dp[i][j-1]);
					if(dp[i-1][j]>=dp[i][j-1])
						dpp[i][j]=1;
					else
						dpp[i][j]=2;
				}
			}
		}
		StringBuilder ans=new StringBuilder();
		int i=dpp.length-1;
		int j=dpp[0].length-1;
		while(dpp[i][j]!=-1){
			if(dpp[i][j]==0){
				ans.append(a.charAt(i-1));
				i--; j--;
			}
			else if(dpp[i][j]==1){
				i--;
			}
			else{
				j--;
			}
		}
		System.out.println(ans.reverse());
		return dp[dp.length-1][dp[0].length-1];
	}
	
	static int[][] dp;
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		String a=sc.next();
		String b=sc.next();
		System.out.println("1: "+lcs(a, b, a.length(), b.length()));
		dp=new int[a.length()+1][b.length()+1];
		for (int i = 0; i < dp.length; i++) {
			Arrays.fill(dp[i], -1);
		}
		System.out.println("2: "+lcsMemo(a, b, a.length(), b.length()));
		System.out.println("3: "+lcsTopDwon(a, b));
	}
}
