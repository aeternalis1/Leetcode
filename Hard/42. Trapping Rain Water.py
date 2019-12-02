class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        nums = height
        N = len(nums)
        stk = []
        ans = 0
        big = 0
        for i in range(N):
            cur = [nums[i],1,big]
            while stk and stk[-1][0] < nums[i]:
                ans += max((min(nums[i],stk[-1][2])-stk[-1][0])*stk[-1][1],0)
                if nums[i] < stk[-1][2]:
                    cur[1] += stk[-1][1]
                stk.pop(-1)
            stk.append(cur)
            big = max(big,nums[i])
        return ans
