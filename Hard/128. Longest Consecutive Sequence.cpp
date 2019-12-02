class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        int ans = 0;
        int N = nums.size();
        unordered_map<int,int> seen, l, r;
        for (int i:nums){
            if (seen[i]) continue;
            seen[i] = 1;
            if (seen[i-1]&&seen[i+1]){
                ans = max(ans,r[i+1]-l[i-1]+1);
                l[r[i+1]] = l[i-1];
                r[l[i-1]] = r[i+1];
            }else{
                if (seen[i-1]){
                    ans = max(ans,i-l[i-1]+1);
                    l[i] = l[i-1];
                    r[l[i-1]] = i;
                }else if (seen[i+1]){
                    ans = max(ans,r[i+1]-i+1);
                    r[i] = r[i+1];
                    l[r[i+1]] = i;
                }else{
                    l[i] = r[i] = i;
                    ans = max(ans,1);
                }
            }
        }
        return ans;
    }
};
