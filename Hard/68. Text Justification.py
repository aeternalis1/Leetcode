class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        N = len(words)
        W = maxWidth
        cur = []
        cnt = 0
        arr = []
        for i in range(N):
            if cnt + len(words[i]) + len(cur) > W:
                arr.append(cur)
                cur = []
                cnt = 0
            cur.append(words[i])
            cnt += len(words[i])
        ans = []
        for i in arr:
            if len(i)==1:
                ans.append(i[0]+" "*(W-len(i[0])))
                continue
            tot = sum(len(j) for j in i)
            spaces = (W-tot)/(len(i)-1)
            mod = (W-tot)%(len(i)-1)
            length = len(i)
            for j in range(length-1):
                i.insert(j*2+1," "*(spaces+(mod>0)))
                mod -= 1
            ans.append("".join(i))
        ans.append(" ".join(cur)+ " " * (W-sum(len(j) for j in cur)-len(cur)+1))
        return ans
