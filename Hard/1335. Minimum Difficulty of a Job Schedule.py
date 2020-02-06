class Solution(object):
    def minDifficulty(self, jobDifficulty, d):
        """
        :type jobDifficulty: List[int]
        :type d: int
        :rtype: int
        """
        N = len(jobDifficulty)
        jobDifficulty = [0] + jobDifficulty
        dp = [[10000000 for x in range(N+1)] for x in range(d+1)]
        dp[0][0] = 0
        for i in range(d):
            for j in range(N):
                cur = 0
                for k in range(j+1,N-d+i+2):
                    cur = max(cur, jobDifficulty[k])
                    dp[i+1][k] = min(dp[i+1][k], dp[i][j]+cur)
        if dp[d][N] == 10000000:
            return -1
        return dp[d][N]
