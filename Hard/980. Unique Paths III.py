class Solution(object):
    def uniquePathsIII(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        N = len(grid)
        M = len(grid[0])
        tot = 0
        queue = []
        end = []
        start = 0
        for i in range(N):
            for j in range(M):
                if grid[i][j] == -1:
                    start ^= (1<<(i*M+j))
                elif grid[i][j] == 1:
                    queue = [i,j]
                    tot += 1
                    start ^= (1<<(i*M+j))
                elif grid[i][j] == 2:
                    end = [i,j]
                elif grid[i][j] == 0:
                    tot += 1
        
        moves = [[1,0],[0,1],[-1,0],[0,-1]]
        
        def valid(i,j,bit):
            if i < 0 or i >= N or j < 0 or j >= M:
                return 0
            if bit&(1<<(i*M+j)):
                return 0
            return 1
        
        def dfs(i,j,bit,cnt):
            if [i,j] == end and cnt == tot:
                return 1
            elif [i,j] == end:
                return 0
            res = 0
            for move in moves:
                y,x = i+move[0],j+move[1]
                if not valid(y,x,bit):
                    continue
                res += dfs(y,x,bit^(1<<(y*M+x)),cnt+1)
            return res
        
        return dfs(queue[0],queue[1],start,0)
