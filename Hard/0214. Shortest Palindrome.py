from random import randint

class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        mod = pow(10,9)+7
        base = randint(100,1000)*2+1
        N = len(s)
        pows = [1 for x in range(N+1)]
        for i in range(N):
            pows[i+1] = pows[i]*base%mod
        phash = [0 for x in range(N)]
        shash = [0 for x in range(N+1)]
        cur = 0
        for i in range(N):
            cur = (cur+ord(s[i]))*base%mod
            phash[i] = cur
        cur = 0
        for i in range(N-1,-1,-1):
            cur = (cur+ord(s[i]))*base%mod
            shash[i] = cur
        ans = 0
        for i in range(N):
            if phash[i]*pows[N-i-1]%mod == (shash[0]-shash[i+1]*pows[i+1])*pows[N-i-1]%mod:
                ans = i+1
        return s[ans:][::-1]+s
        
#equivalent to finding longest prefix palindrome
