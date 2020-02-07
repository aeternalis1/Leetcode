class Solution(object):
    def countVowelPermutation(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [[0 for x in range(5)] for x in range(n)]
        # a e i o u respectively
        dp[0] = [1 for x in range(5)]
        mod = 1000000007
        for i in range(1,n):
            dp[i][0] = dp[i-1][1] + dp[i-1][2] + dp[i-1][4]
            dp[i][1] = dp[i-1][0] + dp[i-1][2]
            dp[i][2] = dp[i-1][1] + dp[i-1][3]
            dp[i][3] = dp[i-1][2]
            dp[i][4] = dp[i-1][2] + dp[i-1][3]
            for j in range(5):
                dp[i][j] %= mod
        return sum(dp[n-1])%mod
