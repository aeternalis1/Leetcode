class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        N = len(nums)
        def solve(cur):
            cnt = 1
            tmp = 0
            for i in range(N):
                if tmp + nums[i] > cur:
                    cnt += 1
                    tmp = nums[i]
                else:
                    tmp += nums[i]
            return cnt
        
        lo = max(nums)
        hi = pow(10,18)
        
        while lo < hi:
            mid = (lo+hi)/2
            if solve(mid) > m:
                lo = mid+1
            else:
                hi = mid
        return lo
