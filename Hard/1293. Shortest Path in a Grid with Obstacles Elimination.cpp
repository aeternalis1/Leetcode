#define f first
#define s second

class Solution {
public:
    int shortestPath(vector<vector<int>>& grid, int k) {
        int N = grid.size();
        int M = grid[0].size();
        int chk[N][M][k+1];
        memset(chk,0,sizeof chk);
        queue<pair<int,pair<int,int>>> q;
        if (!grid[0][0]){
            q.push({0,{0,0}});
            chk[0][0][0] = 1;
        }else{
            q.push({0,{0,1}});
            chk[0][0][1] = 1;
        }
        pair<int,pair<int,int>> cur;
        int y,x,num,ny,nx;
        vector<pair<int,int>> moves = {{0,1},{1,0},{-1,0},{0,-1}};
        int ans = N*M+1;
        while (!q.empty()){
            cur = q.front();
            q.pop();
            y = cur.f;
            x = cur.s.f;
            num = cur.s.s;
            if (y == N-1 && x == M-1) return chk[y][x][num]-1;
            for (pair<int,int> i: moves){
                ny = y+i.f;
                nx = x+i.s;
                if (ny < 0 || ny >= N || nx < 0 || nx >= M){
                    continue;
                }
                if (grid[ny][nx] && num < k && !chk[ny][nx][num+1]){
                    chk[ny][nx][num+1] = chk[y][x][num]+1;
                    q.push({ny,{nx,num+1}});
                }else if (!grid[ny][nx] && !chk[ny][nx][num]){
                    chk[ny][nx][num] = chk[y][x][num]+1;
                    q.push({ny,{nx,num}});
                }
            }
        }
        return -1;
    }
};
