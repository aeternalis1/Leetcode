#define f first
#define s second

class Solution {
public:
    int racecar(int target) {
        int N = 100000;
        unordered_map<int, int> chk[N*2+5];
        int t = N+target;
        chk[N][1] = 1;
        queue<pair<int,int>> q;
        q.push({N,1});
        while (!q.empty()){
            pair<int,int> cur = q.front();
            q.pop();
            if (cur.f==t){
                return chk[cur.f][cur.s]-1;
                return 0;
            }
            if (cur.s>0&&!chk[cur.f][-1]){
                chk[cur.f][-1] = chk[cur.f][cur.s] + 1;
                q.push({cur.f,-1});
            }else if (cur.s<0&&!chk[cur.f][1]){
                chk[cur.f][1] = chk[cur.f][cur.s] + 1;
                q.push({cur.f,1});
            }
            int newpos = cur.f + cur.s;
            int newspd = cur.s * 2;
            if (newpos >= 0 && newpos <= 2*N && !chk[newpos][newspd]){
                chk[newpos][newspd] = chk[cur.f][cur.s] + 1;
                q.push({newpos, newspd});
            }
        }
        return 0;
    }
};
