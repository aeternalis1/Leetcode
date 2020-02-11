class Solution {
public:
    int minJumps(vector<int>& arr) {
        int N = arr.size();
        unordered_map<int,int> seen;
        unordered_map<int,vector<int>> paths;
        for (int i=0;i<N;i++){
            seen[arr[i]] = 0;
            if (paths.find(arr[i]) == paths.end()){
                vector<int> tmp;
                paths[arr[i]] = tmp;
            }
            paths[arr[i]].push_back(i);
        }
        queue<int> q;
        q.push(0);
        int chk[N];
        for (int i=0;i<N;i++){
            chk[i] = 0;
        }
        chk[0] = 1;
        int c;
        while (!q.empty()){
            c = q.front();
            q.pop();
            if (c > 0){
                if (!chk[c-1]){
                    chk[c-1] = chk[c] + 1;
                    q.push(c-1);
                }
            }
            if (c < N-1){
                if (!chk[c+1]){
                    chk[c+1] = chk[c] + 1;
                    q.push(c+1);
                }
            }
            if (seen[arr[c]]) continue;
            seen[arr[c]] = 1;
            for (int i:paths[arr[c]]){
                if (!chk[i]){
                    chk[i] = chk[c]+1;
                    q.push(i);
                }
            }
        }
        return chk[N-1]-1;
    }
};
