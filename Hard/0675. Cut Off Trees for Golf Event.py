class Solution(object):
    def cutOffTree(self, forest):
        """
        :type forest: List[List[int]]
        :rtype: int
        """
        N = len(forest)
        M = len(forest[0])
        moves = [[-1,0],[1,0],[0,-1],[0,1]]
        arr = []
        for i in range(N):
            for j in range(M):
                if forest[i][j] > 1:
                    arr.append([forest[i][j],i,j])
        arr = sorted(arr)
        y,x = 0,0
        ans = 0
        for tar in arr:
            queue = [[y,x]]
            dp = [[1000000 for i in range(M)] for i in range(N)]
            dp[y][x] = 0
            while queue:
                y,x = queue.pop(0)
                if y == tar[1] and x == tar[2]:
                    break
                for k in moves:
                    ny,nx = y+k[0],x+k[1]
                    if 0 <= ny < N and 0 <= nx < M:
                        if forest[ny][nx] and dp[ny][nx] == 1000000:
                            queue.append([ny,nx])
                            dp[ny][nx] = dp[y][x]+1
            if dp[tar[1]][tar[2]] == 1000000:
                return -1
            ans += dp[tar[1]][tar[2]]
            y,x = tar[1],tar[2]
        return ans
