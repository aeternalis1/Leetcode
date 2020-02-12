class Solution(object):
    def minimumDistance(self, word):
        """
        :type word: str
        :rtype: int
        """
        lets = [[-1 for x in range(6)] for x in range(5)]
        for i in range(26):
            lets[i/6][i%6] = i
        dist = [[0 for x in range(26)] for x in range(26)]
        for i in range(5):
            for j in range(6):
                for k in range(5):
                    for l in range(6):
                        if lets[i][j] == -1 or lets[k][l] == -1:
                            continue
                        dist[lets[i][j]][lets[k][l]] = abs(i-k)+abs(j-l)
                        dist[lets[k][l]][lets[i][j]] = abs(i-k)+abs(j-l)
        N = len(word)
        ans = [[0 for x in range(26)] for x in range(26)]
        for i in range(N):
            nxt = [[1000000 for x in range(26)] for x in range(26)]
            cur = ord(word[i])-ord('A')
            for j in range(26):
                for k in range(26):
                    nxt[j][cur] = min(nxt[j][cur], ans[j][k]+dist[k][cur])
                    nxt[cur][k] = min(nxt[cur][k], ans[j][k]+dist[j][cur])
            ans = nxt
        res = 1000000
        for i in ans:
            res = min(res,min(i))
        return res
