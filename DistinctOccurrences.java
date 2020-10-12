/*Given two strings S and T of length n and m respectively. find count of distinct occurrences of T in S as a sub-sequence. 
 */
import java.util.*;

public class DistinctOccurrences
{
	public static void main(String args[])
	{
		Scanner sc = new Scanner(System.in);
		int t = sc.nextInt();
		sc.nextLine();
		while(t>0)
		{
			String line = sc.nextLine();
			String S = line.split(" ")[0];
			String T = line.split(" ")[1];
			
			Solution sol=new Solution();
			System.out.println(sol.subsequenceCount(S,T));
			t--;
		}
	}
}// } Driver Code Ends


/*You are required to complete this method*/
class Solution
{
    int  subsequenceCount(String s, String t)
    {
	int dp[][]=new int[t.length()+1][s.length()+1];
	for(int j=0;j<=s.length();j++)
	dp[0][j]=1;
	for(int i=0;i<t.length();i++){
	    for(int j=0;j<s.length();j++){
	        if(t.charAt(i)==s.charAt(j))
	        dp[i+1][j+1]=(dp[i][j]+dp[i+1][j])%1000000007;
	        else
	        dp[i+1][j+1]=(dp[i+1][j])%1000000007;
	    }
	}
	return dp[t.length()][s.length()];
    }
}