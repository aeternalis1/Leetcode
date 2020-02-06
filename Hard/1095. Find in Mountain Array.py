# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray(object):
#    def get(self, index):
#        """
#        :type index: int
#        :rtype int
#        """
#
#    def length(self):
#        """
#        :rtype int
#        """

class Solution(object):
    def findInMountainArray(self, target, mountain_arr):
        """
        :type target: integer
        :type mountain_arr: MountainArray
        :rtype: integer
        """
        N = mountain_arr.length()
        lo = 0
        hi = mountain_arr.length()-1
        while lo < hi:
            mid = (lo+hi)/2
            cur = mountain_arr.get(mid)
            cur2 = -1
            cur3 = 1000000000000
            if mid > 0:
                cur2 = mountain_arr.get(mid-1)
            if mid < N:
                cur3 = mountain_arr.get(mid+1)
            if cur2 < cur > cur3:
                lo = mid
                break
            if cur2 < cur:
                lo = mid + 1
            else:
                hi = mid - 1
        l = 0
        r = lo
        while l <= r:
            m = (l+r)/2
            cur = mountain_arr.get(m)
            if cur == target:
                return m
            elif cur < target:
                l = m + 1
            else:
                r = m - 1
        
        l = lo
        r = N-1
        while l <= r:
            m = (l+r)/2
            cur = mountain_arr.get(m)
            if cur == target:
                return m
            elif cur < target:
                r = m - 1
            else:
                l = m + 1
        
        return -1
