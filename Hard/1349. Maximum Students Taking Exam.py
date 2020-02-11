class Solution(object):
    def maxStudents(self, seats):
        """
        :type seats: List[List[str]]
        :rtype: int
        """
        if seats == []:
            return 0
        N = len(seats)
        M = len(seats[0])
        dp = [0 for x in range(1<<M)]
        dp[0] = 1
        for i in range(N):
            nxt = [0 for x in range(1<<M)]
            for j in range(1<<M):
                if not dp[j]:
                    continue
                occ = []
                for k in range(1<<M):
                    f = 0
                    cnt = 0
                    for l in range(M):
                        if k&(1<<l):
                            cnt += 1
                        if l > 0 and k&(1<<l) and j&(1<<(l-1)):
                            f = 1
                        elif l < M-1 and k&(1<<l) and j&(1<<(l+1)):
                            f = 1
                        elif l > 0 and k&(1<<l) and k&(1<<(l-1)):
                            f = 1
                        elif k&(1<<l) and seats[i][l] == '#':
                            f = 1
                        if f:
                            break
                    if not f:
                        nxt[k] = max(nxt[k], dp[j]+cnt)
            dp = nxt
        return max(dp)-1
