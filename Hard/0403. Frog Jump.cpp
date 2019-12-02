class Solution {
public:
    bool canCross(vector<int>& stones) {
        int N = stones.size();
        sort(stones.begin(),stones.end());
        if (stones[1] != 1) return false;
        unordered_map<int,int> exist;
        int dp[N+1][N+5];
        memset(dp,0,sizeof dp);
        dp[1][1] = 1;
        for (int i=0;i<N;i++){
            exist[stones[i]] = i+1;
        }
        for (int i=1;i<N-1;i++){
            for (int j=1;j<N+1;j++){
                if (dp[i][j]){
                    if (j > 1){
                        if (exist[stones[i]+j-1]){
                            dp[exist[stones[i]+j-1]-1][j-1] = 1;
                        }
                    }
                    if (exist[stones[i]+j]){
                        dp[exist[stones[i]+j]-1][j] = 1;
                    }
                    if (exist[stones[i]+j+1]){
                        dp[exist[stones[i]+j+1]-1][j+1] = 1;
                    }
                }
            }
        }
        for (int i=0;i<N+5;i++){
            if (dp[N-1][i]) return true;
        }
        return false;
    }
};
