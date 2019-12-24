class Solution(object):
    def minFallingPathSum(self, arr):
        """
        :type arr: List[List[int]]
        :rtype: int
        """
        N = len(arr)
        M = len(arr[0])
        dp = [0 for x in range(M)]
        for i in range(N):
            mins = [1000000,1000000]
            inds = [0,0]
            for j in range(M):
                if dp[j] <= mins[0]:
                    mins[1],inds[1] = mins[0],inds[0]
                    mins[0],inds[0] = dp[j],j
                elif dp[j] <= mins[1]:
                    mins[1],inds[1] = dp[j],j
            for j in range(M):
                if j != inds[0]:
                    dp[j] = mins[0]+arr[i][j]
                else:
                    dp[j] = mins[1]+arr[i][j]
            print mins,dp
        return min(dp)
