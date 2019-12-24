class Solution {
public:
    int numSubmatrixSumTarget(vector<vector<int>>& matrix, int target) {
        int N = matrix.size();
        int M = matrix[0].size();
        int arr[N+1][M+1];
        memset(arr,0,sizeof arr);
        for (int i=0;i<N;i++){
            for (int j=0;j<M;j++){
                arr[i+1][j+1] = arr[i+1][j] + matrix[i][j];
            }
        }
        for (int i=0;i<N;i++){
            for (int j=1;j<=M;j++){
                arr[i+1][j] = arr[i][j] + arr[i+1][j];
            }
        }
        unordered_map<int,int> occ[M+1];
        for (int i=0;i<M;i++){
            occ[i][0] = 1;
        }
        long long ans = 0;
        int cur = 0;
        for (int i=1;i<=N;i++){
            for (int j=i;j<=N;j++){
                unordered_map<int,int> occ;
                occ[target] = 1;
                for (int k=1;k<=M;k++){
                    cur = arr[j][k]-arr[i-1][k];
                    ans += occ[cur];
                    occ[target-arr[i-1][k]+arr[j][k]]++;
                }
            }
        }
        return ans;
    }
};

// arr[c][d] - arr[a][d] - arr[c][b] + arr[a][b] = tar
