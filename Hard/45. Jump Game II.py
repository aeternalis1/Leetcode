class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        ans = [N+1 for x in range(N)]
        ans[0] = 0
        ind = 1
        q = [0]
        while q:
            c = q.pop(0)
            for i in range(max(ind,c+1),c+nums[c]+1):
                if i >= N:
                    continue
                if ans[i] > ans[c]+1:
                    ans[i] = ans[c]+1
                    q.append(i)
            ind = max(ind,c+nums[c])
        return ans[N-1]
