class Solution {
    public boolean canPartition(int[] nums) {

        int n = nums.length;

        int sum = 0;

        for(int ele : nums){
            sum += ele;
        }

        if(sum % 2 == 1){
            return false;
        }

      

        int W = sum / 2;


      

        int dp[][] = new int[n+1][W+1];


        for(int i=0; i<n; i++){
            dp[i][0] = 0;
        }

        for(int j=0; j<W; j++){
            dp[0][j] = 0;
        }

        for(int i=1; i<n+1; i++){
            for(int j=1; j<W+1; j++){

                int v = nums[i-1];

                if(v <= j){


                    dp[i][j] = Math.max(v + dp[i-1][j-v], dp[i-1][j]);

                }

                else{
                    dp[i][j] = dp[i-1][j];
                }
            }
        }


        if(dp[n][W] == sum / 2){
            return true;
        }


        return false;
    }
}
