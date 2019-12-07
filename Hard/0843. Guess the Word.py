# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Master(object):
#    def guess(self, word):
#        """
#        :type word: str
#        :rtype int
#        """

class Solution(object):
    def findSecretWord(self, wordlist, master):
        """
        :type wordlist: List[Str]
        :type master: Master
        :rtype: None
        """
        pos = wordlist
        for i in range(10):
            if not pos:
                return
            cur = pos[0]
            for j in pos:
                if j.count(j[0]) != 1:
                    cur = j
            num = master.guess(cur)
            nxt = []
            for j in pos:
                cnt = 0
                for k in range(6):
                    if j[k] == cur[k]:
                        cnt += 1
                if cnt == num and j != cur:
                    nxt.append(j)
            pos = nxt
