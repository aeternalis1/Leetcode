const int MAXN = 2001;
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
    int distinctEchoSubstrings(string text) {
        string s = text;
        int N = s.length();
        ll base = gen_base(256,1000000007);
        ll mod = 982451653;
        ll pows[N+1], arr[N+1];
        unordered_map<ll,int> seen;
        pows[0] = 1;
        arr[0] = 0;
        for (int i=0;i<N;i++){
            pows[i+1] = pows[i]*base%mod;
            arr[i+1] = (arr[i]+s[i]*pows[i])%mod;
        }
        int ans = 0;
        ll cur,cur2;
        for (int i=0;i<N;i++){
            for (int j=2;j<=N-i;j+=2){
                cur = ((arr[i+j/2]-arr[i]+mod)*pows[N-i])%mod;
                cur2 = ((arr[i+j]-arr[i+j/2]+mod)*pows[N-(i+j/2)])%mod;
                if (cur==cur2){
                    if (!seen[cur]){
                        ans++;
                        seen[cur] = 1;
                    }
                }
            }
        }
        return ans;
    }
};
