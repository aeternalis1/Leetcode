class Solution(object):
    def minKBitFlips(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        N = len(A)
        cur = []
        cnt = 0
        ans = 0
        for i in range(N):
            A[i] ^= (cnt%2)
            if N-i >= K and A[i] == 0:
                cur.append(i)
                cnt += 1
                ans += 1
            elif A[i] == 0:
                return -1
            while cur and i-cur[0] >= K-1:
                cur.pop(0)
                cnt -= 1
        return ans
