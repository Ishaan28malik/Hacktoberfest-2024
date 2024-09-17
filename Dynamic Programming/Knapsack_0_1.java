package dp;

import java.util.Arrays;

public class Knapsack_0_1 {

	static int knapsack(int[] wt, int[] val, int w, int i){
		if(dp[i][w]!=-1)
			return dp[i][w];
		if(i>=wt.length || w==0){
			dp[i][w]=0;
			return 0;
		}
		if(wt[i]<=w)
			return dp[i][w]=Math.max(val[i]+knapsack(wt, val, w-wt[i], i+1), knapsack(wt, val, w, i+1));
		return dp[i][w]=knapsack(wt, val, w, i+1);
	}
	
	static int knapsackTopDown(int[] wt, int[] val, int w){
		for (int i = 0; i < dp.length; i++) {
			for (int j = 0; j < dp[0].length; j++) {
				if(i==0 || j==0)
					dp[i][j]=0;
				else if(wt[i-1]<=j)
					dp[i][j]=Math.max(val[i-1]+dp[i-1][j-wt[i-1]], dp[i-1][j]);
				else
					dp[i][j]=dp[i-1][j];
			}
		}
		return dp[dp.length-1][dp[0].length-1];
	}
	
	static int[][] dp;
	public static void main(String[] args) {
		int[] val={60, 100, 120};
		int[] wt={10, 20, 30};
		int w=50;
		dp=new int[wt.length+1][w+1];
		for (int i = 0; i < wt.length; i++) {
			Arrays.fill(dp[i], -1);
		}
		System.out.println("max profit: "+knapsack(wt, val, w, 0));
		System.out.println("max profit top-down: "+knapsackTopDown(wt, val, w));
	}
}
