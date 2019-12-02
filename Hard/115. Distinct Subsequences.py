class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        N = len(s)
        M = len(t)
        lets = {}
        for i in range(M-1,-1,-1):
            try:
                lets[t[i]].append(i)
            except:
                lets[t[i]] = [i]
        dp = [0 for x in range(M+1)]
        dp[0] = 1
        for i in range(N):
            if s[i] in lets:
                for j in lets[s[i]]:
                    dp[j+1] += dp[j]
        return dp[M]
