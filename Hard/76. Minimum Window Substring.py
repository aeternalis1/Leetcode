class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        seen = {}
        freq = {}
        M = 0
        for i in t:
            seen[i] = 0
            try:
                freq[i] += 1
            except:
                freq[i] = 1
                M += 1
        N = len(s)
        ind = 0
        ans = N+1
        res = 0
        cnt = 0
        for i in range(N):
            while ind < N and cnt < M:
                if s[ind] in seen:
                    seen[s[ind]] += 1
                    if seen[s[ind]] == freq[s[ind]]:
                        cnt += 1
                ind += 1
            if cnt == M:
                if ind-i < ans:
                    ans = ind-i
                    res = i
                ans = min(ans, ind-i)
            if s[i] in seen:
                seen[s[i]] -= 1
                if seen[s[i]] == freq[s[i]]-1:
                    cnt -= 1
        if ans == N+1:
            return ""
        else:
            return s[res:res+ans]
        
