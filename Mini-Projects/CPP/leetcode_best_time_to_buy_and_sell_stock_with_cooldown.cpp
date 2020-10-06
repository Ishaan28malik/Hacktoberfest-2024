class Solution {
public:
    int maxProfit(vector<int>& p) {
        if(p.size()<=1)return 0;
        int n=p.size();
        int dp[n][2];
        if(n==2 && p[0]<p[1])return p[1]-p[0];
        if(n==2 && p[0]>p[1])return 0;
        dp[0][0]=0;
        dp[0][1]=-p[0];
        dp[1][0]=max(dp[0][0], dp[0][1]+p[1]);
        dp[1][1]=max(dp[0][1], dp[0][0]-p[1]);
        
        for(int i=2;i<p.size(); i++)
        {
            dp[i][0]= max(dp[i-1][0], dp[i-1][1]+p[i]);
            dp[i][1]= max(dp[i-1][1], dp[i-2][0]-p[i]);
        }
        return dp[n-1][0];
    }
};