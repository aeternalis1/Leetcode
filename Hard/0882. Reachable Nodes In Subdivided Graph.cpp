#define f first
#define s second

class Solution {
public:
    int reachableNodes(vector<vector<int>>& edges, int M, int N) {
        vector<pair<int,int>> paths[N];
        for (int i=0;i<edges.size();i++){
            int a = edges[i][0], b = edges[i][1], c = edges[i][2];
            paths[a].push_back({b,c+1});
            paths[b].push_back({a,c+1});
        }
        priority_queue<pair<int,int>, vector<pair<int,int>>, greater<pair<int,int>>> pq;
        pq.push({0,0});
        int dist[N];
        dist[0] = 0;
        for (int i=1;i<N;i++){
            dist[i] = 1e9;
        }
        while (!pq.empty()){
            pair<int,int> cur = pq.top();
            pq.pop();
            for (pair<int,int> i:paths[cur.s]){
                if (cur.f + i.s < dist[i.f]){
                    dist[i.f] = cur.f + i.s;
                    pq.push({dist[i.f], i.f});
                }
            }
        }
        int ans = 0;
        for (int i=0;i<N;i++){
            if (dist[i] <= M) ans++;
        }
        for (int i=0;i<edges.size();i++){
            int a = edges[i][0], b = edges[i][1], c = edges[i][2];
            a = max(M-dist[a],0);
            b = max(M-dist[b],0);
            ans += min(c,a+b);
        }
        return ans;
    }
};
