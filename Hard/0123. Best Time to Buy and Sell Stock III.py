class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        N = len(prices)
        if N == 0:
            return 0
        pre = [0 for x in range(N+1)]
        m = prices[0]
        for i in range(N):
            m = min(m, prices[i])
            pre[i+1] = max(pre[i], prices[i] - m)
        m = prices[N-1]
        ans = 0
        for i in range(N-2,-1,-1):
            ans = max(ans, (m - prices[i]) + pre[i])
            m = max(m, prices[i])
        return ans
