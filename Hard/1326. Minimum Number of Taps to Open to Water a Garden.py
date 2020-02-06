class Solution(object):
    def minTaps(self, n, ranges):
        """
        :type n: int
        :type ranges: List[int]
        :rtype: int
        """
        #dp[i] stores min num of taps to water everything up to (and inc)
        
        dp = [100000 for x in range(n+1)]
        dp[0] = 0
        for i in range(n+1):
            if ranges[i] == 0:
                continue
            cur = dp[max(0,i-ranges[i])]
            for j in range(max(0,i-ranges[i]),min(n+1,i+ranges[i]+1)):
                dp[j] = min(dp[j],cur+1)
        if dp[n] == 100000:
            return -1
        return dp[n]
