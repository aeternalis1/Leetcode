class Solution(object):
    def largestIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if grid == []:
            return 0
        N = len(grid)
        M = len(grid[0])
        p = [[[i,j] for j in range(M)] for i in range(N)]
        r = [[0 for x in range(M)] for x in range(N)]
        s = [[1 for x in range(M)] for x in range(N)]
        
        def par(i):
            if i == p[i[0]][i[1]]:
                return i
            return par(p[i[0]][i[1]])
        
        def join(a, b):
            if r[a[0]][a[1]] > r[b[0]][b[1]]:
                p[b[0]][b[1]] = a
                s[a[0]][a[1]] += s[b[0]][b[1]]
            elif r[a[0]][a[1]] < r[b[0]][b[1]]:
                p[a[0]][a[1]] = b
                s[b[0]][b[1]] += s[a[0]][a[1]]
            else:
                r[a[0]][a[1]] += 1
                p[b[0]][b[1]] = a
                s[a[0]][a[1]] += s[b[0]][b[1]]
        
        ans = 1
        
        for i in range(N):
            for j in range(M):
                if j < M - 1 and grid[i][j] and grid[i][j+1]:
                    a = par([i,j])
                    b = par([i,j+1])
                    if a != b:
                        join(a,b)
                    ans = max(ans,s[a[0]][a[1]],s[b[0]][b[1]])
                if i < N - 1 and grid[i][j] and grid[i+1][j]:
                    a = par([i,j])
                    b = par([i+1,j])
                    if a != b:
                        join(a,b)
                    ans = max(ans,s[a[0]][a[1]],s[b[0]][b[1]])
        
        moves = [[-1,0],[1,0],[0,-1],[0,1]]
        
        for i in range(N):
            for j in range(M):
                if grid[i][j]:
                    continue
                res = []
                for k in moves:
                    y,x = i+k[0],j+k[1]
                    if 0 <= y < N and 0 <= x < M and grid[y][x]:
                        a = par([y,x])
                        res.append(tuple(a))
                res = set(res)
                if not res:
                    continue
                ans = max(ans, 1+sum([s[x[0]][x[1]] for x in res]))
        
        return ans
                
