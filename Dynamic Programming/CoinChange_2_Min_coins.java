package dp;

import java.util.Arrays;

public class CoinChange_2_Min_coins {

	static int getCount(int[] a, int sum) {
		int[][] dp=new int[a.length+1][sum+1];
		for (int i = 0; i < dp.length; i++) {
			for (int j = 0; j < dp[0].length; j++) {
				if(i==0)
					dp[i][j]=Integer.MAX_VALUE-1;
				else if(j==0)
					dp[i][j]=0;
				else if(a[i-1]<=j)
					dp[i][j]=Math.min(1+dp[i][j-a[i-1]], dp[i-1][j]);
				else
					dp[i][j]=dp[i-1][j];
			}
		}
		return dp[dp.length-1][dp[0].length-1];
	}
	
	static int getCountMemoryEff(int[] a, int sum) {
		int[] dp=new int[sum+1];
		Arrays.fill(dp, Integer.MAX_VALUE-1);
		dp[0]=0;
		for (int i = 0; i < a.length; i++) {
			for (int j = a[i]; j < dp.length; j++) {
				dp[j]=Math.min(1+dp[j-a[i]], dp[j]);
			}
		}
		return dp[sum];
	}
	
	public static void main(String[] args) {
		int[] a={1,4,5};
		int sum=550;
		System.out.println(getCount(a, sum));
		System.out.println(getCountMemoryEff(a, sum));
	}
}
