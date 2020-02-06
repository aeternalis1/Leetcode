class Solution(object):
    def maxJumps(self, arr, d):
        """
        :type arr: List[int]
        :type d: int
        :rtype: int
        """
        N = len(arr)
        temp = [[arr[i],i] for i in range(N)]
        temp = sorted(temp)
        dp = [0 for x in range(N)]
        for i in range(N):
            ind = temp[i][1]
            dp[ind] = 1
            for j in range(ind+1, min(N,ind+d+1)):
                if arr[ind] <= arr[j]:
                    break
                dp[ind] = max(dp[ind], dp[j]+1)
            for j in range(ind-1,max(-1,ind-d-1),-1):
                if arr[ind] <= arr[j]:
                    break
                dp[ind] = max(dp[ind], dp[j]+1)
        return max(dp)
