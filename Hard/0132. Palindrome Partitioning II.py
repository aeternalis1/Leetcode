class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        N = len(s)
        if N == 0:
            return 0
        base = 101
        mod = pow(10,9)+7
        pows = [1 for x in range(N+1)]
        for i in range(N):
            pows[i+1] = pows[i] * base % mod
        pre = [0 for x in range(N+1)]
        suf = [0 for x in range(N+1)]
        for i in range(N):
            pre[i+1] = (pre[i] + ord(s[i]) * pows[i]) % mod
        for i in range(N-1,-1,-1):
            suf[i] = (suf[i+1] + ord(s[i]) * pows[N-i-1]) % mod
        dp = [N for x in range(N+1)]
        dp[0] = 0
        for i in range(N):
            for j in range(1,N-i+1):
                if (pre[i+j]-pre[i]) * pows[N-i-j] % mod == (suf[i]-suf[i+j]) * pows[i] % mod:
                    dp[i+j] = min(dp[i+j], dp[i]+1)
        return dp[N]-1
