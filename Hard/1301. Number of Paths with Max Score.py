class Solution(object):
    def pathsWithMaxScore(self, board):
        """
        :type board: List[str]
        :rtype: List[int]
        """
        N = len(board)
        M = len(board[0])
        moves = [[-1,0],[-1,-1],[0,-1]]
        dp = [[[0,0] for x in range(M)] for x in range(N)]
        dp[N-1][M-1] = [0,1]
        MOD = pow(10,9)+7
        board[0] = [0] + list(board[0])[1:]
        for i in range(N-1,-1,-1):
            for j in range(M-1,-1,-1):
                for k in moves:
                    y, x = i + k[0], j + k[1]
                    if x < 0 or y < 0 or board[y][x] == 'X' or dp[i][j][1] == 0:
                        continue
                    if dp[i][j][0] + int(board[y][x]) > dp[y][x][0]:
                        dp[y][x] = [dp[i][j][0] + int(board[y][x]), dp[i][j][1]]
                    elif dp[i][j][0] + int(board[y][x]) == dp[y][x][0]:
                        dp[y][x][1] = dp[y][x][1] + dp[i][j][1]
                        dp[y][x][1] %= MOD
        return dp[0][0]
