
class Solution(object):
    def minPushBox(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        R = len(grid)
        C = len(grid[0])
        xmoves = [-1,1,0,0]
        ymoves = [0,0,-1,1]
        checked = [[[[pow(10,18) for x in range(C)] for x in range(R)] for x in range(C)] for x in range(R)]
        inq = [[[[False for x in range(C)] for x in range(R)] for x in range(C)] for x in range(R)]
        
        def valid(x,y):
            if x >= 0 and x <= C-1 and y >= 0 and y <= R-1 and grid[y][x] != '#':
                return True
            return False
        
        for i in range(R):
            row = grid[i]
            for j in range(C):
                if row[j] == 'B':
                    boxx = j
                    boxy = i
                elif row[j] == 'S':
                    sx = j
                    sy = i
                elif row[j] == 'T':
                    endx = j
                    endy = i
        try:
            queue = [[sx,sy,boxx,boxy]]
            checked[sy][sx][boxy][boxx] = 0
        except:
            return -1
        ans = pow(10,18)
        while queue:
            x,y,x2,y2 = queue.pop(0)
            inq[y][x][y2][x2] = 0
            for i in range(4):
                nx = x+xmoves[i]
                ny = y+ymoves[i]
                if valid(nx,ny):
                    nx2 = x2
                    ny2 = y2
                    if nx == x2 and ny == y2:
                        nx2 = x2+xmoves[i]
                        ny2 = y2+ymoves[i]
                    if valid(nx2,ny2):
                        cur = checked[y][x][y2][x2]
                        if nx2 != x2 or ny2 != y2:
                            cur += 1
                        if cur < checked[ny][nx][ny2][nx2]:
                            checked[ny][nx][ny2][nx2] = cur
                            if not inq[ny][nx][ny2][nx2]:
                                queue.append([nx,ny,nx2,ny2])
                                inq[ny][nx][ny2][nx2] = 1
                            if ny2 == endy and nx2 == endx:
                                ans = min(ans,cur)
        if ans == pow(10,18):
            return -1
        return ans
