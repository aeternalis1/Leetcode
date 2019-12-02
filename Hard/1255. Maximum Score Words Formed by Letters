class Solution(object):
    def maxScoreWords(self, words, letters, score):
        """
        :type words: List[str]
        :type letters: List[str]
        :type score: List[int]
        :rtype: int
        """
        N = len(words)
        cnt = [0 for x in range(26)]
        for i in letters:
            cnt[ord(i)-ord('a')] += 1
        ans = 0
        for i in range(1<<N):
            tmp = [0 for x in range(26)]
            for j in range(N):
                if i&(1<<j):
                    for k in words[j]:
                        tmp[ord(k)-ord('a')] += 1
            f = 0
            res = 0
            for j in range(26):
                if tmp[j] > cnt[j]:
                    f = 1
                res += tmp[j]*score[j]
            if f:
                continue
            ans = max(ans,res)
        return ans
