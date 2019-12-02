class Solution(object):
    def shortestSuperstring(self, A):
        """
        :type A: List[str]
        :rtype: str
        """
        
        N = len(A)
        dp = [[1000 for x in range(N)] for x in range(1<<N)] # bit, last string
        back = [[0 for x in range(N)] for x in range(1<<N)]
        arr = [[0 for x in range(N)] for x in range(N)] # length of common suffix/prefix of [i][j]
        
        for i in range(N):
            for j in range(N):
                if i == j:
                    continue
                for k in range(min(len(A[i]),len(A[j]))):
                    if A[i][-k-1:] == A[j][:k+1]:
                        arr[i][j] = k+1
        
        for i in range(N):
            dp[1<<i][i] = len(A[i])
        
        for i in range(1<<N):
            for j in range(N):
                if dp[i][j] != 1000:
                    for k in range(N):
                        if i&(1<<k):
                            continue
                        if dp[i][j]+len(A[k])-arr[j][k] < dp[i^(1<<k)][k]:
                            back[i^(1<<k)][k] = j
                            dp[i^(1<<k)][k] = dp[i][j]+len(A[k])-arr[j][k]
        ind = dp[(1<<N)-1].index(min(dp[(1<<N)-1]))
        cur = (1<<N)-1
        ans = A[ind]
        for i in range(N-1):
            newind = back[cur][ind]
            ans = A[newind][:len(A[newind])-arr[newind][ind]]+ans
            cur, ind = cur ^ (1<<ind), back[cur][ind]
        return ans
