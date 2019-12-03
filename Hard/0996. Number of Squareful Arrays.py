class Solution(object):
    def numSquarefulPerms(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        N = len(A)
        dp = [[0 for x in range(N)] for x in range(1<<N)]
        sqr = [[0 for x in range(N)] for x in range(N)]
        for i in range(N):
            for j in range(N):
                if pow(int(pow(A[i]+A[j],0.5)),2) == A[i]+A[j]:
                    sqr[i][j] = 1
        for i in range(N):
            dp[1<<i][i] = 1
        for i in range(1<<N):
            for j in range(N):
                if not dp[i][j]:
                    continue
                for k in range(N):
                    if i&(1<<k) or not sqr[j][k]:
                        continue
                    dp[i|(1<<k)][k] += dp[i][j]
        fact = [1 for x in range(N+1)]
        for i in range(1,N+1):
            fact[i] = fact[i-1]*i
        A = sorted(A)
        cnt = 1
        ans = sum(dp[(1<<N)-1])
        for i in range(1,N):
            if A[i] == A[i-1]:
                cnt += 1
            else:
                ans /= fact[cnt]
                cnt = 1
        ans /= fact[cnt]
        return ans
