class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)+1
        nums = nums+[0]+[0]
        for i in range(N):
            if nums[i] <= 0 or nums[i] > N:
                nums[i] = 0
        for i in range(N):
            if nums[i] > 0:
                cur = nums[i]
                while cur > 0:
                    lst = cur
                    cur = nums[cur]
                    nums[lst] = -1
        for i in range(1,N+1):
            if nums[i] != -1:
                return i
