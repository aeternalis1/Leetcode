typedef long long ll;
#define f first
#define s second

int gen_base(const int before, const int after) {
    auto seed = std::chrono::high_resolution_clock::now().time_since_epoch().count();
    std::mt19937 mt_rand(seed);
    int base = std::uniform_int_distribution<int>(before+1, after)(mt_rand);
    return base % 2 == 0 ? base-1 : base;
}

class Solution {
public:
    string longestDupSubstring(string S) {
        int N = S.length();
        string s = S;
        ll base = gen_base(256,805306453);
        ll mod[2] = {805306457,1610612741};
        ll pows[2][N+1], arr[2][N+1];
        pows[0][0] = pows[1][0] = 1;
        arr[0][0] = arr[1][0] = 0;
        for (int i=0;i<N;i++){
            for (int j=0;j<2;j++){
                pows[j][i+1] = pows[j][i]*base%mod[j];
                arr[j][i+1] = (arr[j][i]+s[i]*pows[j][i])%mod[j];
            }
        }
        int lo=0,hi=N+1,mid,f;
        string res[N];
        while (lo<hi){
            mid = (lo+hi)/2;
            f = 0;
            vector<pair<ll,pair<ll, ll>>> temp;
            pair<ll,ll> cur;
            for (int i=0;i<N-mid+1;i++){
                temp.push_back({((arr[0][i+mid]-arr[0][i]+mod[0])*pows[0][N-i])%mod[0],{((arr[1][i+mid]-arr[1][i]+mod[1])*pows[1][N-i])%mod[1], i}});
            }
            sort(temp.begin(),temp.end());
            ll cnt = 1, ans = 1;
            cur = {temp[0].f, temp[0].s.f};
            for (int i=1;i<temp.size();i++){
                if (temp[i].f == cur.f && temp[i].s.f == cur.s){
                    cnt++;
                    if (cnt >= 2){
                        res[mid] = s.substr(temp[i].s.s,mid);
                        break;
                    }
                }else{
                    cur = {temp[i].f,temp[i].s.f};
                    cnt = 1;
                }
            }
            if (cnt<2) hi = mid;
            else lo = mid+1;
        }
        return res[lo-1];
    }
};
