class Solution {
    public int solution(int n, int[] tops) {
        
        int[][] dp = new int[n][2];
        int MOD = 10007;
            
        for (int i=0; i<n; i++) {
            if (tops[i] == 1) { // 위에 세모가 있을 때
                if (i == 0) {   // 첫번째 세모
                    dp[i][0] = 3;
                    dp[i][1] = 1;
                } else {
                    dp[i][0] = (dp[i-1][0]*3 + dp[i-1][1]*2) % MOD; 
                    dp[i][1] = (dp[i-1][0] + dp[i-1][1]) % MOD;
                }
            } else {            // 위에 세모가 없을 때
                if (i == 0) {   // 첫번째 마름모
                    dp[i][0] = 2;
                    dp[i][1] = 1;
                } else {
                    dp[i][0] = (dp[i-1][0]*2 + dp[i-1][1]) % MOD;
                    dp[i][1] = (dp[i-1][0] + dp[i-1][1]) % MOD;
                }
            }
        }
        return (dp[n-1][0] + dp[n-1][1]) % MOD;
    }   
}