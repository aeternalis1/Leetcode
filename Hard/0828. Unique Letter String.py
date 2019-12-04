class Solution(object):
    def uniqueLetterString(self, S):
        """
        :type S: str
        :rtype: int
        """
        lets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        N = len(S)
        ans = 0
        
        def cnt(n):
            return n*(n-1)/2
        
        for i in lets:
            arr = []
            for j in range(N):
                if S[j] == i:
                    arr.append(j)
            arr = [-1] + arr + [N]
            for j in range(1,len(arr)-1):
                ans += cnt(arr[j+1]-arr[j-1])-(cnt(arr[j]-arr[j-1])+cnt(arr[j+1]-arr[j]))
        
        return ans
