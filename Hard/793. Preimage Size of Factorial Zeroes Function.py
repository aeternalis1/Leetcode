def solve(K):
    if K < 0:
        return 0
    lo = 0
    hi = pow(10,15)
    while lo < hi:
        mid = (lo+hi)/2
        cur = 5
        res = 0
        while cur <= mid:
            res += mid/cur
            cur *= 5
        if res > K:
            hi = mid
        else:
            lo = mid+1
    return lo


class Solution(object):
    def preimageSizeFZF(self, K):
        """
        :type K: int
        :rtype: int
        """
        return solve(K)-solve(K-1)
