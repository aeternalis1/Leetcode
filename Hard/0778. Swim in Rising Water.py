class Solution(object):
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        N = len(grid)
        lo = grid[0][0]
        hi = N*N
        moves = [[0,1],[0,-1],[1,0],[-1,0]]
        
        while lo < hi:
            mid = (lo+hi)/2
            chk = [[0 for x in range(N)] for x in range(N)]
            chk[0][0] = 1
            q = [[0,0]]
            while q:
                y,x = q.pop(0)
                for i in moves:
                    ny,nx = y+i[0],x+i[1]
                    if 0 <= ny < N and 0 <= nx < N:
                        if not chk[ny][nx] and grid[ny][nx] <= mid:
                            chk[ny][nx] = 1
                            q.append([ny,nx])
            if chk[N-1][N-1]:
                hi = mid
            else:
                lo = mid+1
                
        return lo
