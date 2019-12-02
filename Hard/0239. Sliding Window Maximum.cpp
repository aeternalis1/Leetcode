class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        priority_queue<pair<int,int>> pq;
        int N = nums.size();
        vector<int> ans;
        pair<int,int> cur;
        for (int i=0;i<N;i++){
            pq.push({nums[i],i});
            if (i < k-1) continue;
            while (!pq.empty()){
                cur = pq.top();
                if (cur.second <= i-k) pq.pop();
                else break;
            }
            ans.push_back(cur.first);
        }
        return ans;
    }
};
