#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    /*
        // Recursive + Memoization Code [Top Down Approach]
        // T.C. -> O(N)
        // S.C. -> O(N) [1D dp vector] + O(N) [Recursion auxillary stack space]
        int f(int ind, vector<int> &nums, vector<int> &dp)
        {

            // Base Case
            if (ind == 0)
                return nums[0];
            if (ind < 0)
                return 0;

            // Step 3 : If overlapping subproblem already solved return its value
            if (dp[ind] != -1)
                return dp[ind];

            int pick = nums[ind] + f(ind - 2, nums, dp);
            int notPick = 0 + f(ind - 1, nums, dp);

            // Step 2 : store output in dp array to avoid overlapping subproblems
            return dp[ind] = max(pick, notPick);
        }

        int house_robber(vector<int> nums)
        {

            int n = nums.size();
            vector<int> dp(n, -1); // Step 1 : Create 1D dp array
            return f(n - 1, nums, dp);
        }
        */

    /*
    // Tabulation Code [Bottom Up Approach]
    // T.C. -> O(N)
    // S.C. -> O(N) [1D dp vector]
    int house_robber(vector<int> nums)
    {
        int n = nums.size();
        vector<int> dp(n, 0);
        // Base Case
        dp[0] = nums[0];

        for (int i = 1; i < n; i++)
        {
            int pick = nums[i];
            if (i > 1)
                pick += dp[i - 2];
            int notpick = 0 + dp[i - 1];

            dp[i] = max(pick, notpick);
        }
        return dp[n - 1];
    }
    */

    // Space Optimized Code
    // T.C. -> O(N)
    // S.C. -> O(1)
    int house_robber(vector<int> nums)
    {
        int n = nums.size();
        int prev1 = nums[0]; //  prev1 signifies (i-1)th index
        int prev2 = 0;       //  prev2 signifies (i-2)th index

        for (int i = 1; i < n; i++)
        {
            int pick = nums[i];
            if (i > 1)
                pick += prev2;
            int notpick = 0 + prev1;

            int curri = max(pick, notpick);
            // Shifting Logic
            prev2 = prev1;
            prev1 = curri;
        }
        return prev1; // because on ending of the above for loop i will point to n, therefore prev1 will be at (n-1) th index
    }
};

int main()
{

    Solution obj;
    vector<int> nums = {2, 7, 9, 3, 1};
    int ans = obj.house_robber(nums);
    cout << "\n Array is: " << endl;
    for (auto it : nums)
        cout << " " << it << " ";
    cout << "\nMaximum Sum of Non Adjacent Elements is: " << ans << endl;

    return 0;
}