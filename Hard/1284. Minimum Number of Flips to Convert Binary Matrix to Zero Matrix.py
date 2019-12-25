class Solution(object):
    def minFlips(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        N = len(mat)
        M = len(mat[0])
        chk = [0 for x in range(1<<(N*M))]
        cur = 0
        for i in range(N):
            for j in range(M):
                if mat[i][j]:
                    cur ^= 1<<(i*M+j)
        chk[cur] = 1
        q = [cur]
        arr = [[0,0],[0,1],[0,-1],[1,0],[-1,0]]
        
        while q:
            cur = q.pop(0)
            for i in range(N):
                for j in range(M):
                    temp = cur
                    for k in arr:
                        y,x = i+k[0],j+k[1]
                        if 0 <= y < N and 0 <= x < M:
                            temp ^= 1<<(y*M+x)
                    if not chk[temp]:
                        chk[temp] = chk[cur]+1
                        q.append(temp)
                        
        return chk[0]-1
