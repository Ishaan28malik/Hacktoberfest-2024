package dp;

public class CountSubsetSum {

	static int countSubsetSum(int[] a, int sum, int i){
		if(sum==0)
			return 1;
		if(i>=a.length)
			return 0;
		if(a[i]<=sum)
			return countSubsetSum(a, sum-a[i], i+1)+countSubsetSum(a, sum, i+1);
		return countSubsetSum(a, sum, i+1);
	}
	
	static int countSubsetSumTopDown(int[] a, int sum){
		for (int i = 0; i < dp.length; i++) {
			for (int j = 0; j < dp[i].length; j++) {
				if(j==0) 
					dp[i][j]=1;
				else if(i==0)
					dp[i][j]=0;
				else if(a[i-1]<=j)
					dp[i][j]=dp[i-1][j-a[i-1]]+dp[i-1][j];
				else
					dp[i][j]=dp[i-1][j];
			}
		}
		return dp[dp.length-1][dp[0].length-1];
	}
	
	static int dp[][];
	public static void main(String[] args) {
		int[] a={1,2,3,3};
		int sum=6;
		System.out.println(countSubsetSum(a, sum, 0));
		dp=new int[a.length+1][sum+1];
		System.out.println(countSubsetSumTopDown(a, sum));
	}
}
