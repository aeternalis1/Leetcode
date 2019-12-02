class Solution(object):
    def shortestPathAllKeys(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """
        keys = 'abcdef'
        locks = 'ABCDEF'
        N = len(grid)
        M = len(grid[0])
        
        # [i][j][k] = [row][column][bitmask of keys found]
        chk = [[[0 for x in range(1<<6)] for x in range(M)] for x in range(N)]
        
        q = []
        K = 0
        
        for i in range(N):
            for j in range(M):
                if grid[i][j] == '@':
                    q.append([i,j,0])
                    chk[i][j][0] = 1
                elif grid[i][j] in keys:
                    K += 1
        
        moves = [[0,1],[1,0],[-1,0],[0,-1]]
        
        while q:
            y,x,bit = q.pop(0)
            if bit == (1<<K)-1:
                return chk[y][x][bit]-1
            for move in moves:
                ny,nx = y+move[0],x+move[1]
                if ny < 0 or ny >= N or nx < 0 or nx >= M or grid[ny][nx] == '#':
                    continue
                if grid[ny][nx] in locks:
                    if not bit&(1<<(locks.index(grid[ny][nx]))):
                        continue
                nbit = bit
                if grid[ny][nx] in keys:
                    nbit |= (1<<(keys.index(grid[ny][nx])))
                if not chk[ny][nx][nbit]:
                    chk[ny][nx][nbit] = chk[y][x][bit]+1
                    q.append([ny,nx,nbit])
        
        return -1
