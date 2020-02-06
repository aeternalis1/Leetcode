class Solution(object):
    def smallestSufficientTeam(self, req_skills, people):
        """
        :type req_skills: List[str]
        :type people: List[List[str]]
        :rtype: List[int]
        """
        N = len(req_skills)
        M = len(people)
        dp = [[M+1 for x in range(1<<N)] for x in range(M+1)]
        ans = [[[] for x in range(1<<N)] for x in range(M+1)]
        masks = [0 for x in range(M)]
        for i in range(M):
            for j in people[i]:
                masks[i] |= (1<<(req_skills.index(j)))
        dp[0][0] = 0
        for i in range(M):
            for j in range(1<<N):
                if dp[i][j] > M:
                    continue
                if dp[i][j] + 1 < dp[i+1][j|masks[i]]:
                    dp[i+1][j|masks[i]] = dp[i][j] + 1
                    ans[i+1][j|masks[i]] = ans[i][j] + [i]
                if dp[i][j] < dp[i+1][j]:
                    dp[i+1][j] = dp[i][j]
                    ans[i+1][j] = ans[i][j]
        return ans[M][(1<<N)-1]
