/*A frog jumps either 1, 2, or 3 steps to go to the top. In how many ways can it reach the top. As the answer will be
 *  large find the answer modulo 1000000007.
 */
//Initial Template for Java

import java.util.*;
import java.io.*;
import java.lang.*;

public class CountNumberOfHops
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        
        while(t-- > 0)
        {
            int n = sc.nextInt();
            System.out.println(new Hops().countWays(n));
            
        }
    }
}
// } Driver Code Ends


//User function Template for Java


class Hops
{
    static long countWays(int n)
    {
        if(n==0||n==1)
        return 1;
        long dp[]=new long[n+1];
        dp[0]=1;
        dp[1]=1;
        dp[2]=2;
        for(int i=3;i<=n;i++)
            dp[i]=(dp[i-1]+dp[i-2]+dp[i-3])%1000000007;
         return dp[n];
    }
    
}

