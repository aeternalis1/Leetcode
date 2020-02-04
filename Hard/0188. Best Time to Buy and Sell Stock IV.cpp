class Solution {
public:
    int maxProfit(int k, vector<int>& prices) {
        int N = prices.size();
        if (N == 0 || k == 0) return 0;
        k = min(k, N/2+1);
        int dp[N+1];
        memset(dp, 0, sizeof dp);
        for (int i=0;i<k;i++){
            int cur = prices[0];
            for (int j=1;j<=N;j++){
                int temp = min(cur, prices[j-1] - dp[j]);
                dp[j] = max(dp[j], prices[j-1] - cur);
                cur = temp;
                dp[j] = max(dp[j],dp[j-1]);
            }
        }
        return dp[N];
    }
};
