long long sum(long long l, long long r){
    return (r*(r-1)/2)-(l*(l-1)/2);
}

class Solution {
public:
    int consecutiveNumbersSum(int N) {
        int hi = N;
        int ans = 1;
        int tot = 1;
        int ind = 2;
        while (tot < N){
            tot += ind;
            ind++;
        }
        for (int i=2;i<ind;i++){
            int lo = 0;
            while (lo <= hi){
                long long mid = (lo+hi)/2;
                long long cur = sum(mid,mid+i);
                if (cur < (long long)N) lo = mid+1;
                else if (cur > (long long)N) hi = mid-1;
                else{
                    ans++;
                    break;
                }
            }
        }
        return ans;
    }
};
