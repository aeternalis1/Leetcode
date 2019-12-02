class Solution(object):
    def longestDecomposition(self, text):
        """
        :type text: str
        :rtype: int
        """
        N = len(text)
        dp = [0 for x in xrange(N/2)] # only really use the first half
        ind = 0
        
        def solve(ind):
            if ind == N/2:
                if N%2:
                    return 1
                return 0
            if dp[ind]:
                return dp[ind]
            
            res = 1
            for j in xrange(ind,N/2):
                if text[ind:j+1] == text[N-j-1:N-ind]:
                    res = max(res,solve(j+1)+2)
            dp[ind] = res
            return res
        
        return solve(0)
