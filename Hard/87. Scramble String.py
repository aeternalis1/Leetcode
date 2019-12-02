def solve(s1, s2):
    if s1 == s2 or s1 == s2[::-1]:
        return True
    N = len(s1)
    for i in range(1,N):
        if sorted(s1[:i]) == sorted(s2[:i]):
            if solve(s1[:i],s2[:i]) & solve(s1[i:],s2[i:]):
                return True
        if sorted(s1[:i]) == sorted(s2[-i:]):
            if solve(s1[:i],s2[-i:]) & solve(s1[i:],s2[:-i]):
                return True
    return False

class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        return solve(list(s1),list(s2))
        
