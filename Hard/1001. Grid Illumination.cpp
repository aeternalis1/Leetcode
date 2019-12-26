class Solution {
public:
    vector<int> gridIllumination(int N, vector<vector<int>>& lamps, vector<vector<int>>& queries) {
        unordered_map<int,int> a,b,c,d;
        unordered_map<int,unordered_map<int,int>> mp;
        for (vector<int> i: lamps){
            a[i[0]]++;
            b[i[1]]++;
            c[i[0]-i[1]]++;
            d[N-i[1]-i[0]]++;
            mp[i[0]][i[1]] = 1;
        }
        vector<int> answer;
        for (vector<int> i: queries){
            if (a[i[0]] || b[i[1]] || c[i[0]-i[1]] || d[N-i[1]-i[0]]){
                answer.push_back(1);
            }else{
                answer.push_back(0);
            }
            for (int j=-1;j<=1;j++){
                for (int k=-1;k<=1;k++){
                    int y = i[0]+j;
                    int x = i[1]+k;
                    if (mp[y][x]){
                        a[y]--;
                        b[x]--;
                        c[y-x]--;
                        d[N-y-x]--;
                        mp[y][x] = 0;
                    }
                }
            }
        }
        return answer;
    }
};
