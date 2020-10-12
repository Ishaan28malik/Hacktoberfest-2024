/*You are given an amount denoted by value. You are also given an array of coins. The array contains the denominations 
 * of the give coins. You need to find the minimum number of coins to make the change for value using the coins of given 
 * denominations. Also, keep in mind that you have infinite supply of the coins.
 * */
//Initial Template for Java

import java.io.*;
import java.util.*;
public class CoinChange {
	public static void main (String[] args) {
		Scanner sc=new Scanner(System.in);
		int testcases=sc.nextInt();
		while(testcases-->0)
		{
		    int value=sc.nextInt();
		    int numberOfCoins=sc.nextInt();
		    int coins[]=new int[numberOfCoins];
		    
		    for(int i=0;i<numberOfCoins;i++)
		    {
		        int x=sc.nextInt();
		        coins[i]=x;
		    }
		   Coin obj=new Coin();
		    long answer=obj.minimumNumberOfCoins(coins,numberOfCoins,value);
		    System.out.println(answer==-1?"Not Possible":answer);
		}
	}
}


 // } Driver Code Ends





class Coin
{
    //Complete this function
    public long minimumNumberOfCoins(int coins[],int numberOfCoins,int amount)
    {
       int dp[]=new int[amount+1];
        Arrays.fill(dp,amount+1);
        dp[0]=0;
        for(int i=1;i<=amount;i++){
            for(int j=0;j<coins.length;j++){
                if(coins[j]<=i)
                    dp[i]=Math.min(dp[i],dp[i-coins[j]]+1);
            }
}
        return dp[amount]>amount?-1:dp[amount];
    }
}


// { Driver Code Starts.

  // } Driver Code Ends