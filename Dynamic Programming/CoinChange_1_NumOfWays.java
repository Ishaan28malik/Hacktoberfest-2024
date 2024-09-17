package dp;
public class CoinChange_1_NumOfWays {

	static int numberOfWays(int[] coins, int sum, int i){
		if(sum==0)
			return 1;
		if(i>=coins.length)
			return 0;
		if(coins[i]<=sum)
			return numberOfWays(coins, sum-coins[i], i)+numberOfWays(coins, sum, i+1);
		return numberOfWays(coins, sum, i+1);
	}
	
	static int numberOfWaysTopDown(int[] coins, int sum){
		for (int i = 0; i < dp.length; i++) {
			for (int j = 0; j < dp[i].length; j++) {
				if(j==0)
					dp[i][j]=1;
				else if(i==0)
					dp[i][j]=0;
				else if(coins[i-1]<=j)
					dp[i][j]=dp[i][j-coins[i-1]]+dp[i-1][j];
				else
					dp[i][j]=dp[i-1][j];
			}
		}
		return dp[dp.length-1][dp[0].length-1];
	}
	
	static int[][] dp;
	
	public static void main(String[] args) {
		int[] coins={1,2,3};
		int sum=4;
		dp=new int[coins.length][sum+1];
		System.out.println(numberOfWays(coins, sum, 0));
		System.out.println(numberOfWaysTopDown(coins, sum));
	}
}
