class Solution(object):
    def numWays(self, steps, arrLen):
        """
        :type steps: int
        :type arrLen: int
        :rtype: int
        """
        N = min(steps,arrLen)
        dp = [0 for x in range(N)]
        dp[0] = 1
        mod = pow(10,9)+7
        for i in range(steps):
            nxt = [0 for x in range(N)]
            for j in range(N):
                nxt[j] = dp[j]
                if j > 0:
                    nxt[j] += dp[j-1]
                if j < N-1:
                    nxt[j] += dp[j+1]
                nxt[j] %= mod
            dp = nxt
        return dp[0]%mod
