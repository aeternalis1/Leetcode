const int MAXN = 100001;
int prime[MAXN], cnt[MAXN], p[MAXN], r[MAXN];

int par(int a){
    if (a==p[a]) return a;
    return par(p[a]);
}

void merge(int a, int b){
    if (r[a]>r[b]){
        p[b] = p[a];
        cnt[a] += cnt[b];
    }else if (r[a] < r[b]){
        p[a] = p[b];
        cnt[b] += cnt[a];
    }else{
        r[a]++;
        p[b] = p[a];
        cnt[a] += cnt[b];
    }
}

class Solution {
public:
    int largestComponentSize(vector<int>& A) {
        int N = A.size();
        for (int i=0;i<MAXN;i++){
            cnt[i] = r[i] = prime[i] = 0;
            p[i] = i;
        }
        vector<int> primes;
        for (int i=2;i<MAXN;i++){
            if (!prime[i]){
                primes.push_back(i);
                for (int j=i+i;j<MAXN;j+=i){
                    prime[j] = 1;
                }
            }
        }
        for (int i=0;i<N;i++){
            if (!prime[A[i]]){
                cnt[A[i]]++;
            }
        }
        for (int i=0;i<N;i++){
            if (prime[A[i]]){
                vector<int> fact;
                for (int j:primes){
                    if (A[i]%j==0){
                        fact.push_back(j);
                        while (A[i]%j==0) A[i] /= j;
                        if (A[i] == 1) break;
                    }
                }
                int len = fact.size();
                for (int j=0;j<len-1;j++){
                    int a = par(fact[j]);
                    int b = par(fact[j+1]);
                    if (a!=b) merge(a,b);
                }
                cnt[par(fact[0])]++;
            }
        }
        int ans = 1;
        for (int i=0;i<MAXN;i++){
            ans = max(ans,cnt[i]);
        }
        return ans;
    }
};
