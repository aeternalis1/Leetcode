class Solution(object):
    def containVirus(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        N = len(grid)
        M = len(grid[0])
        moves = [[1,0],[0,1],[-1,0],[0,-1]]
        ans = 0
        for _ in range(N*M):
            chk = [[0 for x in range(M)] for x in range(N)]
            blob = []
            res = 0
            add = 0
            for i in range(N):
                for j in range(M):
                    if grid[i][j] == 1 and not chk[i][j]:
                        q = [[i,j]]
                        chk[i][j] = 1
                        cur = [[i,j]]
                        chk2 = [[0 for x in range(M)] for x in range(N)]
                        cnt = 0
                        tot = 0
                        while q:
                            y,x = q.pop(0)
                            for k in moves:
                                ny,nx = y+k[0],x+k[1]
                                if 0 <= ny < N and 0 <= nx < M:
                                    if grid[ny][nx] == 1 and not chk[ny][nx]:
                                        chk[ny][nx] = 1
                                        q.append([ny,nx])
                                        cur.append([ny,nx])
                                    elif grid[ny][nx] == 0:
                                        if not chk2[ny][nx]:
                                            chk2[ny][nx] = 1
                                            cnt += 1
                                        tot += 1
                        if cnt >= res:
                            res = cnt
                            blob = cur
                            add = tot
            ans += add
            if add == 0:
                break
            for [i,j] in blob:
                grid[i][j] = -1
            chk = [[0 for x in range(M)] for x in range(N)]
            tbd = []
            for i in range(N):
                for j in range(M):
                    if grid[i][j] == 1:
                        for k in moves:
                            ny,nx = i+k[0],j+k[1]
                            if 0 <= ny < N and 0 <= nx < M:
                                if grid[ny][nx] == 0 and not chk[ny][nx]:
                                    tbd.append([ny,nx])
                                    chk[ny][nx] = 1
            for [i,j] in tbd:
                grid[i][j] = 1
        
        return ans
