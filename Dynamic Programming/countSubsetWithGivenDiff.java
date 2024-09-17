package dp;
public class countSubsetWithGivenDiff {

	static int countSubsetWithGivenSum(int[] a, int sum){
		for (int i = 0; i < dp.length; i++) {
			for (int j = 0; j < dp[i].length; j++) {
				if(j==0)
					dp[i][j]=1;
				else if(i==0)
					dp[i][j]=0;
				else if (a[i-1]<=j)
					dp[i][j]=dp[i-1][j-a[i-1]]+dp[i-1][j];
				else
					dp[i][j]=dp[i-1][j];
			}
		}
		return dp[dp.length-1][dp[0].length-1];
	}
	
	static int dp[][];
	static int countSubsetWithGivenDiff(int[] a, int diff){
		int sum=0;
		for (int i = 0; i < a.length; i++) {
			sum+=a[i];
		}
		int s=(sum+diff)/2;
		dp=new int[a.length+1][s+1];
		return countSubsetWithGivenSum(a, s);
	}
	
	public static void main(String[] args) {
		int[] a={1,2,1,3};
		int diff=1;
		System.out.println(countSubsetWithGivenDiff(a, diff));
	}
}
