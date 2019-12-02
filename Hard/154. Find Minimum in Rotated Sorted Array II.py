class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return min(nums)
        N = len(nums)
        if N <= 2:
            return min(nums)
        l = 0
        r = N
        ans = pow(10,19)
        while l < r:
            mid = (l+r)/2
            if nums[mid] >= nums[N-1] and mid != N-1:
                l = mid+1
            elif nums[mid] >= nums[N-1]:
                ans = min(ans,nums[N-1])
                r = mid
            else:
                r = mid
        return nums[l]
